# 03 — Imagem de capa

- **Ferramenta:** Claude Code (Claude Opus 5, Anthropic) + Python 3.12 / Pillow 12.2
- **Arquivo gerado:** [`imagens/capa-claude-devs.png`](../imagens/capa-claude-devs.png)
- **Status:** ✅ concluído

## Prompt utilizado

```text
1. crie uma imagem para a capa
```

## Resultado obtido

Não havia modelo de geração de imagens (nem Lexica, nem ImageMagick) disponível no
ambiente, então o Claude Code **desenhou a capa programaticamente** com Pillow, em vez
de gerá-la por difusão. O script está versionado em
[`imagens/gerar-capa.py`](../imagens/gerar-capa.py) e regenera a imagem com
`python imagens/gerar-capa.py`.

### Especificação visual

| Item | Decisão |
| --- | --- |
| Dimensões | 1280×720 (16:9), renderizado em 2× e reduzido com LANCZOS para ficar nítido |
| Fundo | Gradiente diagonal `#0A0D14` → `#151C2B`, malha de pontos sutil |
| Iluminação | Dois brilhos gaussianos: coral atrás do terminal, azul no canto inferior esquerdo |
| Acento | Coral `#D97757` (paleta Anthropic) |
| Tipografia | Segoe UI (títulos) e Consolas (terminal) |
| Composição | Bloco de texto à esquerda, janela de terminal à direita |

### Conteúdo da capa

- Eyebrow: `IA · GERAÇÃO DE CÓDIGO`
- Título: **Claude**
- Subtítulo: "acelerando o dia a dia dos desenvolvedores"
- Apoio: "IA que lê o repositório, edita arquivos e roda comandos."
- Terminal simulando uma sessão do Claude Code (`Read` / `Edit` / `Write` / `Bash`,
  com `npm test → 12 passed`) — reforçando o argumento central do artigo: IA que
  **executa**, não apenas sugere
- Rodapé: `DIO · Gerando Artigos com Inteligência Artificial`

## Iterações

1. **1ª versão** — layout correto, mas sem acentuação (evitada no teste inicial por
   precaução com encoding), bullets renderizados como `*` e sobra de espaço vazio no
   rodapé do card do terminal.
2. **2ª versão (final)** — acentuação em português corrigida, bullets trocados para `●`,
   separador `·` no lugar de `.`, altura do card reduzida de 456px para 408px e brilho
   coral intensificado.

## Observações

Como a capa foi desenhada por código e não gerada por IA de difusão, o Lexica não foi
utilizado neste projeto. Para trocar por uma capa gerada no Lexica, basta substituir o
arquivo `imagens/capa-claude-devs.png` mantendo o mesmo nome.
