# Podcast gerado por IA — desenho do projeto

**Data:** 2026-08-29
**Branch:** `feat/podcast-ias-generativas`
**Desafio DIO:** *Criando um Podcast com Inteligência Artificial* (Formação ChatGPT for Devs)
**Repositório de referência do expert:** https://github.com/felipeAguiarCode/prompts-for-podcast-generate-by-ia

---

## 1. Objetivo

Entregar o terceiro desafio da formação — um episódio de podcast produzido com IA — mantendo
a identidade que o repositório já tem: **conteúdo gerado por código e versionado**, como o
artigo e o e-book que já vivem aqui.

O desafio pede três coisas:

1. Um repositório com os **prompts** usados na criação do projeto.
2. O **áudio do podcast editado** salvo dentro do repositório.
3. O link do repositório enviado à DIO.

## 2. O que o módulo ensina (base das transcrições)

O fluxo apresentado pelo expert, na ordem:

1. **Estratégia** — podcast sem nicho é hobby; escolher nicho e subnicho de posicionamento.
2. **Prompt engineering** — ser específico, dar contexto, estimular aplicação prática,
   comunicação clara. Depois: **prompts negativos** (dizer o que *não* se quer) e
   **variáveis / blocos de substituição** dentro do prompt.
3. **Roteirista** (ChatGPT) — gerar o nome do podcast (5 sugestões + regras + regras
   negativas, refinando em rodadas) e depois o roteiro do episódio em blocos.
4. **Artista** (Midjourney) — capa 1:1: *o que se quer* + contexto/câmera + adjetivos e
   filtros + parâmetros (`--ar`, `--v`).
5. **Narrador** (ElevenLabs) — síntese de voz, download do mp3.
6. **Editor** (CapCut) — trilha de fundo com volume reduzido, corte, *fade out*, export
   em mp3 para a pasta `output`.
7. **Publicação** — Anchor/Spotify, SoundCloud, Amazon Music, YouTube.

## 3. Decisões

### 3.1 Nicho e tema

**Nicho:** tecnologia. **Subnicho:** IA agêntica no dia a dia de quem programa.

Justificativa: o repositório já tem um artigo e um e-book sobre exatamente esse recorte.
Um podcast no mesmo subnicho transforma três desafios soltos em uma linha de autoridade
única — que é literalmente o argumento estratégico da primeira aula do módulo.

### 3.2 Nome

**O Segundo Par de Mãos** — *o podcast de quem programa acompanhado*.

Atende às regras do prompt da aula: nome enxuto com subtítulo, em português, sem palavras
em inglês, sem termos óbvios (`dev`, `tech`, `code`, `cast`). Conversa direto com a tese do
e-book do repositório ("o que muda quando a IA tem mãos").

### 3.3 Substituição de ferramentas

O ElevenLabs é pago e não há créditos disponíveis na conta OpenAI, então a narração precisa
de outro caminho. A oportunidade: em vez de trocar uma ferramenta manual por outra, tornar
**todo o pós-roteiro reproduzível por código** — coerente com o e-book, que é gerado por
`python ebook/src/gerar_ebook.py`.

| Etapa | Ferramenta da aula | Aqui | Motivo |
| --- | --- | --- | --- |
| Roteiro | ChatGPT | Prompt documentado; roteiro versionado em `roteiro.py` | O roteiro vira dado, não um texto colado à mão |
| Capa | Midjourney | Pillow (`capa.py`) | Mesma abordagem das outras capas do repo |
| Narração | ElevenLabs (pago) | `edge-tts`, voz `pt-BR-AntonioNeural` | Vozes neurais pt-BR, gratuitas, sem chave de API |
| Edição | CapCut (manual) | Trilha sintetizada por código + `ffmpeg` | Reproduzível; trilha própria elimina a questão de direitos autorais |

O prompt de capa para Midjourney é documentado na íntegra em `prompts/podcast/03-capa.md`,
como referência — a decisão de renderizar por código fica registrada ali.

### 3.4 Trilha sonora

Sintetizada em `trilha.py` com numpy: um *pad* lo-fi de acordes (ondas com harmônicos
suaves), ruído rosa de baixa amplitude e um leve *wow* de afinação para dar textura de fita.
Gerada na duração exata da narração, portanto sem o problema de "a música acaba antes do
áudio" que a aula resolve copiando e colando trechos no CapCut.

### 3.5 Mixagem

`mixagem.py`, via `ffmpeg`:

- trilha atenuada e com *ducking* sob a voz (`sidechaincompress`), replicando o "−20 dB"
  manual da aula de forma dinâmica;
- *fade in* na abertura e *fade out* no encerramento, com a trilha morrendo depois da voz;
- normalização `loudnorm` para −16 LUFS (padrão de podcast em plataformas);
- export `mp3` 128 kbps mono → `podcast/output/podcast-editado.mp3`.

