# -*- coding: utf-8 -*-
"""Componentes de desenho do e-book "O Dev Aumentado".

Este módulo é o equivalente, em código, dos "componentes" que se monta uma vez
no PowerPoint e depois só se replica com Ctrl+C / Ctrl+V: um componente de
título, um de subtítulo, um de texto corrido, um de bloco de código.

Nada aqui conhece o conteúdo do e-book — só sabe desenhar. O conteúdo vive em
`conteudo.py`, e `gerar_ebook.py` costura os dois.

Regra dos 8 pontos
------------------
Todos os tamanhos de fonte e espaçamentos são múltiplos de 8, e o título tem
exatamente o dobro do corpo (64 / 32), com o subtítulo no meio (48). É a regra
de design que a aula ensina, aplicada de forma literal.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# --------------------------------------------------------------------------
# Página
# --------------------------------------------------------------------------
S = 2                              # supersampling: desenha em 2x e reduz
W, H = 1240, 1754                  # A4 retrato @ 150 dpi
WS, HS = W * S, H * S

MARGEM = 112                       # múltiplo de 8
UTIL = W - MARGEM * 2              # 1016 px de largura útil

# --------------------------------------------------------------------------
# Paleta — herdada da capa do artigo, para os dois desafios lerem como um só
# portfólio. Páginas escuras dão impacto (capa, divisórias); páginas claras
# são para leitura longa, como a aula recomenda.
# --------------------------------------------------------------------------
BG1      = (10, 13, 20)
BG2      = (21, 28, 43)
CORAL    = (217, 119, 87)
CORAL_LT = (232, 168, 142)

PAPEL      = (245, 243, 239)
TINTA      = (26, 30, 38)
TINTA_SOFT = (74, 82, 96)
TINTA_FRACA= (146, 152, 164)
LINHA      = (223, 219, 211)

CARD   = (13, 20, 32)
BAR    = (22, 30, 44)
BORDER = (37, 47, 65)

BRANCO = (245, 243, 239)
SUAVE  = (198, 203, 214)
MUDO   = (139, 147, 167)
CINZA  = (107, 116, 136)
AZUL   = (120, 160, 216)
VERDE  = (127, 184, 138)
AMBAR  = (224, 180, 79)
ROXO   = (177, 156, 217)

# cores nomeadas usadas nos snippets de código
TOKENS = {
    "cmd":  CORAL,      "prompt": CORAL,    "txt": SUAVE,
    "path": AZUL,       "ok": VERDE,        "warn": AMBAR,
    "dim":  CINZA,      "kw": ROXO,         "fg": BRANCO,
}

# --------------------------------------------------------------------------
# Tipografia
# --------------------------------------------------------------------------
_FONTES = "C:/Windows/Fonts/"

CORPO      = 32                    # base da regra dos 8
SUBTITULO  = 48                    # entre corpo e título
TITULO     = 64                    # exatamente 2x o corpo
MICRO      = 24
RODAPE     = 16

TITULO_CAPA   = 136
NUM_CAPITULO  = 320
NOME_CAPITULO = 88

ENTRELINHA = 48                    # corpo 32 + 16 de respiro


def ui(tamanho, peso="r"):
    """Segoe UI — a mesma família da capa do artigo."""
    arquivo = {"r": "segoeui.ttf", "b": "segoeuib.ttf",
               "l": "segoeuil.ttf", "sl": "segoeuisl.ttf"}[peso]
    return ImageFont.truetype(_FONTES + arquivo, tamanho * S)


def mono(tamanho, negrito=False):
    """Consolas — garantida no Windows, boa para código."""
    return ImageFont.truetype(
        _FONTES + ("consolab.ttf" if negrito else "consola.ttf"), tamanho * S)


# --------------------------------------------------------------------------
# Primitivas
# --------------------------------------------------------------------------
def _px(v):
    """Converte coordenada de página para coordenada de desenho (2x)."""
    return int(v * S)


def quebrar(d, texto, fonte, largura):
    """Quebra `texto` em linhas que cabem em `largura` (px de página)."""
    limite = _px(largura)
    linhas, atual = [], ""
    for palavra in texto.split():
        teste = (atual + " " + palavra).strip()
        if d.textlength(teste, font=fonte) <= limite:
            atual = teste
        else:
            if atual:
                linhas.append(atual)
            atual = palavra
    if atual:
        linhas.append(atual)
    return linhas


def espacar(d, x, y, texto, fonte, cor, tracking):
    """Desenha texto com espaçamento extra entre letras (para labels)."""
    px = _px(x)
    for ch in texto:
        d.text((px, _px(y)), ch, font=fonte, fill=cor)
        px += d.textlength(ch, font=fonte) + _px(tracking)


def _brilho(base, cx, cy, rx, ry, cor, alpha, blur):
    camada = Image.new("RGBA", (WS, HS), (0, 0, 0, 0))
    ImageDraw.Draw(camada).ellipse(
        [_px(cx - rx), _px(cy - ry), _px(cx + rx), _px(cy + ry)],
        fill=cor + (alpha,))
    camada = camada.filter(ImageFilter.GaussianBlur(_px(blur)))
    b = base.convert("RGBA")
    b.alpha_composite(camada)
    return b.convert("RGB")


def pagina_escura(brilhos=True):
    """Fundo com gradiente diagonal + malha de pontos. Capa e divisórias."""
    img = Image.new("RGB", (WS, HS))
    d = ImageDraw.Draw(img)
    for i in range(HS):
        t = i / HS
        d.line([(0, i), (WS, i)], fill=(
            int(BG1[0] + (BG2[0] - BG1[0]) * t),
            int(BG1[1] + (BG2[1] - BG1[1]) * t),
            int(BG1[2] + (BG2[2] - BG1[2]) * t)))

    if brilhos:
        img = _brilho(img, 980, 420, 340, 300, CORAL, 78, 140)
        img = _brilho(img, 180, 1340, 300, 240, (86, 116, 196), 44, 150)

    pontos = Image.new("RGBA", (WS, HS), (0, 0, 0, 0))
    dp = ImageDraw.Draw(pontos)
    passo = _px(26)
    for y in range(0, HS, passo):
        for x in range(0, WS, passo):
            dp.ellipse([x, y, x + S, y + S], fill=(255, 255, 255, 12))
    b = img.convert("RGBA")
    b.alpha_composite(pontos)
    return b.convert("RGB")


def pagina_clara():
    """Off-white para leitura longa — a aula desaconselha fundo preto no corpo."""
    return Image.new("RGB", (WS, HS), PAPEL)


def finalizar(img):
    """Reduz do supersampling para o tamanho final da página."""
    return img.resize((W, H), Image.LANCZOS)


# --------------------------------------------------------------------------
# Componentes
# --------------------------------------------------------------------------
def barra_gradiente(img, x, y, largura, altura, de=CORAL, para=(120, 90, 200)):
    """A 'caixinha com gradiente' que a aula usa para demarcar o título."""
    faixa = Image.new("RGB", (_px(largura), _px(altura)))
    df = ImageDraw.Draw(faixa)
    alt = _px(altura)
    for i in range(alt):
        t = i / max(alt - 1, 1)
        df.line([(0, i), (_px(largura), i)], fill=(
            int(de[0] + (para[0] - de[0]) * t),
            int(de[1] + (para[1] - de[1]) * t),
            int(de[2] + (para[2] - de[2]) * t)))
    img.paste(faixa, (_px(x), _px(y)))


def titulo_pagina(img, d, texto, y=MARGEM + 96):
    """Componente de título: barra de gradiente + texto em caixa alta."""
    linhas = quebrar(d, texto.upper(), ui(TITULO, "b"), UTIL - 56)
    altura = len(linhas) * (TITULO + 16)

    barra_gradiente(img, MARGEM, y - 16, 8, altura + 16)

    for i, linha in enumerate(linhas):
        d.text((_px(MARGEM + 40), _px(y + i * (TITULO + 16))),
               linha, font=ui(TITULO, "b"), fill=TINTA)
    return y + altura + 24


def paragrafos(d, y, blocos, cor=TINTA_SOFT, largura=UTIL, x=MARGEM):
    """Componente de texto corrido. Itens iniciados por '- ' viram bullets."""
    fonte = ui(CORPO, "l")
    for bloco in blocos:
        if bloco.startswith("- "):
            texto = bloco[2:]
            d.ellipse([_px(x + 6), _px(y + 13), _px(x + 16), _px(y + 23)],
                      fill=CORAL)
            for i, linha in enumerate(quebrar(d, texto, fonte, largura - 40)):
                d.text((_px(x + 40), _px(y)), linha, font=fonte, fill=cor)
                y += ENTRELINHA
            y += 8
        else:
            for linha in quebrar(d, bloco, fonte, largura):
                d.text((_px(x), _px(y)), linha, font=fonte, fill=cor)
                y += ENTRELINHA
            y += 24
    return y


def destaque(img, d, y, texto):
    """Citação em bloco — quebra o texto corrido e dá respiro à página."""
    fonte = ui(SUBTITULO, "l")
    linhas = quebrar(d, texto, fonte, UTIL - 72)
    altura = len(linhas) * (SUBTITULO + 16)

    d.rectangle([_px(MARGEM), _px(y), _px(MARGEM + 6), _px(y + altura)],
                fill=CORAL)
    for i, linha in enumerate(linhas):
        d.text((_px(MARGEM + 40), _px(y + i * (SUBTITULO + 16))),
               linha, font=fonte, fill=TINTA)
    return y + altura + 40


def bloco_codigo(img, x, y, largura, arquivo, linhas):
    """Bloco de código no estilo das ferramentas da aula (ray.so / showcode).

    `linhas` é uma lista de listas de tuplas (texto, token). Uma lista vazia
    representa uma linha em branco.
    """
    fonte = mono(24)
    fonte_b = mono(24, True)
    lh = 40
    barra = 56
    pad = 32
    altura = barra + pad * 2 + max(len(linhas), 1) * lh

    caixa = [_px(x), _px(y), _px(x + largura), _px(y + altura)]
    raio = _px(14)

    sombra = Image.new("RGBA", (WS, HS), (0, 0, 0, 0))
    ImageDraw.Draw(sombra).rounded_rectangle(
        [caixa[0], caixa[1] + _px(14), caixa[2], caixa[3] + _px(14)],
        radius=raio, fill=(0, 0, 0, 70))
    sombra = sombra.filter(ImageFilter.GaussianBlur(_px(16)))
    b = img.convert("RGBA")
    b.alpha_composite(sombra)
    img.paste(b.convert("RGB"), (0, 0))

    d = ImageDraw.Draw(img)
    d.rounded_rectangle(caixa, radius=raio, fill=CARD)
    d.rounded_rectangle([caixa[0], caixa[1], caixa[2], caixa[1] + _px(barra)],
                        radius=raio, fill=BAR)
    d.rectangle([caixa[0], caixa[1] + _px(barra) - raio,
                 caixa[2], caixa[1] + _px(barra)], fill=BAR)
    d.line([(caixa[0], caixa[1] + _px(barra)),
            (caixa[2], caixa[1] + _px(barra))], fill=BORDER, width=S)
    d.rounded_rectangle(caixa, radius=raio, outline=BORDER, width=S)

    cy = caixa[1] + _px(barra) // 2
    for i, cor in enumerate([(224, 108, 99), (224, 180, 79), (98, 179, 107)]):
        cx = caixa[0] + _px(28 + i * 24)
        d.ellipse([cx - _px(6), cy - _px(6), cx + _px(6), cy + _px(6)], fill=cor)

    if arquivo:
        fa = mono(20)
        d.text((caixa[0] + _px(largura) // 2 - d.textlength(arquivo, font=fa) / 2,
                cy - _px(12)), arquivo, font=fa, fill=CINZA)

    tx = x + pad
    ty = y + barra + pad - 4
    for i, linha in enumerate(linhas):
        px = _px(tx)
        for texto, token in linha:
            f = fonte_b if token in ("cmd", "prompt") else fonte
            d.text((px, _px(ty + i * lh)), texto, font=f,
                   fill=TOKENS.get(token, SUAVE))
            px += d.textlength(texto, font=f)

    return y + altura + 40


def rodape(d, numero, texto):
    """Paginação automática — o equivalente ao cabeçalho/rodapé do PowerPoint."""
    y = H - 72
    f = ui(RODAPE)
    d.line([(_px(MARGEM), _px(y - 20)), (_px(W - MARGEM), _px(y - 20))],
           fill=LINHA, width=S)
    d.text((_px(MARGEM), _px(y)), texto, font=f, fill=TINTA_FRACA)
    largura = d.textlength(str(numero), font=f)
    d.text((_px(W - MARGEM) - largura, _px(y)), str(numero), font=f,
           fill=TINTA_FRACA)


def separador(d, y, cor=LINHA):
    """Separador simples entre seções."""
    d.line([(_px(MARGEM), _px(y)), (_px(MARGEM + 120), _px(y))],
           fill=cor, width=_px(3))
