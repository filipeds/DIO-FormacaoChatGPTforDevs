# 06 — Edição e publicação

- **Ferramentas:** CapCut (caminho da aula) · ffmpeg + numpy (execução)
- **Etapa:** o "robô editor" da aula, e o fechamento do projeto

## Contexto

A última aula prática monta o episódio no CapCut. O passo a passo:

1. Importar o mp3 da narração.
2. Ajustar o volume dos trechos estourados e, opcionalmente, reduzir ruído.
3. Buscar uma música na biblioteca (o expert procura por *lo-fi*) e adicionar.
4. Baixar a música para −20 dB, "só para não ocupar o espaço da voz".
5. Copiar e colar a música até cobrir a narração inteira — ou procurar uma faixa
   com a duração do episódio.
6. Cortar o excedente com *Split* e aplicar *fade out* no final.
7. Exportar desmarcando "vídeo", marcando "áudio", em mp3.

## O que foi feito aqui

A mesma sequência, expressa em código: [`podcast/src/trilha.py`](../../podcast/src/trilha.py)
e [`podcast/src/mixagem.py`](../../podcast/src/mixagem.py).

| Passo do CapCut | Equivalente aqui |
| --- | --- |
| Buscar música lo-fi na biblioteca | Pad sintetizado com numpy: acordes em lá menor, harmônicos suaves, ruído escuro e oscilação lenta de afinação (efeito de fita) |
| Copiar e colar até cobrir a narração | A trilha é gerada já na duração exata da voz mais a abertura e o encerramento |
| Baixar a música para −20 dB | Ganho calculado por *loudness* + `sidechaincompress` |
| *Split* e *fade out* | `afade` |
| Exportar em mp3 | `libmp3lame` 128 kbps mono, com metadados ID3 |

Gerar a trilha por código resolve de brinde a questão de direitos autorais: a
biblioteca do CapCut é licenciada para uso dentro da plataforma, e um podcast
publicado em outro lugar entra em zona cinzenta. Esta trilha não existia antes de
rodar o arquivo.

### O que a aula não faz

A trilha **abaixa sozinha quando a voz entra** (`sidechaincompress`), em vez de
ficar num volume fixo baixo o bastante para nunca atrapalhar. É o que deixa a
abertura e o encerramento respirarem sem que a música brigue com a narração no
meio.

E o resultado é normalizado a −16 LUFS, que é o alvo usado pelas plataformas de
podcast — o CapCut não expõe esse controle.

Medições do arquivo final:

| Medida | Valor |
| --- | --- |
| Loudness integrado | −16,6 LUFS |
| Pico | −1,9 dBFS |
| Fala | −16,6 dB RMS |
| Trilha sozinha (abertura) | −31,2 dB RMS |
| Duração | 4 min 20 s |

## Publicação

A aula encerra listando onde hospedar. Nenhuma publicação foi feita — o episódio
vive neste repositório, em
[`podcast/output/podcast-editado.mp3`](../../podcast/output/podcast-editado.mp3).

| Plataforma | Observação da aula |
| --- | --- |
| [Spotify for Podcasters](https://podcasters.spotify.com/) (ex-Anchor) | Caminho mais comum para chegar ao Spotify; passa por aprovação |
| [SoundCloud](https://soundcloud.com/) | Cota gratuita suficiente para montar um repertório |
| [Amazon Music](https://music.amazon.com/podcasts) | Exige seguir a documentação de submissão |
| YouTube | Sobe o áudio como vídeo, com a capa parada |

## Observações

O expert fecha dizendo que gerou o podcast inteiro em menos de uma hora. Aqui a
maior parte do tempo foi em depuração de mixagem, não em produção de conteúdo — e
uma dessas depurações vale registro:

A primeira versão normalizava a **mixagem pronta**. Parece equivalente a
normalizar antes, mas não é: para alcançar −16 LUFS o ganho necessário estourava o
pico, então o `loudnorm` caía no modo dinâmico e empurrava os trechos baixos para
cima. Na prática, a trilha subia até o nível da fala na abertura e em cada pausa
entre blocos. A separação entre abertura e fala, que deveria ser de ~14 dB, tinha
virado 0,7 dB.

A correção foi inverter a ordem — normalizar a voz sozinha primeiro e posicionar a
trilha em relação a ela, deixando só um limitador de pico no fim. É o tipo de erro
que não aparece olhando o código e nem sempre aparece ouvindo: aparece medindo.
