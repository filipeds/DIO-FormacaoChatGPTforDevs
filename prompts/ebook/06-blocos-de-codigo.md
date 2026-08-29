# Etapa 6 — Os blocos de código

Colar código como texto puro num e-book fica feio e ilegível. A aula apresenta as
ferramentas que resolvem isso, a partir de um artigo do Gael Thomas no Medium
("6 ferramentas para compartilhar imagens de código de maneira elegante").

## As ferramentas apresentadas na aula

| Ferramenta | Tipo | Observação |
| --- | --- | --- |
| [ray.so](https://ray.so) | Web | Efeito translúcido; não permite remover a sombra |
| [showcode.app](https://showcode.app) | Web | Mais controle: sombra, borda, padding, escala |
| [carbon.now.sh](https://carbon.now.sh) | Web | A mais popular; exporta PNG e SVG |
| [snappify.io](https://snappify.io) | Web | Blocos "suspensos"; exporta PDF e PNG |
| Polacode | Extensão VS Code | Captura o trecho selecionado |
| CodeSnap | Extensão VS Code | Mesma premissa |

Na aula o instrutor testa o `ray.so`, não gosta da sombra obrigatória, e acaba
padronizando no `showcode.app` com tema **Dracula**, fonte **JetBrains Mono**,
fundo transparente e largura de 600px.

## O que foi feito aqui

Os blocos deste e-book são **renderizados pelo próprio gerador** — função
`bloco_codigo()` em `ebook/src/layout.py` — em vez de exportados de uma
ferramenta web e colados como imagem.

O motivo é prático: são 8 blocos. Exportar um por um e reposicionar à mão é
exatamente o trabalho repetitivo que o e-book inteiro argumenta que deve ser
automatizado. Fazer diferente seria incoerente.

O visual replica a mesma linguagem das ferramentas da aula:

- Barra de título com os três círculos e o nome do arquivo centralizado
- Fundo escuro `#0D1420` com borda sutil, sobre página clara
- Sombra gaussiana suave (o `showcode` permite desligar; aqui ficou leve)
- Consolas no lugar de JetBrains Mono — está garantida no Windows, sem download
- Tokens coloridos por papel semântico, não por sintaxe

## Sobre os tokens

Como os blocos mostram **sessões de terminal**, não arquivos-fonte, o
colorizador é semântico em vez de sintático:

```python
TOKENS = {
    "cmd":  CORAL,   # o comando digitado
    "path": AZUL,    # arquivos tocados
    "ok":   VERDE,   # sucesso
    "warn": AMBAR,   # falha ou pergunta
    "dim":  CINZA,   # nome da ferramenta
}
```

Isso deixa a leitura da página inteira mais rápida: o leitor bate o olho e vê
o que foi pedido, o que foi mexido e o que deu certo.

## A armadilha que a aula alerta

> "Cuidado para não fazer isso aqui, esticar o seu elemento e distorcer o que
> está escrito. Usa ele do jeito que vem."

Como aqui o bloco é desenhado no tamanho final, e não redimensionado depois,
o problema não chega a existir.
