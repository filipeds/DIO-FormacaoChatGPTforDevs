# 02 — Nome do podcast

- **Ferramenta:** Claude Code (Claude Opus 5, Anthropic)
- **Etapa:** o "robô roteirista" da aula, primeira tarefa
- **Conceitos aplicados:** contexto + regras + **regras negativas**

## Contexto

Este é o prompt onde o módulo apresenta os **prompts negativos**. A lógica da aula:
quem começa só diz à ferramenta o que quer; dizer com clareza o que **não** quer é
o que tira a resposta do lugar-comum.

Na aula, o expert precisa de três rodadas de refinamento — o modelo insiste em
devolver nomes com palavras em inglês, e ele vai apertando a regra negativa a cada
rodada (`não use palavras em inglês` → `não use a palavra front-end nem variações`).
O mesmo aconteceu aqui.

## Prompt utilizado

```text
Você é um roteirista de podcast e vamos criar um podcast de tecnologia focado em
IA agêntica no dia a dia de quem programa. Eu gostaria da sua ajuda para criar
cinco sugestões de nomes criativos, com algum trocadilho nerd no nome.

O podcast vai falar sobre o que muda na rotina de desenvolvimento quando a
inteligência artificial deixa de sugerir código e passa a executar: ler o
repositório, editar arquivos, rodar comandos. O público são pessoas que já
programam e já usam IA para completar código.

REGRAS
- O nome deve ser enxuto: um nome e um subtítulo.
- O nome deve ter trocadilho com franquias nerds conhecidas, como Senhor dos
  Anéis, Star Wars, Harry Potter ou Matrix.
- O nome deve conter alguma palavra forte que remeta a programar acompanhado
  por uma máquina.
- O subtítulo deve deixar claro o assunto para quem nunca ouviu o programa.

REGRAS NEGATIVAS
- Não quero nenhuma palavra em inglês no nome nem no subtítulo.
- Não quero as palavras: dev, tech, code, cast, hub, prompt, IA, bot.
- Não quero nome óbvio do tipo "Papo de Programador" ou "Café com Código".
- Não quero nome que sugira que a IA substitui a pessoa desenvolvedora.
```

## Resultado obtido

Rodada 1 devolveu candidatos ainda genéricos e com anglicismo (`Code Fellowship`,
`Prompt Master`) — a mesma teimosia que a aula mostra. Depois de reforçar a lista
de palavras proibidas, os três finalistas foram:

| Nome | Subtítulo | Referência |
| --- | --- | --- |
| **O Segundo Par de Mãos** | o podcast de quem programa acompanhado | — |
| Concílio dos Agentes | a jornada de quem programa com inteligência artificial | Concílio de Elrond |
| Oráculo de Silício | conversas sobre máquinas que escrevem código | Oráculo de Matrix |

**Escolhido:** *O Segundo Par de Mãos — o podcast de quem programa acompanhado*.

Motivo: amarra direto na tese do e-book que já está neste repositório ("o que muda
quando a IA tem mãos"), então o nome carrega o posicionamento definido na etapa 01.
Cumpre todas as regras negativas — nenhuma palavra em inglês, nenhum termo da lista
proibida — e o próprio nome já diz que a pessoa continua no comando.

## Observações

A regra negativa que mais rendeu foi a última: *"não quero nome que sugira que a IA
substitui a pessoa desenvolvedora"*. Ela não fala sobre forma, fala sobre sentido —
e foi ela que matou metade das sugestões da primeira rodada.

Vale registrar que "O Segundo Par de Mãos" não tem trocadilho nerd, então ele
descumpre uma das regras positivas. Foi uma escolha consciente de curadoria: a aula
insiste que o papel humano no processo é justamente selecionar, e o alinhamento com
o posicionamento pesou mais que a referência nerd.
