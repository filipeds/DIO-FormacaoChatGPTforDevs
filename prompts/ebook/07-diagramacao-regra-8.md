# Etapa 7 — Diagramação e a regra dos 8 pontos

Diagramar é definir onde os elementos ficam e como se repetem. A aula faz isso no
PowerPoint; aqui foi feito em Python, mas **as regras aplicadas são as mesmas**.

## A regra dos 8 pontos

> "A gente sempre vai utilizar múltiplos de 8. Se cada página tiver um padrão,
> fica estranho. Tem que ser um padrão do e-book."

E a hierarquia: **título = 2× o corpo**, subtítulo no meio.

Na aula os valores são 24 / 32 / 40 — mas repare que 40 não é o dobro de 24.
Aqui os valores foram escolhidos para satisfazer as duas regras ao mesmo tempo:

| Papel | Tamanho | Múltiplo de 8? | Relação |
| --- | --- | --- | --- |
| Corpo | 32 px | sim | base |
| Subtítulo | 48 px | sim | entre os dois |
| Título | 64 px | sim | exatamente 2× o corpo |
| Entrelinha | 48 px | sim | corpo + 16 de respiro |
| Margem | 112 px | sim | — |

Tudo isso vive no topo de `ebook/src/layout.py`, em constantes nomeadas.

## Componentes, não páginas soltas

A aula monta os componentes uma vez e depois só replica com Ctrl+C / Ctrl+V:

> "Eu vou até chamar esse cara de componente título. E esse aqui de subtítulo
> underline component. Quando eu for criar minhas páginas eu só preciso dar
> Ctrl-C e Ctrl-V nisso aqui."

O `layout.py` é a versão em código dessa ideia. Cada componente da aula virou
uma função:

| Componente da aula | Função |
| --- | --- |
| Componente de título | `titulo_pagina()` |
| Componente de texto | `paragrafos()` |
| Caixinha de gradiente ao lado do título | `barra_gradiente()` |
| Bloco de código | `bloco_codigo()` |
| Cabeçalho e rodapé / número do slide | `rodape()` |
| Página de divisória de capítulo | `pagina_escura()` |

E o conteúdo mora separado, em `conteudo.py`. Trocar um texto do e-book não exige
tocar em nenhuma linha de código de desenho — que é exatamente o benefício que o
instrutor busca ao nunca editar a página de template.

## Claro para ler, escuro para impactar

A aula é explícita sobre o fundo das páginas de conteúdo:

> "Eu sei que você é dev, eu sei que você gosta muito de telinha preta, mas...
> vá para uma linha mais neutra, mais para o branco. Para mais tempo de leitura,
> recomendo alguma coisa que não canse tanto a vista."

Por isso o e-book alterna:

- **Escuro** (`#0A0D14`) — capa, divisórias de capítulo, página final. São páginas
  de impacto, com pouco texto e leitura de segundos.
- **Claro** (`#F5F3EF`) — todas as páginas de conteúdo. São páginas de leitura.

## Paleta única

> "Tenha uma paleta de cores que você vai repetir em todo o seu e-book para tudo
> ficar em harmonia, não parecer aquele carnaval."

Uma cor de destaque só — o coral `#D97757` — usada nos bullets, na barra do
título, nos rótulos e no comando dos blocos de terminal. É a mesma cor da capa do
artigo, o que faz os dois desafios lerem como um portfólio único.

## Paginação

O PowerPoint tem numeração automática via Inserir → Cabeçalho e Rodapé. Aqui o
equivalente é a função `rodape()`, chamada com o índice da página durante a
montagem. Capa e sumário não recebem rodapé, seguindo a convenção editorial.

## Verificação de estouro

Um problema que a aula resolve no olho — texto que passa do limite da página — aqui
é verificado automaticamente. Toda página checa a altura final do conteúdo contra
o limite e o gerador reporta no fim:

```
layout: nenhuma página estourou o limite
```

Se algum texto crescer em `conteudo.py` a ponto de invadir o rodapé, o script avisa
qual página e por quanto.
