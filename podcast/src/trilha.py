# -*- coding: utf-8 -*-
"""Trilha lo-fi sintetizada por código.

No módulo, a música de fundo vem da biblioteca do CapCut e o problema é encaixar
a duração: a aula resolve copiando e colando o trecho até cobrir a narração.
Aqui a trilha é gerada na duração exata pedida, e sem questão de direitos
autorais — ela não existia antes de rodar este arquivo.

O som: um pad de acordes em lá menor, com harmônicos suaves, ruído escuro de
fundo e uma oscilação lenta de afinação que imita a instabilidade de fita.
"""
import math
import wave
from pathlib import Path

import numpy as np

SR = 44100

# Progressão em lá menor. Cada acorde é uma tríade em frequências (Hz).
PROGRESSAO = [
    (220.00, 261.63, 329.63),   # Am
    (174.61, 220.00, 261.63),   # F
    (130.81, 164.81, 196.00),   # C
    (196.00, 246.94, 293.66),   # G
]

DURACAO_ACORDE = 3.4      # segundos por acorde
SOBREPOSICAO = 0.9        # crossfade entre acordes consecutivos
HARMONICOS = (1.0, 0.35, 0.14)   # pesos do fundamental, 2ª e 3ª harmônica
DETUNE = 0.7              # desafinação em Hz entre as duas vozes de cada nota
WOW_HZ = 0.27             # frequência da oscilação de afinação
WOW_PROF = 0.055          # profundidade, em radianos de fase
NIVEL_RUIDO = 0.016


def _voz(freq: float, n: int, rng: np.random.Generator) -> np.ndarray:
    """Uma nota: soma de harmônicos, duas vozes desafinadas, com wow de fita."""
    t = np.arange(n) / SR
    wow = WOW_PROF * np.sin(2 * math.pi * WOW_HZ * t + rng.uniform(0, 2 * math.pi))
    saida = np.zeros(n)
    for desvio in (-DETUNE / 2, DETUNE / 2):
        fase = 2 * math.pi * (freq + desvio) * t + wow
        for h, peso in enumerate(HARMONICOS, start=1):
            saida += peso * np.sin(h * fase)
    return saida / (len(HARMONICOS) * 2)


def _passa_baixa(sinal: np.ndarray, janela: int) -> np.ndarray:
    """Média móvel — o suficiente para escurecer o ruído e tirar o brilho."""
    nucleo = np.ones(janela) / janela
    return np.convolve(sinal, nucleo, mode="same")


def gerar_trilha(duracao: float, destino: Path, semente: int = 20260829) -> Path:
    """Escreve um WAV mono de `duracao` segundos com o pad lo-fi.

    A semente é fixa de propósito: rodar de novo produz exatamente o mesmo
    arquivo, como acontece com as capas e o PDF do e-book neste repositório.
    """
    rng = np.random.default_rng(semente)
    total = int(duracao * SR)

    passo = DURACAO_ACORDE - SOBREPOSICAO
    n_acorde = int(DURACAO_ACORDE * SR)
    envelope = np.hanning(n_acorde)

    # A folga cabe um acorde inteiro: o último começa antes de `total` e passa
    # do fim. O excedente é cortado depois do laço.
    faixa = np.zeros(total + n_acorde)

    i = 0
    while i * passo * SR < total:
        acorde = PROGRESSAO[i % len(PROGRESSAO)]
        inicio = int(i * passo * SR)
        pedaco = np.zeros(n_acorde)
        for freq in acorde:
            pedaco += _voz(freq, n_acorde, rng)
        faixa[inicio:inicio + n_acorde] += pedaco * envelope / len(acorde)
        i += 1

    faixa = faixa[:total]

    ruido = _passa_baixa(rng.standard_normal(total), 180)
    ruido /= np.max(np.abs(ruido)) or 1.0
    faixa += ruido * NIVEL_RUIDO

    faixa = _passa_baixa(faixa, 12)

    pico = np.max(np.abs(faixa)) or 1.0
    faixa = faixa / pico * 0.5

    destino.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(destino), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((faixa * 32767).astype("<i2").tobytes())

    return destino


if __name__ == "__main__":
    print(gerar_trilha(30.0, Path(__file__).resolve().parents[1] / "output" / "trilha.wav"))
