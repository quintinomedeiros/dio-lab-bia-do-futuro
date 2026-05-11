# 🤖 Agente Financeiro Inteligente com IA Generativa

## Contexto

Assistentes virtuais no setor financeiro estão evoluindo de simples chatbots reativos para **agentes inteligentes e proativos**.  
Neste projeto, o objetivo é criar um agente que ajuda o usuário a **registrar receitas e despesas, identificar gastos fora do padrão e manter o controle do orçamento**.

O agente foi pensado para:
- **Antecipar necessidades**, em vez de apenas responder perguntas;
- **Personalizar respostas** com base no perfil financeiro do usuário;
- **Cocriar soluções** de forma consultiva;
- **Garantir segurança e confiabilidade**, evitando alucinações.

---

## O que você deve entregar

### 1. Documentação do Agente

Defina **o que** seu agente faz e **como** ele funciona:

- **Caso de Uso:** qual problema financeiro ele resolve?
- **Persona e Tom de Voz:** como o agente se comunica?
- **Arquitetura:** fluxo de dados e integração com a base de conhecimento
- **Segurança:** como evitar alucinações e garantir respostas confiáveis?

---

### 2. Base de Conhecimento

Utilize os dados mockados disponíveis na pasta [`data/`](./data/) para alimentar seu agente:

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `transacoes.csv` | CSV | Histórico de transações do cliente |
| `historico_atendimento.csv` | CSV | Histórico de atendimentos anteriores |
| `perfil_usuario.json` | JSON | Perfil e preferências do cliente |
| `compras_interesse.json` | JSON | Compras monitoradas com limites e alertas |
| `regras_agente.json` | JSON | Regras operacionais do agente |

Você pode adaptar ou expandir esses dados conforme seu caso de uso.

---

### 3. Prompts do Agente

Documente os prompts que definem o comportamento do seu agente:

- **System Prompt:** instruções gerais de comportamento e restrições
- **Exemplos de Interação:** cenários de uso com entrada e saída esperada
- **Tratamento de Edge Cases:** como o agente lida com situações limite

---

### 4. Aplicação Funcional

Desenvolva um **protótipo funcional** do seu agente:

- chatbot interativo;
- integração com LLM local ou via API;
- conexão com a base de conhecimento;
- persistência local das interações.

---

### 5. Avaliação e Métricas

Descreva como você avalia a qualidade do seu agente:

**Métricas sugeridas:**
- assertividade das respostas;
- taxa de respostas seguras;
- coerência com o perfil do cliente.

---

### 6. Pitch

Grave um **pitch de 3 minutos** apresentando:

- qual problema o agente resolve;
- como ele funciona na prática;
- por que a solução é útil e inovadora.

---

## Ferramentas sugeridas

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | Ollama, GPT-OSS |
| **Desenvolvimento** | Streamlit, Gradio |
| **Persistência** | SQLite |
| **Orquestração** | LangChain, LangFlow, CrewAI |
| **Diagramas** | Mermaid, Draw.io, Excalidraw |

---

## Estrutura do repositório

```text
📁 lab-agente-financeiro/
├── README.md
├── data/
│   ├── historico_atendimento.csv
│   ├── perfil_usuario.json
│   ├── compras_interesse.json
│   ├── regras_agente.json
│   └── transacoes.csv
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
├── src/
│   └── app.py
├── assets/
└── examples/