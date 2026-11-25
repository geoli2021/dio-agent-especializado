# Fundamentos de Segurança da Informação

## Vulnerabilidade, ameaça e risco

- **Vulnerabilidade:** uma fraqueza no sistema (código, configuração, processo)
  que pode ser explorada. Ex.: SQL Injection por concatenação de entrada.
- **Ameaça:** o agente ou evento que pode explorar a vulnerabilidade. Ex.: um
  atacante externo, um insider, um malware.
- **Risco:** a combinação de probabilidade e impacto. Um risco alto ocorre quando
  uma vulnerabilidade crítica é fácil de explorar e afeta dados sensíveis.

## Tríade CIA (Confidencialidade, Integridade, Disponibilidade)

| Princípio | Pergunta central | Exemplo de violação |
|---|---|---|
| **Confidencialidade** | Quem não deveria ver, viu? | Vazamento de credenciais |
| **Integridade** | Alguém alterou o que não deveria? | Modificação de registros |
| **Disponibilidade** | O serviço está acessível quando necessário? | DDoS, ransomware |

Uma falha de SQL Injection pode violar confidencialidade (leitura de dados),
integridade (alteração de registros) e, em alguns casos, disponibilidade
(exclusão de tabelas).

## Boas práticas defensivas

1. **Validação e parametrização:** nunca concatene entrada do usuário em
   consultas SQL. Use consultas parametrizadas.
2. **Princípio do menor privilégio:** o banco da aplicação não deve ter permissões
   de administrador.
3. **Defesa em profundidade:** combine validação, parametrização, WAF e
   monitoramento.
4. **Não confie na entrada:** valide formato, tamanho e tipo no servidor.
5. **Mensagens de erro genéricas:** não exponha detalhes internos ao usuário.
6. **Atualização e patches:** mantenha dependências e sistemas atualizados.
7. **Registro e monitoramento:** registre tentativas de acesso anômalas e
   monitore padrões suspeitos.
8. **Contexto antes da ação:** em segurança, a mesma falha pode ter pesos
   diferentes dependendo da exposição e dos dados tratados.
