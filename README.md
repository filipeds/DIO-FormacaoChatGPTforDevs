# Gerando Artigos com Inteligência Artificial

Desafio de projeto do bootcamp **DIO — Formação ChatGPT for Devs**. A proposta é usar
ferramentas de IA generativa (texto e imagem) para produzir um artigo técnico completo,
documentando cada etapa do processo: da definição do assunto até o call to action final.

Este repositório reúne o artigo produzido, os prompts utilizados em cada etapa e a
imagem de capa gerada.

---

## Sobre o artigo

**Tema:** Claude e o uso de IA na geração de código e como acelerador de desenvolvedores.

O artigo explica como o Claude, da Anthropic, saiu do uso via chat e passou a atuar como
agente dentro do fluxo de trabalho de times de engenharia — lendo repositórios, editando
arquivos e executando comandos — e como isso encurta o caminho entre a ideia e o código
funcional, sem substituir o julgamento técnico do desenvolvedor.

📄 **Leia o artigo:** [`artigo/claude-acelerador-de-devs.md`](./artigo/claude-acelerador-de-devs.md)

> O artigo não foi publicado em plataforma externa — ele vive neste repositório.

![Capa do artigo](./imagens/capa-claude-devs.png)

---

## Repositório de referência

Este projeto foi inspirado (forkado) no repositório do expert Felipe Aguiar:

👉 https://github.com/felipeAguiarCode/prompts-for-article-generate-by-ia

---

## Checklist do artigo

- [x] Definir o assunto
- [x] Título chamativo (headline)
- [x] Imagem de capa chamativa
- [x] Blocos do artigo
- [x] Call to action no final do post

---

## Prompts utilizados

Cada arquivo documenta o prompt real enviado à IA e o resultado obtido naquela etapa:

| Etapa | Arquivo |
| --- | --- |
| 1. Definição do assunto | [`prompts/01-definicao-assunto.md`](./prompts/01-definicao-assunto.md) |
| 2. Título e headline | [`prompts/02-titulo-headline.md`](./prompts/02-titulo-headline.md) |
| 3. Imagem de capa | [`prompts/03-imagem-capa.md`](./prompts/03-imagem-capa.md) |
| 4. Blocos do artigo | [`prompts/04-blocos-artigo.md`](./prompts/04-blocos-artigo.md) |
| 5. Call to action | [`prompts/05-call-to-action.md`](./prompts/05-call-to-action.md) |

---

## Imagens geradas

| Arquivo | Descrição |
| --- | --- |
| [`imagens/capa-claude-devs.png`](./imagens/capa-claude-devs.png) | Capa do artigo — 1280×720, tema escuro com terminal simulando uma sessão do Claude Code |
| [`imagens/gerar-capa.py`](./imagens/gerar-capa.py) | Script que gera a capa (`python imagens/gerar-capa.py`) |

A capa foi **desenhada por código** com Python + Pillow, e não gerada por um modelo de
difusão. Os detalhes da composição estão em [`prompts/03-imagem-capa.md`](./prompts/03-imagem-capa.md).

---

## Tecnologias e ferramentas usadas

| Ferramenta | Uso no projeto |
| --- | --- |
| **Claude (Anthropic)** | Via Claude Code: estruturação do repositório, documentação dos prompts e criação da capa |
| **Python 3.12 + Pillow** | Renderização da imagem de capa |
| **ChatGPT** | Redação inicial do texto do artigo |

---

## Estrutura do repositório

```
.
├── artigo/
│   └── claude-acelerador-de-devs.md   # o artigo
├── imagens/
│   ├── capa-claude-devs.png           # capa gerada
│   └── gerar-capa.py                  # script que gera a capa
├── prompts/                           # prompts de cada etapa
│   ├── 01-definicao-assunto.md
│   ├── 02-titulo-headline.md
│   ├── 03-imagem-capa.md
│   ├── 04-blocos-artigo.md
│   └── 05-call-to-action.md
├── server/                            # API Node + OpenAI (desafio anterior)
└── web/                               # front-end React (desafio anterior)
```

---

*Projeto desenvolvido como parte do desafio "Gerando Artigos com Inteligência Artificial" da [DIO](https://www.dio.me).*
