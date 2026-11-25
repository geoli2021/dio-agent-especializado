# DIO Agent — Especialização em Análise de Vulnerabilidades

![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Tipo](https://img.shields.io/badge/tipo-agente%20Markdown-blue)
![Foco](https://img.shields.io/badge/foco-AppSec-orange)

> Evolução do [DIO Agent](https://github.com/digitalinnovationone/dio-agent) com
> uma especialização em **análise de segurança defensiva (AppSec)**. Nenhum
> modelo foi treinado: o agente aprende apenas pelos arquivos Markdown.

---

## 🎯 A especialização e por quê

Evoluí o DIO Agent para atuar como **analista de segurança defensivo**. O objetivo
é que o agente, antes de responder, **entenda o contexto** (ambiente, exposição,
dados, stack) e conduza uma análise estruturada de **impacto, probabilidade e
severidade** — algo que um chat genérico raramente faz.

A especialização foi construída **apenas com arquivos Markdown**:

- uma **skill nova** (`vulnerability-analysis`);
- um **arquivo de conhecimento** (`security-basics.md`);
- um **trecho na persona** (`agent/persona.md`);
- uma **linha na tabela de skills** do `AGENTS.md`.

---

## 📁 Arquivos criados ou alterados

| Arquivo | Tipo | O que faz |
|---|---|---|
| `skills/vulnerability-analysis/SKILL.md` | **Novo** | Roteiro que o agente segue na análise |
| `skills/vulnerability-analysis/README.md` | **Novo** | Explicação da skill para pessoas |
| `agent/knowledge/security-basics.md` | **Novo** | Fundamentos: vulnerabilidade, ameaça, risco, tríade CIA, boas práticas |
| `agent/persona.md` | **Alterado** | Trecho que ativa o modo “analista de segurança” |
| `AGENTS.md` | **Alterado** | Linha na tabela de skills para rotear a nova intenção |
| `lab/app.py` | **Novo** | Aplicação de login com SQL Injection intencional (laboratório) |
| `lab/app_fixed.py` | **Novo** | Versão com consulta parametrizada, usada na validação |

---

## ▶️ Como rodar o agente no harness

1. Clone este repositório:

   ```bash
   git clone https://github.com/<seu-usuario>/dio-agent-especializado.git
   cd dio-agent-especializado
   ```

2. Abra **a pasta que contém o `AGENTS.md`** no harness (Hermes, Antigravity, etc.).
   - ⚠️ O harness precisa ser aberto **na pasta do projeto**. Aberto em outro lugar,
     ele não encontra os arquivos.

3. O harness lê o `AGENTS.md` automaticamente e passa a oferecer a skill.

4. Peça uma análise de segurança, por exemplo:

   > “Analise o arquivo `lab/app.py` e me diga o risco.”

5. Observe o agente **perguntar o contexto** antes de concluir e entregar a
   análise no formato estruturado.

### Testar a aplicação de laboratório (opcional)

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install flask

python lab/app.py
# Acesse http://127.0.0.1:5000/login (POST)
```

---

## 🧪 Melhoria escolhida e evidências

- **Melhoria escolhida:** skill de análise de vulnerabilidades com formato
  estruturado (contexto → impacto → probabilidade → severidade → correção →
  validação).
- **Teste principal:** `lab/app.py` com SQL Injection por concatenação.
- **Antes da skill:** resposta direta, sem perguntar contexto.
- **Depois da skill:** o agente pergunta o contexto e entrega a análise
  estruturada, citando CWE-89 e a técnica do MITRE ATT&CK (T1190 quando o serviço
  é público).

### Prints

- `images/analise_antes.png` — resposta sem a skill.
- `images/analise_depois.png` — resposta com a skill.
- `images/perguntas_contexto.png` — agente perguntando antes de agir.
- `images/correcao.png` — consulta parametrizada sugerida.
- `images/chat_generico.png` — mesma pergunta em chat genérico, para comparação.

---

## 📚 O que aprendi

- Uma skill é um **roteiro em Markdown**, não um programa.
- A `description` do frontmatter é o **gatilho de roteamento**: se ela não deixar
  claro *quando* usar, o agente pode não carregar a skill.
- **Perguntar o contexto antes de agir** é o que mais diferencia um agente
  especializado de um chat genérico.
- A **tabela do `AGENTS.md`** é essencial para o agente saber que a skill existe.
- O harness precisa ser aberto **na pasta do projeto** — caso contrário, não lê
  os arquivos.

---

## ⚠️ Aviso

Todos os testes usaram apenas código e servidores de **laboratório**, executados
em `127.0.0.1`. Nenhum exploit funcional foi executado contra sistemas de
terceiros. A aplicação `lab/app.py` é **intencionalmente vulnerável** e **não
deve** ser exposta na internet.

---

## 📖 Referências

- [DIO Agent (repositório base)](https://github.com/digitalinnovationone/dio-agent)
- [CWE-89: SQL Injection](https://cwe.mitre.org/data/definitions/89.html)
- [MITRE ATT&CK — T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Tríade CIA](https://en.wikipedia.org/wiki/Confidentiality,_integrity,_and_availability)
