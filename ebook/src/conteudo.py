# -*- coding: utf-8 -*-
"""Conteúdo do e-book "O Dev Aumentado".

Só dados. Para mudar um texto do e-book, mexe-se aqui e roda-se o gerador —
nenhum código de desenho precisa ser tocado.

Estrutura de uma página de conteúdo:
    {
      "titulo":     str,
      "paragrafos": [str, ...]        # "- " no início vira bullet
      "destaque":   str | None,       # citação em bloco
      "codigo":     {"arquivo": str, "linhas": [[(texto, token), ...], ...]}
      "fecho":      [str, ...]        # parágrafos depois do bloco de código
    }
"""

TITULO = "O DEV AUMENTADO"
SUBTITULO = "Claude Code na prática: da ideia ao commit"
CHAMADA = "Como a IA agêntica encurta o caminho entre a ideia e o código funcional"
AUTOR = "Filipe Zanin"
RODAPE = "O Dev Aumentado  ·  Filipe Zanin"

FICHA = [
    "Este e-book foi produzido como desafio de projeto da DIO — Formação "
    "ChatGPT for Devs.",
    "O texto foi acelerado por IA e revisado, editado e diagramado por um "
    "humano. A diagramação é gerada por código: todas as páginas que você "
    "está lendo saem de um script Python versionado no repositório.",
]

INTRODUCAO = {
    "titulo": "Antes de começar",
    "paragrafos": [
        "Existe uma diferença grande entre uma IA que sugere e uma IA que "
        "executa. A primeira te devolve um trecho de código para você copiar. "
        "A segunda abre o seu repositório, lê os arquivos, entende as "
        "convenções do projeto, edita o que precisa ser editado e roda os "
        "testes para conferir se não quebrou nada.",

        "Esse segundo grupo tem nome: ferramentas agênticas. E o Claude Code, "
        "da Anthropic, é uma delas. Este e-book é sobre o que muda no dia a "
        "dia de quem programa quando a IA sai da aba do navegador e entra no "
        "terminal, no editor e no fluxo de trabalho.",

        "Não é um manual de referência — a documentação oficial faz isso "
        "melhor. É um guia de postura: onde essas ferramentas ganham tempo de "
        "verdade, onde elas atrapalham, e o que continua sendo, "
        "inegociavelmente, trabalho seu.",
    ],
    "destaque": "O ganho não está em terceirizar o pensamento. Está em "
                "encurtar a distância entre a ideia e o código funcional.",
    "fecho": [
        "Cada capítulo traz uma situação concreta, o que você pediria e o que "
        "acontece na prática. Leia na ordem ou pule direto para o problema que "
        "você tem hoje.",
    ],
}

