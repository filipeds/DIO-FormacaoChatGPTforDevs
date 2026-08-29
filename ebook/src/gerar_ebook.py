# -*- coding: utf-8 -*-
"""Gera o e-book "O Dev Aumentado" em PDF.

Uso:
    python ebook/src/gerar_ebook.py

Saídas:
    ebook/o-dev-aumentado.pdf   o e-book completo
    ebook/capa-ebook.png        a capa isolada (README, LinkedIn)

Requisitos: Pillow e as fontes Segoe UI / Consolas (padrão no Windows).
"""
import os
import sys
import time

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import conteudo as C            # noqa: E402
import layout as L              # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(RAIZ, "o-dev-aumentado.pdf")
CAPA_PNG = os.path.join(RAIZ, "capa-ebook.png")

# Data de publicação fixa. Sem isso o Pillow carimba a hora atual nos metadados
# do PDF, e cada execução geraria um arquivo diferente — o que sujaria o diff do
# Git sem que uma linha de conteúdo tivesse mudado.
DATA_PUBLICACAO = time.strptime("2026-08-28", "%Y-%m-%d")

_avisos = []


def _checar_altura(y, onde):
    """A página é fixa; se o conteúdo passar do rodapé, precisa ser cortado."""
    if y > L.H - 120:
        _avisos.append(f"{onde}: conteúdo termina em y={y:.0f} "
                       f"(limite {L.H - 120})")


# --------------------------------------------------------------------------
# Páginas
# --------------------------------------------------------------------------
def capa():
    img = L.pagina_escura()
    d = ImageDraw.Draw(img)

    x = L.MARGEM

    d.rounded_rectangle([L._px(x), L._px(286), L._px(x + 56), L._px(292)],
                        radius=L._px(2), fill=L.CORAL)
    L.espacar(d, x, 316, "DIO · FORMAÇÃO CHATGPT FOR DEVS",
              L.ui(20, "sl"), L.CORAL_LT, 2.4)

    d.text((L._px(x - 4), L._px(374)), "O DEV",
           font=L.ui(L.TITULO_CAPA, "b"), fill=L.BRANCO)
    d.text((L._px(x - 4), L._px(516)), "AUMENTADO",
           font=L.ui(L.TITULO_CAPA, "b"), fill=L.BRANCO)

    d.text((L._px(x), L._px(700)), C.SUBTITULO,
           font=L.ui(40, "l"), fill=L.SUAVE)

    for i, linha in enumerate(L.quebrar(d, C.CHAMADA, L.ui(L.MICRO), L.UTIL)):
        d.text((L._px(x), L._px(764 + i * 34)), linha,
               font=L.ui(L.MICRO), fill=L.MUDO)

    L.bloco_codigo(img, x, 880, L.UTIL, "claude-code", [
        [("$ ", "cmd"), ("claude", "fg")],
        [("> ", "prompt"), ("crie o endpoint /perfil com testes", "txt")],
        [],
        [("● ", "ok"), ("Read   ", "dim"), ("src/routes/routes.js", "path")],
        [("● ", "ok"), ("Edit   ", "dim"), ("src/controllers/perfil.js", "path")],
        [("● ", "ok"), ("Write  ", "dim"), ("tests/perfil.test.js", "path")],
        [("● ", "ok"), ("Bash   ", "dim"), ("npm test", "fg"),
         ("   12 passed", "ok")],
        [],
        [("Endpoint criado e testes passando.", "txt")],
    ])
    d = ImageDraw.Draw(img)

    d.line([(L._px(x), L._px(1548)), (L._px(L.W - L.MARGEM), L._px(1548))],
           fill=(52, 62, 82), width=L.S)
    d.text((L._px(x), L._px(1576)), C.AUTOR, font=L.ui(28, "b"), fill=L.BRANCO)
    d.text((L._px(x), L._px(1618)), "Desafio de projeto · DIO",
           font=L.ui(L.MICRO), fill=L.CINZA)

    return img


