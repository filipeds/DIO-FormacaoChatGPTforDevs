# Etapa 4 — A estrutura de capítulos

Antes de gerar texto, definir o esqueleto. A aula pede que o prompt já diga o
formato ("faça um texto para e-book"), o foco e que traga **um título sugestivo
por tópico** — porque cada título vira uma página de divisória de capítulo.

## Prompt

```
Faça a estrutura de capítulos de um e-book sobre o uso de IA agêntica
(Claude Code) como acelerador no dia a dia de desenvolvedores.

Contexto: o e-book é um guia de postura, não um manual de referência. Cada
capítulo deve partir de uma situação concreta do dia a dia de quem programa,
não de uma funcionalidade da ferramenta.

Requisitos:
- 7 capítulos
- Cada capítulo com um título curto (1 a 3 palavras) e um resumo de uma linha
- Explique sempre de maneira simples, texto enxuto
- O último capítulo deve tratar dos limites e riscos, não só dos ganhos
```

## Resultado (após um ajuste)

A primeira resposta veio organizada por funcionalidade — "Leitura de arquivos",
"Execução de comandos", "Integrações". Foi rejeitada por contrariar o recorte
definido na etapa 1. O pedido de correção foi:

```
Reescreva partindo da situação do desenvolvedor, não da funcionalidade da
ferramenta. O leitor deve reconhecer o problema dele no título do capítulo.
```

Estrutura final:

| # | Título | Resumo |
| --- | --- | --- |
| 01 | Da sugestão à ação | O que muda quando a IA tem mãos |
| 02 | Onboarding | Entendendo uma base que você nunca viu |
| 03 | Ponta a ponta | Funcionalidade completa, com testes |
| 04 | Debugging | Da mensagem de erro à causa raiz |
| 05 | Refatoração | Mudanças mecânicas, em escala |
| 06 | Memória de projeto | Ensinando as regras do seu time |
| 07 | Acelerador | Não substituto |

## A lição desta etapa

O primeiro output estava correto e inútil ao mesmo tempo. Um prompt bem escrito
não garante a resposta certa — garante que você consegue **explicar por que a
resposta está errada**, e é isso que torna a segunda tentativa produtiva.
