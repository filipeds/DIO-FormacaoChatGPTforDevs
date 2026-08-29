# -*- coding: utf-8 -*-
"""Narração do roteiro com vozes neurais em português, via edge-tts.

Substitui o ElevenLabs do módulo: mesmas vozes neurais, em pt-BR, sem chave de
API e sem cota. Precisa de conexão — a síntese acontece no serviço da Microsoft.

Cada bloco do roteiro é sintetizado separadamente e depois concatenado com uma
pausa curta entre eles. Enviar o roteiro inteiro de uma vez funciona, mas a fala
sai sem respiro nas transições.
"""
import asyncio
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import edge_tts
except ImportError:  # pragma: no cover - erro de ambiente, não de lógica
    sys.exit(
        "edge-tts não está instalado.\n"
        "Instale com:  pip install edge-tts"
    )

import roteiro


async def _sintetizar_bloco(texto: str, voz: str, destino: Path) -> None:
    await edge_tts.Communicate(texto, voz).save(str(destino))


async def _sintetizar_todos(voz: str, pasta: Path) -> list[Path]:
    partes = []
    for i, bloco in enumerate(roteiro.BLOCOS, start=1):
        destino = pasta / f"bloco-{i:02d}.mp3"
        print(f"    [{i}/{len(roteiro.BLOCOS)}] {bloco.rotulo}")
        await _sintetizar_bloco(bloco.texto, voz, destino)
        if not destino.exists() or destino.stat().st_size == 0:
            raise RuntimeError(
                f"o serviço de síntese não retornou áudio para o bloco {bloco.variavel}"
            )
        partes.append(destino)
    return partes


def _concatenar(partes: list[Path], pausa: float, destino: Path) -> None:
    """Junta as partes inserindo `pausa` segundos de silêncio entre elas."""
    entradas = []
    for parte in partes:
        entradas += ["-i", str(parte)]

    # Uma trilha de silêncio serve de separador reutilizável entre os blocos.
    entradas += [
        "-f", "lavfi",
        "-t", str(pausa),
        "-i", "anullsrc=channel_layout=mono:sample_rate=24000",
    ]
    silencio = len(partes)

    sequencia = []
    for i in range(len(partes)):
        sequencia.append(f"[{i}:a]")
        if i < len(partes) - 1:
            sequencia.append(f"[{silencio}:a]")

    n = len(sequencia)
    filtro = "".join(sequencia) + f"concat=n={n}:v=0:a=1[out]"

    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", *entradas,
         "-filter_complex", filtro, "-map", "[out]", str(destino)],
        check=True,
    )


def sintetizar(destino: Path, voz: str = roteiro.VOZ) -> Path:
    """Sintetiza o roteiro inteiro e devolve o caminho do áudio de voz."""
    destino.parent.mkdir(parents=True, exist_ok=True)
    trabalho = destino.parent / "_blocos"
    if trabalho.exists():
        shutil.rmtree(trabalho)
    trabalho.mkdir()

    try:
        partes = asyncio.run(_sintetizar_todos(voz, trabalho))
        _concatenar(partes, roteiro.PAUSA_ENTRE_BLOCOS, destino)
    finally:
        shutil.rmtree(trabalho, ignore_errors=True)

    return destino


async def _listar() -> None:
    vozes = [v["ShortName"] for v in await edge_tts.list_voices()
             if v["Locale"] == "pt-BR"]
    print("\n".join(sorted(vozes)))


if __name__ == "__main__":
    # `python narracao.py --vozes` lista as vozes pt-BR disponíveis.
    if "--vozes" in sys.argv:
        asyncio.run(_listar())
    else:
        print(sintetizar(Path(__file__).resolve().parents[1] / "output" / "voz.mp3"))
