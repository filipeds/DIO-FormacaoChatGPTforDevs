# Etapa 1 — Definição do tema e do público

A primeira aula é categórica: **escreva sobre algo que você já domina.** A IA entra
como aceleradora de um conhecimento que já existe, não como fonte dele.

> "Eu não vou pedir para o ChatGPT gerar um livro para mim, eu vou utilizar ele
> como uma ferramenta aceleradora para trazer alguma coisa que eu já tenho de
> conhecimento."

Por isso o tema escolhido foi o mesmo do desafio anterior deste repositório —
**Claude Code e IA agêntica na geração de código** — sobre o qual eu já tinha
escrito um artigo. O e-book não repete o artigo: aprofunda com exemplos práticos
que não cabiam no formato de post.

## Prompt

```
Vou escrever um e-book técnico sobre o uso do Claude Code (IA agêntica) como
acelerador no dia a dia de desenvolvedores.

Público-alvo: desenvolvedores de nível júnior a pleno, que já programam mas
ainda usam IA só como chat de perguntas e respostas.

Me ajude a definir o recorte:
1. Qual é a promessa central do e-book em uma frase?
2. O que ele NÃO deve tentar cobrir para não virar um manual genérico?
3. Qual é a dor concreta desse público que ele resolve?
```

## Resultado

**Promessa central:** mostrar a diferença prática entre "IA que sugere" e "IA que
executa", e o que muda no fluxo de trabalho quando ela ganha acesso ao repositório.

**Fora do escopo** (decisão deliberada):

- Documentação de flags, comandos e configuração — a documentação oficial faz melhor
- Comparativo entre ferramentas concorrentes — envelhece em semanas
- Tutorial de instalação

**Dor atendida:** o dev que já usa IA, mas gasta tempo traduzindo respostas
genéricas para o contexto do projeto real dele.

## Decisão

O e-book seria um **guia de postura**, não de referência. Isso definiu o tom de
todos os capítulos: cada um parte de uma situação concreta, não de uma feature.