CAPITULOS = [
    # -- 1 ------------------------------------------------------------------
    {
        "numero": 1,
        "titulo": "Da sugestão à ação",
        "resumo": "O que muda quando a IA tem mãos",
        "paginas": [
            {
                "titulo": "A IA saiu da aba do navegador",
                "paragrafos": [
                    "Por anos o fluxo foi sempre o mesmo: descrever o problema "
                    "num chat, receber um bloco de código, voltar para o "
                    "editor, colar, adaptar os nomes das variáveis, descobrir "
                    "que faltava um import. Funcionava, mas o custo de "
                    "tradução entre a resposta genérica e o seu projeto real "
                    "era todo seu.",

                    "Uma ferramenta agêntica inverte isso. Ela opera dentro do "
                    "repositório, então não precisa adivinhar como o seu "
                    "projeto é organizado — ela lê. As três capacidades que "
                    "fazem a diferença:",

                    "- Ler arquivos e navegar pela estrutura do projeto",
                    "- Editar arquivos existentes, não só propor trechos",
                    "- Executar comandos e reagir ao resultado deles",
                ],
                "codigo": {
                    "arquivo": "terminal",
                    "linhas": [
                        [("$ ", "cmd"), ("claude", "fg")],
                        [("> ", "prompt"),
                         ("adicione paginação no endpoint de listagem", "txt")],
                        [],
                        [("● ", "ok"), ("Read   ", "dim"),
                         ("src/routes/produtos.js", "path")],
                        [("● ", "ok"), ("Edit   ", "dim"),
                         ("src/controllers/produtos.js", "path")],
                        [("● ", "ok"), ("Bash   ", "dim"), ("npm test", "fg"),
                         ("   18 passed", "ok")],
                    ],
                },
                "fecho": [
                    "A diferença não é de qualidade do código gerado. É de "
                    "onde o trabalho acontece.",
                ],
            },
        ],
    },

    # -- 2 ------------------------------------------------------------------
    {
        "numero": 2,
        "titulo": "Onboarding",
        "resumo": "Entendendo uma base que você nunca viu",
        "paginas": [
            {
                "titulo": "O custo real de entrar num projeto",
                "paragrafos": [
                    "Entrar num repositório desconhecido é, de longe, uma das "
                    "partes mais lentas do trabalho. Não porque o código seja "
                    "difícil, mas porque o conhecimento está espalhado: um "
                    "pouco no README desatualizado, um pouco na cabeça de quem "
                    "escreveu, um pouco só no histórico do Git.",

                    "Aqui a IA agêntica rende muito, porque a tarefa é "
                    "essencialmente de leitura em volume — exatamente o que "
                    "uma pessoa faz devagar e uma máquina faz rápido.",
                ],
                "destaque": "Peça o mapa antes de pedir a mudança.",
                "fecho": [
                    "Perguntas que rendem no primeiro dia:",
                    "- Qual é o ponto de entrada da aplicação?",
                    "- Como a autenticação funciona e onde ela é aplicada?",
                    "- Quais são os 5 arquivos que mais mudam neste repo?",
                ],
            },
            {
                "titulo": "Do mapa ao primeiro commit",
                "paragrafos": [
                    "Depois do panorama, o próximo passo é entender uma fatia "
                    "específica. O truque é pedir explicação ancorada em "
                    "arquivo e linha, não explicação genérica — assim você "
                    "consegue conferir.",
                ],
                "codigo": {
                    "arquivo": "onboarding",
                    "linhas": [
                        [("> ", "prompt"),
                         ("explique o fluxo de login e cite", "txt")],
                        [("  ", "txt"), ("os arquivos envolvidos", "txt")],
                        [],
                        [("● ", "ok"), ("Grep   ", "dim"),
                         ('"session" (14 arquivos)', "path")],
                        [("● ", "ok"), ("Read   ", "dim"),
                         ("src/auth/middleware.js", "path")],
                        [("● ", "ok"), ("Read   ", "dim"),
                         ("src/auth/tokens.js", "path")],
                        [],
                        [("O login passa por 3 camadas:", "txt")],
                        [("middleware → tokens → sessão.", "txt")],
                    ],
                },
                "fecho": [
                    "Você ainda precisa abrir os arquivos citados e conferir. "
                    "A diferença é que agora você sabe quais abrir.",
                ],
            },
        ],
    },

    # -- 3 ------------------------------------------------------------------
    {
        "numero": 3,
        "titulo": "Ponta a ponta",
        "resumo": "Funcionalidade completa, com testes",
        "paginas": [
            {
                "titulo": "Descreva o comportamento, não a implementação",
                "paragrafos": [
                    "O erro mais comum é pedir código como se estivesse "
                    "ditando: 'crie uma função que recebe X e retorna Y'. "
                    "Isso desperdiça a parte mais útil da ferramenta, que é "
                    "ela decidir a implementação a partir das convenções que "
                    "já existem no seu projeto.",

                    "Descreva o comportamento esperado e os critérios de "
                    "aceite. Deixe a estrutura por conta de quem já leu o "
                    "repositório inteiro.",
                ],
                "destaque": "Um pedido bom descreve o resultado. Um pedido "
                            "ruim descreve os passos.",
                "fecho": [
                    "E sempre peça os testes junto. Não por disciplina: "
                    "porque um teste que passa é a única evidência de que a "
                    "coisa funciona.",
                ],
            },
            {
                "titulo": "O ciclo que vale a pena",
                "paragrafos": [
                    "Na prática o fluxo vira um laço curto: você descreve, ela "
                    "implementa e roda, você revisa o diff. Se o teste falha, "
                    "ela mesma vê a saída e corrige antes de te devolver.",
                ],
                "codigo": {
                    "arquivo": "feature",
                    "linhas": [
                        [("> ", "prompt"),
                         ("usuário só vê os próprios pedidos.", "txt")],
                        [("  ", "txt"), ("cubra com testes.", "txt")],
                        [],
                        [("● ", "ok"), ("Write  ", "dim"),
                         ("tests/pedidos.test.js", "path")],
                        [("● ", "ok"), ("Edit   ", "dim"),
                         ("src/controllers/pedidos.js", "path")],
                        [("● ", "ok"), ("Bash   ", "dim"), ("npm test", "fg")],
                        [("  ✗ ", "warn"), ("1 failing", "warn")],
                        [("● ", "ok"), ("Edit   ", "dim"),
                         ("src/controllers/pedidos.js", "path")],
                        [("● ", "ok"), ("Bash   ", "dim"), ("npm test", "fg"),
                         ("   6 passed", "ok")],
                    ],
                },
                "fecho": [
                    "Repare no passo do meio: o teste falhou e foi corrigido "
                    "sem você entrar no circuito. É aí que o tempo aparece.",
                ],
            },
        ],
    },

    # -- 4 ------------------------------------------------------------------
    {
        "numero": 4,
        "titulo": "Debugging",
        "resumo": "Da mensagem de erro à causa raiz",
        "paginas": [
            {
                "titulo": "Pare de pesquisar a mensagem de erro",
                "paragrafos": [
                    "Colar um stack trace no buscador te dá o caso genérico. "
                    "O seu bug quase nunca é o caso genérico — ele é a "
                    "interação entre a biblioteca e alguma decisão específica "
                    "do seu projeto.",

                    "Uma ferramenta que lê o seu código investiga o seu caso. "
                    "Ela segue a pilha até o arquivo real, olha o que está em "
                    "volta e propõe uma hipótese verificável.",
                ],
                "destaque": "A pergunta certa não é 'o que significa esse "
                            "erro'. É 'por que ele acontece aqui'.",
                "fecho": [
                    "Quando o erro não reproduz sempre, dê o contexto que só "
                    "você tem: o que mudou, desde quando, em qual ambiente.",
                ],
            },
            {
                "titulo": "Investigar antes de corrigir",
                "paragrafos": [
                    "Vale um hábito: peça o diagnóstico antes da correção. "
                    "Uma correção proposta sem explicação é uma aposta; com "
                    "explicação, você consegue julgar se faz sentido.",
                ],
                "codigo": {
                    "arquivo": "debug",
                    "linhas": [
                        [("> ", "prompt"),
                         ("TypeError em produção, só às vezes.", "txt")],
                        [("  ", "txt"),
                         ("investigue antes de corrigir.", "txt")],
                        [],
                        [("● ", "ok"), ("Read   ", "dim"),
                         ("src/cache/store.js", "path")],
                        [("● ", "ok"), ("Grep   ", "dim"),
                         ('"invalidate"', "path")],
                        [],
                        [("Causa provável: leitura do cache", "txt")],
                        [("antes da escrita terminar.", "txt")],
                        [("Corrijo aguardando a promise?", "warn")],
                    ],
                },
                "fecho": [
                    "Note o ponto de interrogação no fim. Ela para e pergunta "
                    "— e é exatamente esse o comportamento que você quer.",
                ],
            },
        ],
    },

    # -- 5 ------------------------------------------------------------------
    {
        "numero": 5,
        "titulo": "Refatoração",
        "resumo": "Mudanças mecânicas, em escala",
        "paginas": [
            {
                "titulo": "O trabalho chato é o mais fácil de delegar",
                "paragrafos": [
                    "Renomear um conceito em 40 arquivos, migrar de uma "
                    "biblioteca para outra, padronizar um jeito de tratar "
                    "erro: tarefas que não são difíceis, são só longas. "
                    "Ninguém aprende nada fazendo a trigésima substituição.",

                    "É o cenário ideal para delegar, com duas condições: que "
                    "exista teste cobrindo o que está sendo mexido, e que "
                    "você revise o diff em vez de confiar no relatório.",

                    "- Faça em lotes pequenos, não no repositório inteiro",
                    "- Commit separado da mudança de comportamento",
                    "- Se não há teste, escreva o teste primeiro",
                ],
                "destaque": "Refatoração sem teste não é refatoração. É "
                            "reescrita com esperança.",
                "fecho": [
                    "A regra prática: se você não consegue revisar o diff, o "
                    "lote está grande demais.",
                ],
            },
        ],
    },

    # -- 6 ------------------------------------------------------------------
    {
        "numero": 6,
        "titulo": "Memória de projeto",
        "resumo": "Ensinando as regras do seu time",
        "paginas": [
            {
                "titulo": "Pare de repetir as mesmas instruções",
                "paragrafos": [
                    "Se você corrige a mesma coisa toda sessão — 'use aspas "
                    "simples', 'os testes rodam com pnpm', 'não mexe na pasta "
                    "de migrations' — o problema não é a ferramenta. É que "
                    "essa informação não está escrita em lugar nenhum.",

                    "A solução é um arquivo de contexto no próprio "
                    "repositório, lido automaticamente antes de qualquer "
                    "ação. Funciona como o manual de onboarding que o time "
                    "nunca escreveu, com uma vantagem: ele é versionado junto "
                    "com o código, então nunca desatualiza em silêncio.",
                ],
                "destaque": "O que você explica duas vezes deveria estar "
                            "escrito uma vez.",
                "fecho": [
                    "Comece pequeno. Três linhas úteis valem mais que duas "
                    "páginas genéricas.",
                ],
            },
            {
                "titulo": "O que vale a pena registrar",
                "paragrafos": [
                    "Registre o que não é dedutível do código: comandos, "
                    "convenções e proibições. Não registre o que a ferramenta "
                    "descobre sozinha lendo os arquivos.",
                ],
                "codigo": {
                    "arquivo": "CLAUDE.md",
                    "linhas": [
                        [("## Comandos", "kw")],
                        [("- testes: ", "txt"), ("pnpm test", "ok")],
                        [("- lint:   ", "txt"), ("pnpm lint --fix", "ok")],
                        [],
                        [("## Convenções", "kw")],
                        [("- Migrations são geradas, nunca", "txt")],
                        [("  editadas à mão.", "txt")],
                        [("- Toda rota nova precisa de teste", "txt")],
                        [("  de integração.", "txt")],
                    ],
                },
                "fecho": [
                    "Esse arquivo tende a virar o documento mais honesto do "
                    "projeto — porque é o único que alguém percebe quando "
                    "está errado.",
                ],
            },
        ],
    },

    # -- 7 ------------------------------------------------------------------
    {
        "numero": 7,
        "titulo": "Acelerador",
        "resumo": "Não substituto",
        "paginas": [
            {
                "titulo": "O que continua sendo trabalho seu",
                "paragrafos": [
                    "Uma ferramenta que edita arquivos, roda comandos e cria "
                    "commits tem poder de causar estrago. Isso não é motivo "
                    "para não usar — é motivo para usar com as mesmas "
                    "cautelas que você teria com qualquer pessoa nova no "
                    "time.",

                    "- Revise o diff. Sempre. Não o resumo, o diff",
                    "- Cuidado redobrado com credenciais e CI/CD",
                    "- Decisão de arquitetura não se delega",
                    "- Se você não entende o código, ele não está pronto",

                    "O julgamento técnico continua inteiro do seu lado. O que "
                    "muda é quanto do seu tempo sobra para exercê-lo, em vez "
                    "de gastá-lo em tarefa mecânica.",
                ],
                "destaque": "Use IA como acelerador, nunca como dependência.",
                "fecho": [
                    "Quem sai na frente não é quem gera mais código. É quem "
                    "consegue revisar bem o código que aparece.",
                ],
            },
        ],
    },
]

AGRADECIMENTOS = {
    "titulo": "Obrigado por ler até aqui",
    "paragrafos": [
        "Este e-book nasceu de um desafio de projeto da DIO, na Formação "
        "ChatGPT for Devs, e é o segundo capítulo de uma dupla: o primeiro "
        "foi um artigo sobre o mesmo tema.",

        "Todo o processo está aberto no repositório — os prompts usados em "
        "cada etapa, o script que gera este PDF e o artigo completo. Se você "
        "quiser produzir o seu, é só clonar e trocar o conteúdo.",
    ],
    "link": "github.com/filipemzanin",
    "fecho": [
        "Se este material te ajudou, o melhor retorno possível é você "
        "publicar o seu.",
    ],
}
