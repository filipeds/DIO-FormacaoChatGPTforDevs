# -*- coding: utf-8 -*-
"""Mixagem final com ffmpeg — o que a aula faz à mão no CapCut.

Equivalências com o passo a passo do módulo:

  CapCut                                  aqui
  ---------------------------------       ------------------------------------
  baixar o volume da música para -20 dB    ganho calculado + sidechaincompress
  cortar a música no fim do áudio          trilha gerada na duração exata
  fade out no último trecho                afade
  export → mp3                             libmp3lame 128 kbps mono

A ordem importa: a voz é normalizada **antes** da mixagem, e só então a trilha é
posicionada em relação a ela. Normalizar a mixagem pronta parece equivalente, mas
não é — para alcançar o alvo o `loudnorm` precisaria de um ganho que estoura o
pico, cai no modo dinâmico e sobe a trilha até o nível da fala nas pausas e na
abertura. Medindo a voz sozinha, o ganho é modesto e o resto fica linear.

O `sidechaincompress` é a única coisa que a aula não faz: em vez de deixar a
trilha num volume fixo baixo o bastante para nunca atrapalhar, ela abaixa sozinha
quando a voz entra e volta a subir quando a voz para.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import roteiro

INTRO = 3.0          # segundos de trilha sozinha antes da voz entrar
OUTRO = 5.0          # segundos de trilha depois da voz terminar
ALVO_LUFS = -16      # loudness integrado, padrão de podcast
TRILHA_ABAIXO_DA_VOZ = 12   # LU entre a voz e a trilha sem duck (abertura)
TETO_TP = -1.5       # dBTP


def _db_para_linear(db: float) -> float:
    return 10 ** (db / 20)


def exigir_ffmpeg() -> None:
    if shutil.which("ffmpeg") is None or shutil.which("ffprobe") is None:
        sys.exit(
            "ffmpeg não encontrado no PATH.\n"
            "Instale em https://ffmpeg.org/download.html "
            "(no Windows:  winget install Gyan.FFmpeg)"
        )


def duracao(caminho: Path) -> float:
    saida = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "json", str(caminho)],
        check=True, capture_output=True, text=True,
    ).stdout
    return float(json.loads(saida)["format"]["duration"])


def _medir(caminho: Path) -> dict:
    """Primeira passagem do loudnorm: mede o arquivo sem escrever nada."""
    saida = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(caminho),
         "-af", f"loudnorm=I={ALVO_LUFS}:TP={TETO_TP}:LRA=11:print_format=json",
         "-f", "null", "-"],
        check=True, capture_output=True, text=True,
    ).stderr
    return json.loads(saida[saida.rindex("{"):saida.rindex("}") + 1])


def normalizar_voz(voz: Path, destino: Path) -> Path:
    """Leva a narração ao loudness alvo, em duas passagens."""
    m = _medir(voz)
    filtro = (
        f"loudnorm=I={ALVO_LUFS}:TP={TETO_TP}:LRA=11:"
        f"measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
        f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:"
        f"offset={m['target_offset']}:linear=true"
    )
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", str(voz),
         "-af", filtro, "-ar", "44100", "-ac", "1", str(destino)],
        check=True,
    )
    return destino


def mixar(voz: Path, trilha: Path, destino: Path) -> Path:
    """Junta a voz já normalizada com a trilha e escreve o mp3 final."""
    total = duracao(trilha)
    inicio_fade_out = max(total - OUTRO, 0.0)

    # A trilha é posicionada por loudness, não por um valor fixo em dB: assim o
    # equilíbrio não muda se o pad for reescrito.
    ganho_trilha = (ALVO_LUFS - TRILHA_ABAIXO_DA_VOZ) - float(_medir(trilha)["input_i"])

    filtro = (
        # A voz entra depois da abertura instrumental e é esticada com silêncio
        # até o fim, para o encerramento poder terminar sozinho.
        f"[0:a]aresample=44100,aformat=channel_layouts=mono,"
        f"adelay={int(INTRO * 1000)},apad=whole_dur={total},asplit=2[voz][chave];"
        # Trilha: ganho calculado, fade de entrada e de saída.
        f"[1:a]aresample=44100,aformat=channel_layouts=mono,"
        f"volume={ganho_trilha:.2f}dB,"
        f"afade=t=in:st=0:d=2.5,"
        f"afade=t=out:st={inicio_fade_out:.3f}:d={OUTRO}[bed];"
        # A voz controla a trilha: quando ela fala, a música recua.
        f"[bed][chave]sidechaincompress="
        f"threshold=0.02:ratio=9:attack=15:release=550[bedduck];"
        # Soma sem reescalar e garante o teto de pico, sem mexer na dinâmica.
        # `limit` é linear (não aceita dB) e `level` precisa ficar desligado —
        # ligado, ele reergue o sinal e desfaz o teto que acabou de aplicar.
        f"[voz][bedduck]amix=inputs=2:duration=longest:normalize=0,"
        f"alimiter=limit={_db_para_linear(TETO_TP):.4f}:level=disabled:latency=true[out]"
    )

    destino.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error",
         "-i", str(voz), "-i", str(trilha),
         "-filter_complex", filtro, "-map", "[out]",
         "-c:a", "libmp3lame", "-b:a", "128k", "-ac", "1", "-ar", "44100",
         "-metadata", f"title={roteiro.TITULO}",
         "-metadata", f"artist={roteiro.APRESENTADOR}",
         "-metadata", f"album={roteiro.PODCAST}",
         "-metadata", f"track={roteiro.EPISODIO}",
         "-metadata", f"comment={roteiro.DESCRICAO}",
         "-metadata", "genre=Podcast",
         "-metadata", "date=2026",
         str(destino)],
        check=True,
    )
    return destino


def duracao_da_voz_mais_bordas(voz: Path) -> float:
    """Quanto a trilha precisa durar para caber abertura, voz e encerramento."""
    return duracao(voz) + INTRO + OUTRO
