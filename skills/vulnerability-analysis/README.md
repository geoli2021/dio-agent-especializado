# Skill: Análise de Vulnerabilidades

## O que faz

Transforma o DIO Agent em um analista de segurança defensivo que conduz uma
análise estruturada de código, configuração ou infraestrutura, avaliando
impacto, probabilidade e severidade antes de orientar a correção.

## Quando é acionada

O agente a utiliza quando o pedido envolve:

- análise de segurança de código ou configuração;
- revisão de vulnerabilidade;
- avaliação de risco;
- correção de falha de segurança.

A `description` no `SKILL.md` é o gatilho. O agente decide sozinho se a skill é
relevante para o contexto da conversa.

## Como funciona

1. Coleta contexto (ambiente, exposição, dados, stack).
2. Identifica a vulnerabilidade.
3. Avalia impacto, probabilidade e severidade.
4. Explica a exploração em conceito, sem payload real.
5. Orienta a correção com código/configuração segura.
6. Sugere validação.

## Exemplo de uso

Peça: "Analise este `app.py` de login e me diga o risco."

O agente deve perguntar o contexto antes de concluir e, em seguida, entregar a
análise no formato estruturado.

## Limitações

- Não executa código nem testa exploits.
- Não substitui uma revisão humana em produção.
- Foi projetada para ambientes de laboratório e educação.
