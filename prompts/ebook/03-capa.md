# Etapa 3 — A capa

> ⚠️ **Leia isto antes:** a capa deste e-book **não foi gerada pelo MidJourney.**
> Ela foi desenhada por código, com Python + Pillow. O prompt do MidJourney está
> documentado abaixo como referência do método ensinado na aula, mas não foi ele
> que produziu o arquivo final. Mesmo critério adotado no desafio do artigo neste
> repositório.

## Por que não o MidJourney

Três motivos, em ordem de peso:

1. **Coerência visual.** A capa do artigo (desafio anterior) já tinha sido
   desenhada por código. Os dois desafios precisavam ler como um portfólio só.
2. **Reprodutibilidade.** O script é versionado. Qualquer pessoa clona o repo,
   roda um comando e obtém exatamente a mesma capa — o que uma imagem de modelo
   de difusão não garante.
3. **Adequação ao tema.** Um e-book sobre IA que escreve código, com a capa
   escrita em código, fecha melhor do que uma ilustração abstrata.

## O prompt do MidJourney (referência, não utilizado)

Seguindo o formato da aula — `/imagine` no bot do Discord, em inglês, com o
estilo de arte no final:

```
/imagine prompt: a developer terminal floating in dark space, glowing amber
and coral light trails flowing from the screen into abstract geometric shapes,
minimalist tech illustration, deep navy background, cinematic lighting,
high contrast, no text --ar 2:3 --v 6
```

`--ar 2:3` porque a capa é retrato (A4), e `no text` porque o título entra
depois, na diagramação — a aula insiste que o modelo não escreve texto legível.

## O que foi feito de verdade

`ebook/src/gerar_ebook.py`, função `capa()`. A composição:

| Elemento | Decisão |
| --- | --- |
| Fundo | Gradiente diagonal `#0A0D14` → `#151C2B` com malha de pontos sutil |
| Brilhos | Dois halos gaussianos (coral e azul) fora do centro, para dar profundidade |
| Título | Segoe UI Bold 136px, duas linhas, alinhado à esquerda |
| Elemento gráfico | Um bloco de terminal estilizado mostrando uma sessão real |
| Assinatura | Nome do autor no rodapé, separado por uma régua fina |

O terminal no lugar da ilustração é intencional: é a coisa mais reconhecível
para o público-alvo, e mostra a promessa do e-book em vez de descrevê-la.

## A regra que veio da aula e foi respeitada

> "Não transforme a sua capa num carnaval. Quanto mais simples, mais efetivo.
> Coloque um título e o seu nome ali, assina ele."

Título, subtítulo, chamada, um elemento gráfico, assinatura. Nada mais.
