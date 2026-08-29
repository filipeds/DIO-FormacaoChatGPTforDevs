# DIO — Formação ChatGPT for Devs

Desafios de projeto da [DIO](https://www.dio.me) sobre uso de IA generativa no
desenvolvimento e na produção de conteúdo técnico.

São **quatro entregas**: uma aplicação que consome a API da OpenAI e três peças de
conteúdo — artigo, e-book e podcast — sobre o mesmo recorte: **IA agêntica na
geração de código**.

Nas três peças de conteúdo, a IA foi usada como **aceleradora** de um conteúdo que
já existia, e o resultado passou por edição humana antes de virar entregável.
Os prompts de cada etapa estão versionados.

| # | Desafio | Entrega | Pasta |
| --- | --- | --- | --- |
| 1 | Criando um chatbot com a API da OpenAI | Aplicação React + Express | [`web/`](./web) · [`server/`](./server) |
| 2 | Gerando artigos com IA | Artigo + capa + 5 prompts | [`artigo/`](./artigo) |
| 3 | Criando um e-book com IA | PDF de 22 páginas + 8 prompts | [`ebook/`](./ebook) |
| 4 | Criando um podcast com IA | Episódio em mp3 + 6 prompts | [`podcast/`](./podcast) |

Um fio conecta as três peças de conteúdo: elas tratam do mesmo subnicho, de
propósito. A primeira aula do módulo de podcast defende que produzir dentro de um
recorte único constrói autoridade, enquanto variedade rasa não constrói nada — então
artigo, e-book e podcast falam todos sobre a diferença entre uma IA que sugere e uma
IA que executa.

---

## 🤖 1. Chatbot com a API da OpenAI

Um clone funcional do ChatGPT: front-end React conversando com uma API Express que
faz proxy para a OpenAI, para não expor a chave no navegador.

```
web/ (React)  ──POST /api/prompt──>  server/ (Express)  ──>  OpenAI  (gpt-4o-mini)
```

**Back-end** — `server/`, em camadas: `routes` → `controllers` → `config`, com o
corpo da requisição validado por um model (`InputPrompt`). A chave vive em
`server/.env` (`OPEN_AI_KEY`), fora do versionamento.

**Front-end** — `web/`, criado com Create React App: menu lateral, histórico de
conversa em estado local e `axios` para chamar a API.

```bash
cd server && npm install && node src/server.js    # porta em server/.env
cd web    && npm install && npm start             # http://localhost:3000
```

> Requer uma chave da OpenAI com créditos em `server/.env`.

---

## 🎙️ 2. Podcast — *O Segundo Par de Mãos*

**o podcast de quem programa acompanhado** · episódio 01, 4 min 20 s

> **[Ouvir o episódio (mp3)](./podcast/output/podcast-editado.mp3)** ·
> [Sobre o podcast](./podcast/README.md) ·
> [Ler o roteiro](./podcast/roteiro/ep01-o-que-muda-quando-a-ia-executa.md)

![Capa do podcast](./podcast/capa-podcast.png)

*O que muda quando a IA executa* — a diferença entre uma inteligência artificial que
sugere e uma que executa, e o que isso muda na rotina de quem programa.

O episódio é **gerado por código**: `python podcast/src/gerar_podcast.py` produz
narração, trilha, mixagem e capa.

| Etapa do módulo | Ferramenta da aula | Aqui |
| --- | --- | --- |
| Roteiro | ChatGPT | Prompt documentado, roteiro versionado em `roteiro.py` |
| Capa | Midjourney | Pillow |
| Narração | ElevenLabs | edge-tts, voz `pt-BR-AntonioNeural` |
| Edição | CapCut | numpy + ffmpeg |

**Além do que a aula faz:** a trilha lo-fi é sintetizada com numpy — livre de
direitos por construção — na duração exata da narração, e a mixagem em ffmpeg faz a
música **recuar sozinha quando a voz entra** (`sidechaincompress`), em vez de ficar
num volume fixo. O resultado é normalizado a −16 LUFS, o alvo das plataformas de
podcast.

Medido no arquivo final: −16,6 LUFS integrado · pico −1,9 dBFS · fala 14,6 dB acima
da trilha.

### Prompts usados na produção do podcast

| Etapa | Arquivo | Conceito do módulo |
| --- | --- | --- |
| 1. Nicho e estratégia | [`01-nicho-e-estrategia.md`](./prompts/podcast/01-nicho-e-estrategia.md) | Posicionamento antes do conteúdo |
| 2. Nome do podcast | [`02-nome-do-podcast.md`](./prompts/podcast/02-nome-do-podcast.md) | **Regras negativas** |
| 3. Capa | [`03-capa.md`](./prompts/podcast/03-capa.md) | Adjetivos e parâmetros de imagem |
| 4. Roteiro | [`04-roteiro-do-episodio.md`](./prompts/podcast/04-roteiro-do-episodio.md) | **Variáveis / blocos de substituição** |
| 5. Narração | [`05-narracao.md`](./prompts/podcast/05-narracao.md) | Síntese de voz |
| 6. Edição e publicação | [`06-edicao-e-publicacao.md`](./prompts/podcast/06-edicao-e-publicacao.md) | Mixagem e hospedagem |

**Repositório de referência do expert:**
https://github.com/felipeAguiarCode/prompts-for-podcast-generate-by-ia

---

## 📕 3. E-book — *O Dev Aumentado*

**Claude Code na prática: da ideia ao commit** · 22 páginas

> **[Ler o e-book (PDF)](./ebook/o-dev-aumentado.pdf)** · [Sobre o e-book](./ebook/README.md)

![Capa do e-book](./ebook/capa-ebook.png)

A diferença entre uma IA que sugere e uma IA que executa — e o que muda no dia a dia
de quem programa quando ela ganha acesso ao repositório.

| # | Capítulo | Sobre |
| --- | --- | --- |
| 01 | Da sugestão à ação | O que muda quando a IA tem mãos |
| 02 | Onboarding | Entendendo uma base que você nunca viu |
| 03 | Ponta a ponta | Funcionalidade completa, com testes |
| 04 | Debugging | Da mensagem de erro à causa raiz |
| 05 | Refatoração | Mudanças mecânicas, em escala |
| 06 | Memória de projeto | Ensinando as regras do seu time |
| 07 | Acelerador | Não substituto |

O PDF é **gerado por código** — `python ebook/src/gerar_ebook.py` produz as 22
páginas a partir de um script versionado, sem PowerPoint no caminho.

### Prompts usados na produção do e-book

| Etapa | Arquivo |
| --- | --- |
| 1. Tema e público | [`01-definicao-tema-publico.md`](./prompts/ebook/01-definicao-tema-publico.md) |
| 2. Título poderoso | [`02-titulo-poderoso.md`](./prompts/ebook/02-titulo-poderoso.md) |
| 3. Capa | [`03-capa.md`](./prompts/ebook/03-capa.md) |
| 4. Estrutura de capítulos | [`04-estrutura-capitulos.md`](./prompts/ebook/04-estrutura-capitulos.md) |
| 5. Conteúdo dos capítulos | [`05-conteudo-capitulos.md`](./prompts/ebook/05-conteudo-capitulos.md) |
| 6. Blocos de código | [`06-blocos-de-codigo.md`](./prompts/ebook/06-blocos-de-codigo.md) |
| 7. Diagramação e regra dos 8 | [`07-diagramacao-regra-8.md`](./prompts/ebook/07-diagramacao-regra-8.md) |
| 8. Post do LinkedIn | [`08-post-linkedin.md`](./prompts/ebook/08-post-linkedin.md) |

**Repositório de referência do expert:**
https://github.com/felipeAguiarCode/prompts-recipe-to-create-a-ebook

---

## 📄 4. Artigo — *Claude: como a IA da Anthropic está acelerando o dia a dia dos desenvolvedores*

> **[Ler o artigo](./artigo/claude-acelerador-de-devs.md)**

![Capa do artigo](./imagens/capa-claude-devs.png)

De assistente de chat a parceiro de codificação: como o Claude saiu do uso via chat e
passou a atuar como agente dentro do fluxo de trabalho de times de engenharia — lendo
repositórios, editando arquivos e executando comandos.

> O artigo não foi publicado em plataforma externa — ele vive neste repositório.

**Checklist do desafio:** definir o assunto ✅ · headline ✅ · imagem de capa ✅ ·
blocos do artigo ✅ · call to action ✅

### Prompts usados na produção do artigo

| Etapa | Arquivo |
| --- | --- |
| 1. Definição do assunto | [`01-definicao-assunto.md`](./prompts/01-definicao-assunto.md) |
| 2. Título e headline | [`02-titulo-headline.md`](./prompts/02-titulo-headline.md) |
| 3. Imagem de capa | [`03-imagem-capa.md`](./prompts/03-imagem-capa.md) |
| 4. Blocos do artigo | [`04-blocos-artigo.md`](./prompts/04-blocos-artigo.md) |
| 5. Call to action | [`05-call-to-action.md`](./prompts/05-call-to-action.md) |

**Repositório de referência do expert:**
https://github.com/felipeAguiarCode/prompts-for-article-generate-by-ia

---

## Conteúdo gerado por código

As três capas e o PDF do e-book foram **desenhados por código**, com Python +
Pillow — não gerados por modelo de difusão. A decisão e os prompts de referência do
Midjourney estão documentados em
[`prompts/ebook/03-capa.md`](./prompts/ebook/03-capa.md) e
[`prompts/podcast/03-capa.md`](./prompts/podcast/03-capa.md).

O motivo é o mesmo nos três casos: arte versionada em `.py` é revisável em *diff*,
reprodutível byte a byte e consistente entre as peças — e modelos de difusão erram
geometria (mãos, microfones, texto) justamente nos elementos que essas capas usam.

```bash
pip install pillow numpy edge-tts     # e ffmpeg no PATH
python imagens/gerar-capa.py          # capa do artigo
python ebook/src/gerar_ebook.py       # e-book completo + capa
python podcast/src/capa.py            # capa do podcast
python podcast/src/gerar_podcast.py   # episódio completo + capa
```

---

## Ferramentas usadas

| Ferramenta | Uso |
| --- | --- |
| **Claude (Anthropic)** | Estruturação do conteúdo, documentação dos prompts e geração das artes |
| **ChatGPT / API da OpenAI** | Redação inicial dos textos e motor do chatbot (`gpt-4o-mini`) |
| **Node + Express + React** | Aplicação do desafio 1 |
| **Python 3.12 + Pillow** | Renderização das capas e diagramação do e-book |
| **edge-tts** | Narração do podcast com voz neural pt-BR |
| **numpy + ffmpeg** | Trilha sonora sintetizada e mixagem do episódio |

---

## Estrutura do repositório

```
.
├── podcast/                           # 🎙️ desafio do podcast
│   ├── output/podcast-editado.mp3     #    o episódio (4 min 20 s)
│   ├── capa-podcast.png
│   ├── roteiro/
│   ├── README.md
│   └── src/                           #    gerador: roteiro → voz → trilha → mix
├── ebook/                             # 📕 desafio do e-book
│   ├── o-dev-aumentado.pdf            #    o e-book (22 páginas)
│   ├── capa-ebook.png
│   ├── README.md
│   └── src/                           #    gerador: conteúdo + layout + montagem
├── artigo/                            # 📄 desafio do artigo
│   └── claude-acelerador-de-devs.md
├── imagens/
│   ├── capa-claude-devs.png
│   └── gerar-capa.py
├── prompts/
│   ├── 01..05-*.md                    #    prompts do artigo
│   ├── ebook/01..08-*.md              #    prompts do e-book
│   └── podcast/01..06-*.md            #    prompts do podcast
├── server/                            # 🤖 API Node + Express + OpenAI
├── web/                               #    front-end React do chatbot
└── docs/superpowers/specs/            #    documentos de design
```

---

*Projetos desenvolvidos como desafios da [DIO](https://www.dio.me) — Formação ChatGPT for Devs.*