def sumario(indice):
    img = L.pagina_clara()
    d = ImageDraw.Draw(img)

    y = L.titulo_pagina(img, d, "Sumário")
    y += 24

    for numero, titulo, resumo, pagina in indice:
        d.text((L._px(L.MARGEM), L._px(y - 4)), f"{numero:02d}",
               font=L.ui(L.CORPO, "b"), fill=L.CORAL)
        d.text((L._px(L.MARGEM + 80), L._px(y - 6)), titulo,
               font=L.ui(L.SUBTITULO - 8, "b"), fill=L.TINTA)
        d.text((L._px(L.MARGEM + 80), L._px(y + 42)), resumo,
               font=L.ui(L.MICRO, "l"), fill=L.TINTA_FRACA)

        rotulo = str(pagina)
        largura = d.textlength(rotulo, font=L.ui(L.CORPO))
        d.text((L._px(L.W - L.MARGEM) - largura, L._px(y)), rotulo,
               font=L.ui(L.CORPO), fill=L.TINTA_FRACA)

        y += 112
        d.line([(L._px(L.MARGEM), L._px(y - 24)),
                (L._px(L.W - L.MARGEM), L._px(y - 24))],
               fill=L.LINHA, width=L.S)

    y += 40
    L.separador(d, y, L.CORAL)
    y += 40
    y = L.paragrafos(d, y, C.FICHA, cor=L.TINTA_FRACA)
    _checar_altura(y, "sumário")

    return img


def introducao(numero):
    img = L.pagina_clara()
    d = ImageDraw.Draw(img)

    y = L.titulo_pagina(img, d, C.INTRODUCAO["titulo"])
    y += 16
    y = L.paragrafos(d, y, C.INTRODUCAO["paragrafos"])
    y += 8
    y = L.destaque(img, d, y, C.INTRODUCAO["destaque"])
    y = L.paragrafos(d, y, C.INTRODUCAO["fecho"])

    _checar_altura(y, "introdução")
    L.rodape(d, numero, C.RODAPE)
    return img


def divisoria(cap, numero):
    img = L.pagina_escura(brilhos=False)
    img = L._brilho(img, 900, 1180, 360, 300, L.CORAL, 70, 150)
    d = ImageDraw.Draw(img)

    L.espacar(d, L.MARGEM, 560, "CAPÍTULO", L.ui(20, "sl"), L.CORAL_LT, 3.2)

    d.text((L._px(L.MARGEM - 12), L._px(620)), f"{cap['numero']:02d}",
           font=L.ui(L.NUM_CAPITULO, "b"), fill=(38, 48, 68))

    y = 1010
    for linha in L.quebrar(d, cap["titulo"].upper(),
                           L.ui(L.NOME_CAPITULO, "b"), L.UTIL):
        d.text((L._px(L.MARGEM), L._px(y)), linha,
               font=L.ui(L.NOME_CAPITULO, "b"), fill=L.BRANCO)
        y += L.NOME_CAPITULO + 16

    y += 16
    for linha in L.quebrar(d, cap["resumo"], L.ui(L.SUBTITULO, "l"), L.UTIL):
        d.text((L._px(L.MARGEM), L._px(y)), linha,
               font=L.ui(L.SUBTITULO, "l"), fill=L.MUDO)
        y += L.SUBTITULO + 16

    L.barra_gradiente(img, L.MARGEM, y + 40, 240, 8)

    d = ImageDraw.Draw(img)
    f = L.ui(L.RODAPE)
    largura = d.textlength(str(numero), font=f)
    d.text((L._px(L.W - L.MARGEM) - largura, L._px(L.H - 72)), str(numero),
           font=f, fill=L.CINZA)
    return img


def pagina_conteudo(pg, numero):
    img = L.pagina_clara()
    d = ImageDraw.Draw(img)

    y = L.titulo_pagina(img, d, pg["titulo"])
    y += 16
    y = L.paragrafos(d, y, pg.get("paragrafos", []))

    if pg.get("destaque"):
        y += 8
        y = L.destaque(img, d, y, pg["destaque"])

    if pg.get("codigo"):
        y += 8
        y = L.bloco_codigo(img, L.MARGEM, y, L.UTIL,
                           pg["codigo"]["arquivo"], pg["codigo"]["linhas"])
        d = ImageDraw.Draw(img)          # o bloco recompõe a imagem

    if pg.get("fecho"):
        y = L.paragrafos(d, y, pg["fecho"])

    _checar_altura(y, pg["titulo"])
    L.rodape(d, numero, C.RODAPE)
    return img


