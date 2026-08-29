# 03 — Capa do podcast

- **Ferramentas:** Midjourney (prompt de referência) · Claude Code + Pillow (execução)
- **Etapa:** o "robô artista" da aula
- **Conceitos aplicados:** estrutura de prompt de imagem, adjetivos, parâmetros

## Contexto

A aula ensina o formato de um prompt de Midjourney:

> **o que você quer** + **palavras de contexto / configuração de câmera** +
> **adjetivos e filtros** + **parâmetros** (`--ar`, `--v`)

E a regra prática: quanto mais adjetivos, mais específica a imagem. O expert também
mostra o peso de palavra (`::5`) e o refinamento por rodadas — no vídeo ele precisa
tirar "castelo" do prompt porque o modelo focou no cenário em vez do personagem.

## Prompt de Midjourney (referência)

Este é o prompt escrito para a capa, no formato da aula:

```text
/imagine prompt: a pair of hands typing on a mechanical keyboard, a second
translucent pair of robotic hands overlapping them in the same gesture, dark
studio desk, warm coral rim light against deep navy background, shallow depth
of field, camera settings f1.8 ISO 200, cinematic lighting, global illumination,
ultra detailed, photorealistic, 16k, muted color grading, minimal composition,
negative space at the top --ar 1:1 --v 5.2

--no text, no letters, no watermark, no extra fingers, no clutter
```

O `--ar 1:1` é o formato quadrado que a aula usa para capa. O bloco `--no` é o
prompt negativo do Midjourney.

## Resultado obtido

A capa **não** foi gerada pelo Midjourney. Ela está em
[`podcast/capa-podcast.png`](../../podcast/capa-podcast.png), desenhada por código
com Pillow, em [`podcast/src/capa.py`](../../podcast/src/capa.py) — 1400×1400, que
é o mínimo exigido por Spotify e Apple Podcasts para arte de programa.

Motivos da troca:

1. O Midjourney não tem plano gratuito desde 2023 — a conta de teste que a aula usa
   não existe mais.
2. As outras duas capas deste repositório (artigo e e-book) já são geradas por
   código. Manter a mesma paleta e a mesma tipografia faz as três peças parecerem
   de um mesmo projeto.
3. Uma capa versionada em `.py` é revisável em *diff* e reprodutível — regerar dá
   exatamente o mesmo arquivo.

O elemento central é uma forma de onda de áudio em coral sobre o fundo azul-escuro
da identidade do repositório: diz "podcast" sem precisar de ilustração figurativa,
e o desenho por código é confiável em geometria de um jeito que um modelo de
difusão não é (o próprio vídeo mostra o Midjourney errando mãos e microfones).

## Observações

O prompt acima fica registrado porque é o entregável conceitual da etapa — quem for
replicar com Midjourney tem o formato pronto. A decisão de renderizar por código é
de execução, não de conteúdo.

O trecho `no extra fingers` no prompt negativo é o vício clássico de modelos de
difusão com mãos — e "mãos" é justamente o símbolo do programa. Foi o que pesou
mais na decisão de desenhar em vez de gerar.
