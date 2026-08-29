# -*- coding: utf-8 -*-
"""Gera o episódio inteiro: roteiro → narração → trilha → mixagem → mp3.

Uso:
    python podcast/src/gerar_podcast.py

Requisitos:
    pip install edge-tts numpy pillow
    ffmpeg no PATH
    conexão com a internet (a síntese de voz roda no serviço da Microsoft)

Cada etapa escreve seu artefato e a próxima consome. Se alguma falhar, o
processo para ali — o mp3 final só aparece em output/ quando todas passaram.
"""
import sys
from pathlib import Path

# O console do Windows abre em cp1252 e engasga com acento e seta no relatório.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent))

import capa           # noqa: E402
import mixagem        # noqa: E402
import narracao       # noqa: E402
import roteiro        # noqa: E402
import trilha         # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
OUTPUT = RAIZ / "output"
TRABALHO = OUTPUT / "_trabalho"

FINAL = OUTPUT / "podcast-editado.mp3"
CAPA = RAIZ / "capa-podcast.png"
ROTEIRO_MD = RAIZ / "roteiro" / "ep01-o-que-muda-quando-a-ia-executa.md"


def escrever_roteiro_md() -> Path:
    """Exporta o roteiro em markdown, com os blocos identificados."""
    linhas = [
        f"# {roteiro.PODCAST} — Episódio {roteiro.EPISODIO:02d}",
        "",
        f"## {roteiro.TITULO}",
        "",
        f"> {roteiro.DESCRICAO}",
        "",
        f"- **Apresentador:** {roteiro.APRESENTADOR}",
        f"- **Voz:** `{roteiro.VOZ}` (edge-tts)",
        f"- **Tags:** {', '.join(roteiro.TAGS)}",
        f"- **Extensão:** {roteiro.palavras()} palavras "
        f"(~{roteiro.duracao_estimada_min():.1f} min de narração)",
        "",
        "Os blocos abaixo são as variáveis de substituição do prompt do roteiro "
        "(`prompts/podcast/04-roteiro-do-episodio.md`), já resolvidas. Este "
        "arquivo é gerado a partir de `podcast/src/roteiro.py` — edite lá, "
        "não aqui.",
        "",
        "---",
        "",
    ]
    for bloco in roteiro.BLOCOS:
        linhas += [
            f"### `{bloco.variavel}` — {bloco.rotulo}",
            "",
            bloco.texto,
            "",
        ]

    ROTEIRO_MD.parent.mkdir(parents=True, exist_ok=True)
    ROTEIRO_MD.write_text("\n".join(linhas), encoding="utf-8")
    return ROTEIRO_MD


def main() -> int:
    mixagem.exigir_ffmpeg()

    OUTPUT.mkdir(parents=True, exist_ok=True)
    TRABALHO.mkdir(parents=True, exist_ok=True)

    print(f"{roteiro.PODCAST} — episódio {roteiro.EPISODIO:02d}: {roteiro.TITULO}\n")

    print("[1/5] roteiro")
    escrever_roteiro_md()
    print(f"      {roteiro.palavras()} palavras em {len(roteiro.BLOCOS)} blocos "
          f"→ {ROTEIRO_MD.relative_to(RAIZ.parent)}")

    print(f"[2/5] narração  (voz {roteiro.VOZ})")
    bruta = narracao.sintetizar(TRABALHO / "voz-bruta.mp3")
    voz = mixagem.normalizar_voz(bruta, TRABALHO / "voz.wav")
    dur_voz = mixagem.duracao(voz)
    print(f"      {dur_voz / 60:.2f} min de fala, normalizada a "
          f"{mixagem.ALVO_LUFS} LUFS")

    print("[3/5] trilha")
    dur_trilha = mixagem.duracao_da_voz_mais_bordas(voz)
    faixa = trilha.gerar_trilha(dur_trilha, TRABALHO / "trilha.wav")
    print(f"      {dur_trilha / 60:.2f} min de pad lo-fi sintetizado")

    print("[4/5] mixagem")
    mixagem.mixar(voz, faixa, FINAL)
    dur_final = mixagem.duracao(FINAL)
    tamanho = FINAL.stat().st_size / 1024
    print(f"      {dur_final / 60:.2f} min · {tamanho:.0f} KB "
          f"→ {FINAL.relative_to(RAIZ.parent)}")

    print("[5/5] capa")
    capa.gerar_capa(CAPA, roteiro.PODCAST, roteiro.SUBTITULO, roteiro.APRESENTADOR)
    print(f"      {capa.LADO}x{capa.LADO} → {CAPA.relative_to(RAIZ.parent)}")

    print("\nPronto.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