def agradecimentos(numero):
    img = L.pagina_escura()
    d = ImageDraw.Draw(img)

    y = 300
    L.espacar(d, L.MARGEM, y, "FIM", L.ui(20, "sl"), L.CORAL_LT, 3.2)
    y += 60

    for linha in L.quebrar(d, C.AGRADECIMENTOS["titulo"],
                           L.ui(L.TITULO, "b"), L.UTIL):
        d.text((L._px(L.MARGEM), L._px(y)), linha,
               font=L.ui(L.TITULO, "b"), fill=L.BRANCO)
        y += L.TITULO + 16

    y += 40
    fonte = L.ui(L.CORPO, "l")
    for bloco in C.AGRADECIMENTOS["paragrafos"]:
        for linha in L.quebrar(d, bloco, fonte, L.UTIL):
            d.text((L._px(L.MARGEM), L._px(y)), linha, font=fonte, fill=L.SUAVE)
            y += L.ENTRELINHA
        y += 24

    y += 24
    L.barra_gradiente(img, L.MARGEM, y, 240, 8)
    d = ImageDraw.Draw(img)
    y += 48

    d.text((L._px(L.MARGEM), L._px(y)), C.AGRADECIMENTOS["link"],
           font=L.ui(L.SUBTITULO - 8, "b"), fill=L.CORAL_LT)
    y += 96

    for bloco in C.AGRADECIMENTOS["fecho"]:
        for linha in L.quebrar(d, bloco, fonte, L.UTIL):
            d.text((L._px(L.MARGEM), L._px(y)), linha, font=fonte, fill=L.MUDO)
            y += L.ENTRELINHA

    _checar_altura(y, "agradecimentos")

    f = L.ui(L.RODAPE)
    largura = d.textlength(str(numero), font=f)
    d.text((L._px(L.W - L.MARGEM) - largura, L._px(L.H - 72)), str(numero),
           font=f, fill=L.CINZA)
    return img


# --------------------------------------------------------------------------
# Montagem
# --------------------------------------------------------------------------
def montar():
    """Monta a lista de páginas. Primeiro o roteiro, depois a renderização —
    assim o sumário sabe em que página cada capítulo começa."""
    roteiro = [("capa",), ("sumario",), ("intro",)]
    for cap in C.CAPITULOS:
        roteiro.append(("divisoria", cap))
        for pg in cap["paginas"]:
            roteiro.append(("conteudo", pg))
    roteiro.append(("fim",))

    indice = [
        (item[1]["numero"], item[1]["titulo"], item[1]["resumo"], i + 1)
        for i, item in enumerate(roteiro) if item[0] == "divisoria"
    ]

    paginas = []
    for i, item in enumerate(roteiro):
        n = i + 1
        tipo = item[0]
        if tipo == "capa":
            img = capa()
        elif tipo == "sumario":
            img = sumario(indice)
        elif tipo == "intro":
            img = introducao(n)
        elif tipo == "divisoria":
            img = divisoria(item[1], n)
        elif tipo == "conteudo":
            img = pagina_conteudo(item[1], n)
        else:
            img = agradecimentos(n)
        paginas.append(L.finalizar(img))

    return paginas


def main():
    paginas = montar()

    paginas[0].save(CAPA_PNG, "PNG", optimize=True)
    paginas[0].save(PDF, "PDF", save_all=True, append_images=paginas[1:],
                    resolution=150.0, title=C.TITULO, author=C.AUTOR,
                    subject=C.SUBTITULO,
                    creationDate=DATA_PUBLICACAO, modDate=DATA_PUBLICACAO)

    print(f"e-book gerado: {PDF}")
    print(f"capa gerada:   {CAPA_PNG}")
    print(f"páginas:       {len(paginas)}")

    if _avisos:
        print("\nAVISOS de estouro de página:")
        for a in _avisos:
            print("  -", a)
    else:
        print("layout: nenhuma página estourou o limite")


if __name__ == "__main__":
    main()
