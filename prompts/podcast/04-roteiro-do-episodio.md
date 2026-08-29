# 04 — Roteiro do episódio

- **Ferramenta:** Claude Code (Claude Opus 5, Anthropic)
- **Etapa:** o "robô roteirista" da aula, segunda tarefa
- **Conceitos aplicados:** **variáveis / blocos de substituição**, regras negativas

## Contexto

Este é o prompt onde o módulo apresenta a **passagem de variáveis**: em vez de
descrever o episódio inteiro em prosa, você monta um formato com blocos nomeados
(`[BLOCO_CURIOSIDADE_1]`) e escreve uma regra dizendo com o que cada bloco deve ser
substituído. A vantagem que a aula destaca: o formato fica fixo e reaproveitável, e
só o conteúdo varia de episódio para episódio.

## Prompt utilizado

```text
Você é um roteirista de podcast. Vamos criar o roteiro do episódio 01 do podcast
"O Segundo Par de Mãos - o podcast de quem programa acompanhado", um podcast de
tecnologia focado em IA agêntica no dia a dia de quem programa.

O público-alvo são pessoas que já programam e já usam IA para completar código,
mas ainda não usaram uma ferramenta que executa comandos no repositório delas.

O formato do roteiro deve ser:

[ABERTURA]
[BLOCO_CONCEITO]
[BLOCO_CURIOSIDADE]
[BLOCO_PRATICO]
[BLOCO_ALERTA]
[ENCERRAMENTO]

REGRAS
- Em [ABERTURA], substitua por uma abertura que dê as boas-vindas, diga o nome e
  o subtítulo do podcast e prometa o assunto do episódio.
- Em [BLOCO_CONCEITO], substitua sempre pela explicação de um conceito. Neste
  episódio: a diferença entre uma IA que sugere e uma IA que executa.
- Em [BLOCO_CURIOSIDADE], substitua sempre por uma curiosidade sobre ferramentas
  de IA para quem programa.
- Em [BLOCO_PRATICO], substitua sempre por uma situação concreta do dia a dia de
  desenvolvimento. Neste episódio: entender uma base de código que você nunca viu.
- Em [BLOCO_ALERTA], substitua sempre pelo que não se deve delegar à ferramenta.
  Este bloco se repete em todos os episódios.
- Em [ENCERRAMENTO], substitua por uma despedida curta com uma frase de efeito e
  a assinatura "Eu sou o Filipe, e esse foi O Segundo Par de Mãos".
- O podcast é apresentado por uma pessoa só, chamada Filipe.
- Escreva para ser falado, não lido: frases curtas, linguagem direta.

REGRAS NEGATIVAS
- Não ultrapasse cinco minutos de duração.
- Não use termos técnicos sem explicar.
- Não escreva rótulos de locutor como "Narrador:" dentro das falas.
- Não use listas nem marcadores: é fala corrida.
- Não prometa que a IA substitui a pessoa desenvolvedora.
```

## Resultado obtido

O roteiro está em
[`podcast/roteiro/ep01-o-que-muda-quando-a-ia-executa.md`](../../podcast/roteiro/ep01-o-que-muda-quando-a-ia-executa.md)
— **642 palavras**, seis blocos, cerca de 4,3 minutos de narração. Ficou dentro da
regra negativa dos cinco minutos.

O texto vive versionado em
[`podcast/src/roteiro.py`](../../podcast/src/roteiro.py), onde cada `Bloco` guarda a
variável do prompt, o rótulo e o texto que a substituiu. O markdown é gerado a
partir dele. Isso mantém a rastreabilidade que a aula sugere ao guardar cada prompt
junto do resultado no Notion — só que em git.

## Observações

Duas regras negativas foram decisivas na prática:

- **"Não escreva rótulos de locutor"** — a aula mostra o expert apagando à mão os
  `Narrador:` e os títulos de bloco antes de colar no sintetizador de voz, porque
  a ferramenta lê tudo em voz alta. Colocar isso como regra negativa desde o
  começo elimina o retrabalho.
- **"Não use listas nem marcadores"** — modelos tendem a responder em tópicos, e
  tópico narrado vira uma sequência de frases soltas, sem conexão.

O `[BLOCO_ALERTA]` é uma adição minha ao formato da aula. Um podcast sobre delegar
trabalho a uma máquina que nunca fala sobre os limites disso seria propaganda, não
conteúdo. Como é um bloco fixo, ele aparece em todos os episódios por construção.
