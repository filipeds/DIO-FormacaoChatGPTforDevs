# -*- coding: utf-8 -*-
"""Gera a imagem de capa do artigo (1280x720) usando Pillow.

Uso:  python imagens/gerar-capa.py
Requisitos: Pillow (pip install pillow) e as fontes Segoe UI / Consolas (Windows).
"""
import os

from PIL import Image, ImageDraw, ImageFont, ImageFilter

SAIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "capa-claude-devs.png")

S = 2                      # supersampling
W, H = 1280 * S, 720 * S

# paleta
BG1      = (10, 13, 20)
BG2      = (21, 28, 43)
CORAL    = (217, 119, 87)
CORAL_LT = (232, 168, 142)
WHITE    = (245, 243, 239)
SOFT     = (198, 203, 214)
MUTED    = (139, 147, 167)
GRAY     = (107, 116, 136)
BLUE     = (120, 160, 216)
GREEN    = (127, 184, 138)
CARD     = (13, 20, 32)
BAR      = (22, 30, 44)
BORDER   = (37, 47, 65)

F = "C:/Windows/Fonts/"
def seg(sz, w="r"):
    f = {"r": "segoeui.ttf", "b": "segoeuib.ttf",
         "l": "segoeuil.ttf", "sl": "segoeuisl.ttf"}[w]
    return ImageFont.truetype(F + f, sz * S)
def mono(sz, bold=False):
    return ImageFont.truetype(F + ("consolab.ttf" if bold else "consola.ttf"), sz * S)

base = Image.new("RGB", (W, H), BG1)

# --- fundo: gradiente diagonal -------------------------------------------
grad = Image.new("RGB", (W, H))
gd = ImageDraw.Draw(grad)
for i in range(H):
    t = i / H
    gd.line([(0, i), (W, i)], fill=(
        int(BG1[0] + (BG2[0] - BG1[0]) * t),
        int(BG1[1] + (BG2[1] - BG1[1]) * t),
        int(BG1[2] + (BG2[2] - BG1[2]) * t)))
base = grad

# --- brilhos suaves -------------------------------------------------------
def glow(cx, cy, rx, ry, color, alpha, blur):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(layer).ellipse(
        [cx - rx, cy - ry, cx + rx, cy + ry], fill=color + (alpha,))
    layer = layer.filter(ImageFilter.GaussianBlur(blur * S))
    b = base.convert("RGBA")
    b.alpha_composite(layer)
    return b.convert("RGB")

base = glow(930 * S, 330 * S, 310 * S, 240 * S, CORAL, 86, 130)
base = glow(180 * S, 640 * S, 260 * S, 180 * S, (86, 116, 196), 46, 140)

# --- malha de pontos ------------------------------------------------------
dots = Image.new("RGBA", (W, H), (0, 0, 0, 0))
dd = ImageDraw.Draw(dots)
step = 26 * S
for y in range(0, H, step):
    for x in range(0, W, step):
        dd.ellipse([x, y, x + 1 * S, y + 1 * S], fill=(255, 255, 255, 12))
b = base.convert("RGBA"); b.alpha_composite(dots); base = b.convert("RGB")

d = ImageDraw.Draw(base)

# --- bloco de texto (esquerda) -------------------------------------------
x0 = 88 * S

d.rounded_rectangle([x0, 236 * S, x0 + 46 * S, 240 * S], radius=2 * S, fill=CORAL)

def tracked(draw, x, y, text, font, fill, tr):
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tr
    return x

tracked(d, x0, 258 * S, "IA · GERAÇÃO DE CÓDIGO", seg(15, "sl"), CORAL_LT, 2.4 * S)
d.text((x0 - 2 * S, 288 * S), "Claude", font=seg(94, "b"), fill=WHITE)
d.text((x0, 404 * S), "acelerando o dia a dia", font=seg(32, "l"), fill=SOFT)
d.text((x0, 444 * S), "dos desenvolvedores",   font=seg(32, "l"), fill=SOFT)
d.text((x0, 512 * S), "IA que lê o repositório, edita arquivos e roda comandos.",
       font=seg(16), fill=MUTED)

# --- terminal (direita) ---------------------------------------------------
CX, CY, CW, CH = 660 * S, 152 * S, 540 * S, 408 * S
R = 16 * S
box = [CX, CY, CX + CW, CY + CH]

shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(shadow).rounded_rectangle(
    [box[0], box[1] + 22 * S, box[2], box[3] + 22 * S], radius=R, fill=(0, 0, 0, 160))
shadow = shadow.filter(ImageFilter.GaussianBlur(26 * S))
b = base.convert("RGBA"); b.alpha_composite(shadow); base = b.convert("RGB")
d = ImageDraw.Draw(base)

d.rounded_rectangle(box, radius=R, fill=CARD, outline=BORDER, width=1 * S)

BARH = 42 * S
d.rounded_rectangle([box[0], box[1], box[2], box[1] + BARH], radius=R, fill=BAR)
d.rectangle([box[0], box[1] + BARH - R, box[2], box[1] + BARH], fill=BAR)
d.line([(box[0], box[1] + BARH), (box[2], box[1] + BARH)], fill=BORDER, width=1 * S)
d.rounded_rectangle(box, radius=R, outline=BORDER, width=1 * S)

cy = box[1] + BARH // 2
for i, col in enumerate([(224, 108, 99), (224, 180, 79), (98, 179, 107)]):
    cx = box[0] + (24 + i * 20) * S
    d.ellipse([cx - 5 * S, cy - 5 * S, cx + 5 * S, cy + 5 * S], fill=col)

lbl = "claude-code"
fb = mono(14)
d.text((box[0] + CW // 2 - d.textlength(lbl, font=fb) / 2, cy - 9 * S),
       lbl, font=fb, fill=GRAY)

# --- linhas de codigo -----------------------------------------------------
fm, fmb = mono(16), mono(16, True)
LINES = [
    [("$ ", CORAL, fmb), ("claude", WHITE, fm)],
    [("> ", CORAL, fmb), ("crie o endpoint /perfil com testes", SOFT, fm)],
    [],
    [("● ", GREEN, fm), ("Read   ", GRAY, fm), ("src/routes/routes.js", BLUE, fm)],
    [("● ", GREEN, fm), ("Edit   ", GRAY, fm), ("src/controllers/perfil.js", BLUE, fm)],
    [("● ", GREEN, fm), ("Write  ", GRAY, fm), ("tests/perfil.test.js", BLUE, fm)],
    [("● ", GREEN, fm), ("Bash   ", GRAY, fm), ("npm test", WHITE, fm),
     ("  12 passed", GREEN, fm)],
    [],
    [("Endpoint criado e testes passando.", SOFT, fm)],
]
tx, ty, LH = box[0] + 28 * S, box[1] + BARH + 28 * S, 31 * S
for i, line in enumerate(LINES):
    x = tx
    for text, color, font in line:
        d.text((x, ty + i * LH), text, font=font, fill=color)
        x += d.textlength(text, font=font)
d.rectangle([tx, ty + len(LINES) * LH + 4 * S,
             tx + 10 * S, ty + len(LINES) * LH + 22 * S], fill=CORAL)

# --- rodape ---------------------------------------------------------------
d.text((x0, 636 * S), "DIO  ·  Gerando Artigos com Inteligência Artificial",
       font=seg(14), fill=(96, 104, 124))

base.resize((1280, 720), Image.LANCZOS).save(SAIDA, "PNG", optimize=True)
print("capa gerada em", SAIDA)
