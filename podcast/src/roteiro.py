# -*- coding: utf-8 -*-
"""Roteiro do episódio, em blocos.

Este módulo é dado puro: não importa nada dos outros módulos da pipeline e não
executa nada. Os blocos seguem o padrão de variáveis de substituição ensinado no
módulo — cada `[NOME_DO_BLOCO]` do prompt virou um item de `BLOCOS`, com o texto
já resolvido.

O texto dos blocos é escrito para ser *falado*, não lido: frases curtas, sem
marcação e sem rótulo de locutor. Rótulos como "Narrador:" precisam ficar fora
do que vai para o sintetizador de voz.
"""
from dataclasses import dataclass

PODCAST = "O Segundo Par de Mãos"
SUBTITULO = "o podcast de quem programa acompanhado"
APRESENTADOR = "Filipe"

EPISODIO = 1
TITULO = "O que muda quando a IA executa"
DESCRICAO = (
    "A diferença entre uma inteligência artificial que sugere e uma que executa — "
    "e o que muda no dia a dia de quem programa quando ela ganha acesso ao repositório."
)

VOZ = "pt-BR-AntonioNeural"
TAGS = ["IA agêntica", "produtividade", "carreira"]

# Pausa inserida depois de cada bloco, em segundos. Dá o respiro que a fala
# sintetizada não produz sozinha quando o texto é enviado de uma vez só.
PAUSA_ENTRE_BLOCOS = 0.75


@dataclass(frozen=True)
class Bloco:
    """Um bloco do roteiro: a variável do prompt e o texto que a substituiu."""

    variavel: str
    rotulo: str
    texto: str


BLOCOS = [
    Bloco(
        "[ABERTURA]",
        "Abertura",
        "Olá! Seja muito bem-vindo ao Segundo Par de Mãos, o podcast de quem "
        "programa acompanhado. Eu sou o Filipe, e esse é o lugar onde a gente "
        "conversa sobre uma mudança silenciosa no jeito de escrever código: a "
        "inteligência artificial saiu da janela de chat e entrou no repositório. "
        "No episódio de hoje, eu quero te mostrar o que muda quando a "
        "inteligência artificial para de sugerir e começa a executar. Prepara o "
        "café, porque em menos de cinco minutos você vai olhar para o seu editor "
        "de um jeito diferente.",
    ),
    Bloco(
        "[BLOCO_CONCEITO]",
        "Conceito: sugerir e executar",
        "Vamos começar pelo começo. Durante uns bons anos, a inteligência "
        "artificial no desenvolvimento de software fez uma coisa só: completar. "
        "Você digitava três linhas, ela sugeria a quarta. Era útil, mas era "
        "passivo. Você continuava sendo as duas mãos que abrem o arquivo, rodam o "
        "teste, leem o erro e voltam para o editor. "
        "O que mudou não foi o modelo ficar mais inteligente. O que mudou foi o "
        "acesso. Quando a ferramenta ganha permissão para ler o repositório "
        "inteiro, abrir arquivos, executar comandos no terminal e olhar a saída, "
        "ela deixa de ser um autocompletar e vira um agente. A diferença é ela "
        "ter mãos. "
        "E isso muda a unidade de trabalho. Antes, você pedia uma função. Agora, "
        "você descreve um resultado: faça esse teste passar. A ferramenta roda o "
        "teste, lê a falha, edita o arquivo, roda de novo. E volta para você com "
        "o ciclo já fechado.",
    ),
    Bloco(
        "[BLOCO_CURIOSIDADE]",
        "Curiosidade da semana",
        "E já que a gente falou em ciclo fechado, aqui vai a curiosidade de hoje. "
        "A maior parte do tempo de um agente de código não é gasta escrevendo "
        "código. É gasta lendo. Abrir arquivo, procurar um padrão, seguir uma "
        "referência, voltar. Escrever é a minoria das ações. "
        "E isso diz muito sobre a nossa profissão. Programar sempre foi mais "
        "sobre entender o que já existe do que sobre digitar coisa nova. A "
        "inteligência artificial só tornou essa proporção visível — e ela é "
        "exatamente a mesma para gente de carne e osso.",
    ),
    Bloco(
        "[BLOCO_PRATICO]",
        "Na prática: o primeiro dia no projeto",
        "Deixa eu te dar o caso mais útil de todos: o primeiro dia num projeto "
        "que você nunca viu. "
        "Você clona um repositório com oitocentos arquivos. O documento de "
        "leitura está desatualizado, quem escreveu aquilo saiu da empresa e a "
        "documentação mora na cabeça de alguém. Antes, isso era uma semana de "
        "leitura até você ter coragem de mudar uma linha. "
        "Com um agente, a pergunta muda de forma. Você não pergunta como funciona "
        "a autenticação nesse projeto. Você pede: encontre onde a autenticação é "
        "validada, mostre o caminho da requisição até o banco e me diga onde "
        "ficam os testes disso. A ferramenta lê, segue as referências e devolve o "
        "mapa com o caminho de cada arquivo. "
        "Repara que você não pulou o entendimento. Você só chegou nele em uma "
        "tarde, em vez de uma semana.",
    ),
    Bloco(
        "[BLOCO_ALERTA]",
        "O que não delegar",
        "Agora o aviso — e esse é o bloco que eu não deixo de fora nenhuma "
        "semana. "
        "Nada disso tira de você a responsabilidade pelo que entra no "
        "repositório. O agente executa, mas quem assina o commit é você. E tem um "
        "detalhe cruel aqui: código gerado por inteligência artificial parece "
        "pronto. Ele tem indentação limpa, nome de variável coerente, comentário "
        "no lugar certo. Isso baixa a sua guarda exatamente no momento em que ela "
        "deveria subir. "
        "Então a regra é simples: se você não consegue explicar por que aquela "
        "linha existe, ela ainda não está pronta para ir. Revisar continua sendo "
        "trabalho seu. A ferramenta é aceleradora, não substituta.",
    ),
    Bloco(
        "[ENCERRAMENTO]",
        "Encerramento",
        "E é isso por hoje. Se você levar uma frase só desse episódio, que seja "
        "essa: a inteligência artificial não substituiu o desenvolvedor. Ela deu "
        "um segundo par de mãos para ele — e as duas primeiras continuam sendo as "
        "que decidem. "
        "Eu sou o Filipe, e esse foi O Segundo Par de Mãos. A gente se encontra "
        "no próximo commit.",
    ),
]


def texto_narrado() -> str:
    """O roteiro inteiro como texto corrido, do jeito que vai para a narração."""
    return "\n\n".join(bloco.texto for bloco in BLOCOS)


def palavras() -> int:
    return len(texto_narrado().split())


def duracao_estimada_min() -> float:
    """Estimativa a 150 palavras por minuto, ritmo de fala narrada em português."""
    return palavras() / 150.0
