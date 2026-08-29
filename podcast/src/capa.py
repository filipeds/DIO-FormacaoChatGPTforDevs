# -*- coding: utf-8 -*-
"""Capa quadrada do podcast (1400x1400), gerada com Pillow.

O módulo gera a capa no Midjourney com `--ar 1:1`. Aqui ela é desenhada por
código, como as outras capas deste repositório — o prompt de Midjourney fica
documentado em prompts/podcast/03-capa.md, como referência.

1400x1400 é o mínimo exigido por Spotify e Apple Podcasts para arte de programa.
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

LADO = 1400
S = 2                       # supersampling
W = H = LADO * S

# Mesma paleta das capas do artigo e do e-book.
BG1 = (10, 13, 20)
BG2 = (21, 28, 43)
CORAL = (217, 119, 87)
CORAL_LT = (232, 168, 142)
WHITE = (245, 243, 239)
SOFT = (198, 203, 214)
MUTED = (139, 147, 167)
GRAY = (107, 116, 136)

FONTES = "C:/Windows/Fonts/"


def seg(sz, w="r"):
    arquivo = {"r": "segoeui.ttf", "b": "segoeuib.ttf",
               "l": "segoeuil.ttf", "sl": "segoeuisl.ttf"}[w]
    return ImageFont.truetype(FONTES + arquivo, sz * S)


def mono(sz, bold=False):
    return ImageFont.truetype(FONTES + ("consolab.ttf" if bold else "consola.ttf"),
                              sz * S)


def _fundo() -> Image.Image:
    grad = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(grad)
    for i in range(H):
        t = i / H
        d.line([(0, i), (W, i)], fill=(
            int(BG1[0] + (BG2[0] - BG1[0]) * t),
            int(BG1[1] + (BG2[1] - BG1[1]) * t),
            int(BG1[2] + (BG2[2] - BG1[2]) * t)))
    return grad


def _brilho(base, cx, cy, rx, ry, cor, alfa, desfoque):
    camada = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(camada).ellipse(
        [cx - rx, cy - ry, cx + rx, cy + ry], fill=cor + (alfa,))
    camada = camada.filter(ImageFilter.GaussianBlur(desfoque * S))
    b = base.convert("RGBA")
    b.alpha_composite(camada)
    return b.convert("RGB")


def _malha(base):
    pontos = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(pontos)
    passo = 30 * S
    for y in range(0, H, passo):
        for x in range(0, W, passo):
            d.ellipse([x, y, x + 1 * S, y + 1 * S], fill=(255, 255, 255, 12))
    b = base.convert("RGBA")
    b.alpha_composite(pontos)
    return b.convert("RGB")


def _onda(d, cx, cy, largura, altura, cor):
    """Forma de onda de áudio: barras simétricas, o símbolo do programa."""
    n = 39
    passo = largura / n
    x = cx - largura / 2
    for i in range(n):
        # Duas senoides somadas dão um contorno irregular, sem parecer aleatório.
        t = i / (n - 1)
        env = math.sin(math.pi * t) ** 0.7
        det = 0.55 + 0.45 * abs(math.sin(t * 11.0) * math.cos(t * 4.3))
        h = altura * env * det
        largura_barra = passo * 0.42
        d.rounded_rectangle(
            [x - largura_barra / 2, cy - h / 2, x + largura_barra / 2, cy + h / 2],
            radius=largura_barra / 2, fill=cor)
        x += passo


def gerar_capa(destino: Path, podcast: str, subtitulo: str,
               apresentador: str) -> Path:
    base = _fundo()
    base = _brilho(base, 700 * S, 470 * S, 430 * S, 330 * S, CORAL, 74, 170)
    base = _brilho(base, 300 * S, 1140 * S, 340 * S, 250 * S, (86, 116, 196), 44, 170)
    base = _malha(base)

    d = ImageDraw.Draw(base)

    def centro(texto, fonte, y, cor):
        largura = d.textlength(texto, font=fonte)
        d.text(((W - largura) / 2, y), texto, font=fonte, fill=cor)

    def rastreado(texto, fonte, y, cor, tr):
        largura = sum(d.textlength(c, font=fonte) + tr for c in texto) - tr
        x = (W - largura) / 2
        for c in texto:
            d.text((x, y), c, font=fonte, fill=cor)
            x += d.textlength(c, font=fonte) + tr

    rastreado("PODCAST · IA AGÊNTICA", seg(21, "sl"), 300 * S, CORAL_LT, 3.4 * S)

    _onda(d, W // 2, 470 * S, 760 * S, 210 * S, CORAL)

    centro("O Segundo Par", seg(96, "b"), 620 * S, WHITE)
    centro("de Mãos", seg(96, "b"), 740 * S, WHITE)

    # Fio separador
    d.rounded_rectangle([W // 2 - 40 * S, 900 * S, W // 2 + 40 * S, 904 * S],
                        radius=2 * S, fill=CORAL)

    centro(subtitulo, seg(34, "l"), 948 * S, SOFT)
    centro(f"com {apresentador}", seg(26), 1030 * S, MUTED)

    centro("$ claude --dangerously-skip-the-boring-parts", mono(19), 1180 * S, GRAY)
    centro("DIO · Formação ChatGPT for Devs", seg(19), 1268 * S, (96, 104, 124))

    destino.parent.mkdir(parents=True, exist_ok=True)
    base.resize((LADO, LADO), Image.LANCZOS).save(destino, "PNG", optimize=True)
    return destino


if __name__ == "__main__":
    import roteiro
    print(gerar_capa(Path(__file__).resolve().parents[1] / "capa-podcast.png",
                     roteiro.PODCAST, roteiro.SUBTITULO, roteiro.APRESENTADOR))
