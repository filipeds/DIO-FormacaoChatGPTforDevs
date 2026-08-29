# O Segundo Par de Mãos

*o podcast de quem programa acompanhado*

![Capa do podcast](./capa-podcast.png)

Desafio da [DIO](https://www.dio.me) — *Criando um Podcast com Inteligência
Artificial*. Um podcast de tecnologia sobre **IA agêntica no dia a dia de quem
programa**: o que muda quando a inteligência artificial deixa de sugerir código e
passa a executar.

> **[Ouvir o episódio 01 (mp3)](./output/podcast-editado.mp3)** ·
> [Ler o roteiro](./roteiro/ep01-o-que-muda-quando-a-ia-executa.md)

---

## Episódio 01 — *O que muda quando a IA executa*

| | |
| --- | --- |
| Duração | 4 min 20 s |
| Apresentação | Filipe |
| Voz | `pt-BR-AntonioNeural` (edge-tts) |
| Roteiro | 642 palavras, 6 blocos |
| Loudness | −16,6 LUFS · pico −1,9 dBFS |

Blocos do episódio, no formato de variáveis de substituição que o módulo ensina:

| Bloco | Assunto |
| --- | --- |
| `[ABERTURA]` | Boas-vindas e promessa do episódio |
| `[BLOCO_CONCEITO]` | A diferença entre uma IA que sugere e uma que executa |
| `[BLOCO_CURIOSIDADE]` | Um agente de código passa mais tempo lendo do que escrevendo |
| `[BLOCO_PRATICO]` | O primeiro dia numa base que você nunca viu |
| `[BLOCO_ALERTA]` | O que não delegar |
| `[ENCERRAMENTO]` | Despedida |

---

## O episódio é gerado por código

O módulo produz o podcast com quatro ferramentas de interface gráfica. Aqui, tudo
depois do roteiro é executado por um script — no mesmo espírito do e-book deste
repositório, que também é gerado por código.

```bash
pip install edge-tts numpy pillow      # e ffmpeg no PATH
python podcast/src/gerar_podcast.py
```

```
[1/5] roteiro     642 palavras em 6 blocos
[2/5] narração    edge-tts, voz pt-BR-AntonioNeural, um bloco por vez
[3/5] trilha      pad lo-fi sintetizado na duração exata da narração
[4/5] mixagem     ducking, fades, limitador → mp3 128 kbps
[5/5] capa        1400x1400
```

### Equivalências com o passo a passo da aula

| Etapa | Ferramenta do módulo | Aqui | Por quê |
| --- | --- | --- | --- |
| Roteiro | ChatGPT | Prompt documentado, roteiro versionado em `roteiro.py` | O roteiro vira dado; o markdown é gerado a partir dele |
| Capa | Midjourney | Pillow (`capa.py`) | Sem plano gratuito; e as outras capas do repo já são por código |
| Narração | ElevenLabs | edge-tts (`narracao.py`) | Vozes neurais pt-BR sem chave de API nem cota |
| Edição | CapCut | numpy + ffmpeg (`trilha.py`, `mixagem.py`) | Reproduzível, e a trilha própria elimina a questão de direitos autorais |

O prompt de Midjourney e o passo a passo do CapCut ficam documentados na íntegra em
[`prompts/podcast/`](../prompts/podcast/), como referência para quem for replicar
pelo caminho original.

### O que foi além da aula

- A trilha **abaixa sozinha quando a voz entra** (`sidechaincompress`), em vez de
  ficar num volume fixo baixo. A aula deixa a música em −20 dB o episódio inteiro.
- A trilha é **sintetizada na duração exata** da narração, então não existe o
  problema de copiar e colar a faixa até cobrir o áudio.
- O resultado é normalizado a **−16 LUFS**, o alvo das plataformas de podcast.
- A trilha é **livre de direitos por construção** — ela não existia antes de rodar
  `trilha.py`.

---

## Prompts usados na produção

| Etapa | Arquivo | Conceito do módulo |
| --- | --- | --- |
| 1. Nicho e estratégia | [`01-nicho-e-estrategia.md`](../prompts/podcast/01-nicho-e-estrategia.md) | Posicionamento antes do conteúdo |
| 2. Nome do podcast | [`02-nome-do-podcast.md`](../prompts/podcast/02-nome-do-podcast.md) | **Regras negativas** |
| 3. Capa | [`03-capa.md`](../prompts/podcast/03-capa.md) | Adjetivos e parâmetros de imagem |
| 4. Roteiro | [`04-roteiro-do-episodio.md`](../prompts/podcast/04-roteiro-do-episodio.md) | **Variáveis / blocos de substituição** |
| 5. Narração | [`05-narracao.md`](../prompts/podcast/05-narracao.md) | Síntese de voz |
| 6. Edição e publicação | [`06-edicao-e-publicacao.md`](../prompts/podcast/06-edicao-e-publicacao.md) | Mixagem e hospedagem |

**Repositório de referência do expert:**
https://github.com/felipeAguiarCode/prompts-for-podcast-generate-by-ia

---

## Estrutura

```
podcast/
├── capa-podcast.png                # 1400x1400, gerada por código
├── roteiro/
│   └── ep01-*.md                   # gerado a partir de src/roteiro.py
├── output/
│   └── podcast-editado.mp3         # o entregável do desafio
└── src/
    ├── gerar_podcast.py            # orquestra a pipeline
    ├── roteiro.py                  # roteiro em blocos (dado puro)
    ├── narracao.py                 # síntese de voz
    ├── trilha.py                   # trilha lo-fi sintetizada
    ├── mixagem.py                  # ducking, fades, limitador, mp3
    └── capa.py                     # capa com Pillow
```

A trilha e a capa são determinísticas — a semente do pad é fixa, e regerar produz
arquivos byte a byte idênticos. A narração passa por um serviço remoto, então o mp3
final pode variar entre execuções; o arquivo versionado em `output/` é o entregável
oficial.