## 4. Estrutura de arquivos

```
podcast/
├── README.md                       # ficha técnica, pipeline, como reproduzir
├── capa-podcast.png                # capa 1:1 gerada por código
├── roteiro/
│   └── ep01-o-que-muda-quando-a-ia-executa.md
├── output/
│   └── podcast-editado.mp3         # entregável do desafio
└── src/
    ├── gerar_podcast.py            # orquestrador da pipeline
    ├── roteiro.py                  # roteiro do episódio, em blocos (dados)
    ├── narracao.py                 # síntese de voz via edge-tts
    ├── trilha.py                   # trilha lo-fi sintetizada
    ├── mixagem.py                  # ffmpeg: ducking, fades, loudnorm, export
    └── capa.py                     # capa 1:1 com Pillow

prompts/podcast/
├── 01-nicho-e-estrategia.md
├── 02-nome-do-podcast.md
├── 03-capa.md
├── 04-roteiro-do-episodio.md
├── 05-narracao.md
└── 06-edicao-e-publicacao.md
```

Cada módulo em `src/` tem uma responsabilidade única e uma entrada pública clara
(`sintetizar()`, `gerar_trilha()`, `mixar()`, `gerar_capa()`), consumidas apenas pelo
orquestrador. `roteiro.py` não importa nada dos outros — é dado puro.

## 5. Episódio 01

**Título:** *O que muda quando a IA executa*
**Duração-alvo:** 4 a 5 minutos (a regra negativa do prompt da aula é "não ultrapasse cinco
minutos"). **Apresentador:** Filipe, voz única.

Blocos, no formato de variáveis de substituição que a aula ensina:

| Bloco | Conteúdo |
| --- | --- |
| `[ABERTURA]` | Boas-vindas, nome e subtítulo do podcast, promessa do episódio |
| `[BLOCO_CONCEITO]` | A diferença entre uma IA que sugere e uma IA que executa |
| `[BLOCO_CURIOSIDADE]` | Uma curiosidade sobre ferramentas de IA para quem programa |
| `[BLOCO_PRATICO]` | Caso concreto: entender uma base de código que você nunca viu |
| `[BLOCO_ALERTA]` | O que não delegar — revisão humana e validação |
| `[ENCERRAMENTO]` | Despedida e assinatura de encerramento |

O roteiro é escrito para ser **falado**: frases curtas, sem marcações de bloco no texto
narrado (a aula mostra que "Narrador:" e títulos de bloco precisam ser removidos antes de
enviar ao sintetizador).

## 6. Prompts documentados

Seguem o formato já usado em `prompts/` e `prompts/ebook/`: ferramenta, etapa, prompt
utilizado em bloco de código, resultado obtido e observações. Os prompts de nome e de
roteiro registram explicitamente as **regras negativas** e os **blocos de variáveis**, que
são os conceitos centrais do módulo.

## 7. Tratamento de erros

- `narracao.py` exige rede (o `edge-tts` chama o serviço da Microsoft). Sem rede, falha com
  mensagem explícita orientando a instalar a dependência ou verificar a conexão — nunca
  gerando um mp3 silencioso.
- `mixagem.py` verifica que `ffmpeg` está no `PATH` antes de começar e aborta com instrução
  de instalação se não estiver.
- `gerar_podcast.py` roda as etapas em sequência e para na primeira falha, sem deixar
  artefatos parciais em `output/`.

## 8. Verificação

Não há suíte de testes no repositório e não faz sentido criar uma para um gerador de mídia.
A verificação é por inspeção do artefato:

1. `python podcast/src/gerar_podcast.py` termina com código 0.
2. `podcast/output/podcast-editado.mp3` existe, tem duração entre 4 e 5 minutos e loudness
   integrado próximo de −16 LUFS (confirmado via `ffmpeg`/`ffprobe`).
3. `podcast/capa-podcast.png` é 1:1.
4. O áudio é ouvido antes da entrega — narração inteligível, trilha audível mas sem cobrir
   a voz, encerramento com *fade out*.

## 9. Fora de escopo

- Publicação em Spotify/Anchor/SoundCloud — apenas documentada em
  `prompts/podcast/06-edicao-e-publicacao.md`.
- Mais de um episódio.
- Interface web ou API para gerar episódios.

## 10. Restrições do repositório

- Todo o trabalho é commitado em `feat/podcast-ias-generativas`, nunca em outra branch.
- `transcricoes/` (que contém `transcricoes/podcast/`, as transcrições das aulas) **não** é
  versionada — já está no `.gitignore` e continua assim.
- O `README.md` da raiz ganha uma seção do podcast, seguindo o padrão das seções do artigo
  e do e-book.
