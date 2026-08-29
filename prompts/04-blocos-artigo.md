# 04 — Blocos do artigo

- **Ferramenta:** Claude Code (Claude Opus 5, Anthropic)
- **Etapa:** organização do corpo do artigo no repositório

## Prompt utilizado

```text
1. Crie a pasta /artigo (se não existir) e dentro dela o arquivo
   "claude-acelerador-de-devs.md" com o seguinte conteúdo:

--- INÍCIO DO CONTEÚDO DO ARTIGO ---
[texto completo do artigo, com todos os blocos já escritos]
--- FIM DO CONTEÚDO DO ARTIGO ---
```

## Resultado obtido

O Claude Code criou `artigo/claude-acelerador-de-devs.md` com o conteúdo **literal**
enviado no prompt (12 headings, sem reescrita). A estrutura final ficou:

| Bloco | Seção no artigo |
| --- | --- |
| 1 | O assunto: por que falar de Claude e geração de código agora? |
| 2 | Do chat ao terminal: a evolução do Claude para devs |
| 3 | Como o Claude acelera o trabalho do desenvolvedor (5 tópicos) |
| 4 | Claude como "acelerador", não substituto |
| 5 | Conclusão |
| 6 | Call to action |

Os 5 tópicos do bloco 3: onboarding e código legado, geração de funcionalidades ponta
a ponta, debugging assistido, refatoração e manutenção, e memória de projeto com
arquivos de contexto.

## Ajuste feito pelo Claude Code

O único desvio em relação ao texto original foi o caminho da imagem de capa: o prompt
trazia `./imagens/capa-claude-devs.png`, que a partir de `artigo/` resolveria para
`artigo/imagens/`. O caminho foi corrigido para `../imagens/capa-claude-devs.png`,
apontando para a pasta `imagens/` na raiz do repositório.
