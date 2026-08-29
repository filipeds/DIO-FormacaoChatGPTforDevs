# 05 — Narração

- **Ferramentas:** ElevenLabs (caminho da aula) · edge-tts (execução)
- **Etapa:** o "robô narrador" da aula

## Contexto

A aula usa o ElevenLabs: cola o roteiro, escolhe uma voz (Adam, Sam, Antoni),
gera e baixa o mp3. O expert deixa claro que a ferramenta não é gratuita — dá 10
mil caracteres de crédito no cadastro, e ele gasta quase tudo nesse único
episódio. Sem login, o limite é de 333 caracteres por vez.

Ele também mostra dois cuidados que valem para qualquer sintetizador:

1. Tirar do texto os rótulos (`Narrador:`, títulos de bloco), senão eles são lidos.
2. A qualidade cai ao longo de textos longos no plano gratuito.

## O que foi feito aqui

Sem créditos disponíveis, a narração usa **edge-tts** — as vozes neurais do serviço
de leitura em voz alta do Microsoft Edge, acessíveis por uma biblioteca Python, sem
chave de API e sem cota.

Vozes pt-BR disponíveis:

```bash
python podcast/src/narracao.py --vozes
```

```text
pt-BR-AntonioNeural
pt-BR-FranciscaNeural
pt-BR-ThalitaMultilingualNeural
```

**Escolhida:** `pt-BR-AntonioNeural` — voz masculina, já que o roteiro é assinado
em primeira pessoa por Filipe.

## Tratamento aplicado

O código está em [`podcast/src/narracao.py`](../../podcast/src/narracao.py).

**Cada bloco é sintetizado separadamente** e depois concatenado com 0,75 s de
silêncio entre eles. Enviar o roteiro inteiro de uma vez funciona, mas as
transições entre blocos saem sem respiro — o sintetizador emenda o encerramento de
um assunto no começo do outro como se fosse a mesma frase. A pausa é o equivalente
em código do corte que se daria na linha do tempo do editor.

O roteiro já chega limpo ao sintetizador: como a regra negativa da etapa 04 proíbe
rótulos de locutor, não há o passo manual de limpeza que a aula mostra.

## Observações

O que se ganha com a troca: sem custo, sem limite de caracteres, e a narração passa
a ser reproduzível — qualquer pessoa que clonar o repositório roda o gerador e
obtém o mesmo áudio, o que não acontece com um mp3 baixado de uma interface web.

O que se perde: o ElevenLabs tem controle fino de estabilidade e clareza da voz, e
uma entrega mais expressiva. O edge-tts entrega uma leitura correta e natural, mas
mais neutra. Para um episódio informativo de quatro minutos, a diferença não
compromete — para um podcast narrativo, comprometeria.

A dependência de rede é real e está tratada: a síntese roda no serviço da
Microsoft, e o gerador falha com mensagem explícita se não houver conexão, em vez
de produzir um arquivo silencioso.
