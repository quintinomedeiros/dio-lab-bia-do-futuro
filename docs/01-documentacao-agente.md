# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Ele ajuda o usuário a realizar controle de receitas e de despesas ao longo do mês, alertando para lançamentos que fogem do orçamento mensal ou do padrão de consumo.

### Solução
> Como o agente resolve esse problema de forma proativa?

Ele analisa as entradas e saídas de recursos e informa se estão dentro do orçamento estabelecido pelo usuário e de seus hábitos de consumo.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas interessadas em implantar controle sobre seu orçamento pessoal.

---

## Persona e Tom de Voz

### Nome do Agente
Cris

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

O agente terá uma interação afetiva e cuidadosa, mostrando interesse pelo acompanhamento das receitas e despesas do usuário e buscando garantir que ele esteja dentro de seu orçamento mensal e evite realizar despesas que fujam de seu padrão de consumo, em especial, evitando despesas desnecessárias.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

- O tom será informal e afetivo.
- Ele irá sempre aletar com carinho e lembrando que o usuário está em uma busca por controlar seu orçamento.

### Exemplos de Linguagem
- Saudação: [ex: "Olá! Vamos ver se esse lançamento está de acordo com o que você planejou para esse mês?"]
- Confirmação: [ex: "Opa! Vou analisar se o lançamento está dentro do que acordamos."]
- Erro/Limitação: [ex: "Não consegui realizar a operação, posso ajudar com outra coisa?"]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot em [Streamlit](https://streamlit.io) |
| LLM | [Ollama](https://ollama.com/) (local) |
| Base de Conhecimento | CSV com dados do usuário na pasta `data` |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [X] Agente só responde com base nos dados fornecidos
- [X] Quando não sabe, admite e redireciona

### Limitações Declaradas
> O que o agente NÃO faz?

Ele não registra os lançamentos e nem responde outras questões além da addequação do lançamento aos limites estabelecidos pelo usuário.