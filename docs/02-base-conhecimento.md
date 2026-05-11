# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores e identificar padrões de atendimento. |
| `perfil_usuario.json` | JSON | Personalizar limites, padrões, metas e alertas do usuário. |
| `compras_interesse.json` | JSON | Detectar compras de interesse e alertar para valores fora do esperado. |
| `transacoes.csv` | CSV | Analisar histórico de receitas e despesas e acompanhar o orçamento. |
| `regras_agente.json` | JSON | Definir critérios de classificação, severidade, mensagens padrão e regras operacionais. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Adaptei os arquivos com mais registros e para que refletissem minha necessidade de um agente para controle de receitas e despesas do usuário.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt

```python
import pandas as pd
import json

# ========== CARREGAR DADOS ========
historico = pd.read_csv('./data/historico_atendimento.csv')
transacoes = pd.read_csv('./data/transacoes.csv')
compras = json.load(open('./data/compras_interesse.json'))
perfil = json.load(open('./data/perfil_usuario.json'))
compras = json.load(open('./data/compras_interesse.json'))

```

### Como os dados são usados no prompt?
> Os dados são incorporados ao contexto conforme a necessidade da análise, com foco em classificação, alerta e acompanhamento do orçamento.

- Perfil do cliente: nome, objetivo, limites, despesas, receitas e metas.
- Histórico de atendimentos: interações anteriores, resoluções e tipos de solicitação.
- Compras de interesse: itens monitorados com limites e severidade.
- Transações: lançamentos já realizados, valores, categorias e tipos.
- Regras do agente: prioridades de classificação, limiares de alerta e mensagens padrão.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Compras de interesse:

[
  {
    "id": "compra_tv",
    "nome": "TV",
    "categoria_financeira": "despesa_discricionaria",
    "subcategoria": "eletrodomesticos",
    "limite_esperado": 2500.00,
    "limite_alerta": 3000.00,
    "limite_critico": 3500.00,
    "severidade": "alta",
    "alerta": "Compra acima do padrão para TV."
  }
]
...

Histórico de atendimentos
evt_0001,2026-01-01,chat,receita,salario,"Salário recebido no valor de R\$ 4.800",4800.00,entrada,dentro_padrao,sim,"Valor abaixo do esperado, mas dentro do mínimo aceitável."
evt_0002,2026-01-02,email,despesa,aluguel,"Pagamento de aluguel no valor de R\$ 1.300",1300.00,saida,dentro_padrao,sim,"Dentro do teto aceito."
...

Perfil Usuário
{
  "nome": "João Silva",
  "perfil_financeiro": "controle_orcamentario",
  "objetivo_principal": "Manter receitas e despesas dentro do padrão mensal",
  "limites_gerais": {
    "receitas_totais_esperadas": 5800.00,
    "despesas_totais_maximas": 4800.00
  }
}
...

Transações
2026-01-02,Salário,receita,5000.00,entrada
2026-01-05,Freelance,receita,850.00,entrada
2026-01-08,Reembolso,receita,220.00,entrada

```
