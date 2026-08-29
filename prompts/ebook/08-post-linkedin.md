# Etapa 8 — A publicação no LinkedIn

A última aula fecha o ciclo: o e-book não foi feito para ficar na sua pasta.

> "Nenhum trabalho tem que ser feito só para você. Ele tem que ser feito para ser
> disseminado pelo mundo."

## O método da aula

1. Primeira linha com o título saltado, para prender a atenção
2. Uma indagação que enquadra o tema
3. A premissa e as ferramentas usadas
4. **Anexar como documento, não como imagem** — `Mais → Adicione um documento`
5. Dar um título ao documento (ajuda a indexar o perfil para recrutadores)
6. Pelo menos três hashtags, preferindo as que o próprio LinkedIn sugere

O passo 4 é o mais fácil de errar: só o upload como documento gera o carrossel
navegável dentro do feed. Como imagem, o e-book vira um PNG único e morre ali.

## Prompt

```
Escreva um post de LinkedIn divulgando um e-book técnico gratuito que eu
produzi, chamado "O Dev Aumentado — Claude Code na prática: da ideia ao commit".

Contexto: é um desafio de projeto da DIO, na Formação ChatGPT for Devs. O e-book
tem 22 páginas e trata da diferença entre IA que sugere e IA que executa.

Requisitos:
- Primeira linha curta e forte, que funcione sozinha no preview do feed
- Tom pessoal, sem hype e sem emoji em excesso
- Mencionar que o processo inteiro (prompts e código) está aberto no GitHub
- Terminar com 3 hashtags
- No máximo 12 linhas
```

## Texto final

```
Escrevi um e-book sobre a diferença entre IA que sugere e IA que executa.

Todo mundo já usou IA para gerar um trecho de código. Bem menos gente já
deixou uma IA abrir o repositório, editar os arquivos e rodar os testes —
e é aí que o trabalho realmente muda de forma.

"O Dev Aumentado" tem 22 páginas sobre isso: onboarding em código legado,
debugging, refatoração em escala, e um capítulo inteiro sobre o que continua
sendo trabalho seu.

Foi produzido como desafio da Formação ChatGPT for Devs, da DIO. O processo
inteiro está aberto no GitHub — os prompts de cada etapa e o script Python
que gera o PDF, página por página.

Link nos comentários. Se você produzir o seu, me marca que eu quero ler.

#ebook #InteligenciaArtificial #desenvolvimento
```

## Duas decisões contra o output

**Cortei os emojis.** A sugestão original abria com 🚀 e usava mais quatro ao
longo do texto. Para um público técnico, isso trabalha contra a credibilidade
do material.

**Tirei o superlativo.** O texto gerado dizia "um guia completo e definitivo".
Não é — são 22 páginas de recorte deliberadamente estreito, e a etapa 1 deste
repositório documenta exatamente o que ficou de fora. Prometer mais do que se
entrega é o jeito mais rápido de perder o leitor na página 3.

## O último conselho da aula

> "Quando você construir o seu, coloca no seu GitHub também. Evolui o modelo."

É o que este repositório é: o e-book, os prompts e o gerador, abertos para quem
quiser trocar o conteúdo e produzir o seu.
