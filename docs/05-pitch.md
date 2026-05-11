# Pitch (3 minutos)

### 1. O Problema (30 seg)
> Qual dor do cliente você resolve?

Muitas pessoas têm dificuldade para controlar receitas e despesas no dia a dia. Elas esquecem lançamentos, não percebem quando um gasto está fora do padrão e acabam sem uma visão clara do próprio orçamento. Isso torna o controle financeiro manual, lento e sujeito a erro.

### 2. A Solução (1 min)
> Como seu agente resolve esse problema?

Nosso agente de IA, chamado Cris, ajuda o usuário pelo WhatsApp a registrar lançamentos financeiros de forma simples. Ele identifica se a mensagem é receita, despesa ou dúvida, classifica a categoria, compara com o histórico e com os limites definidos no perfil do usuário, e avisa quando algo foge do padrão.

A solução foi pensada para rodar localmente com Ollama, usando um modelo leve para interpretação das mensagens, e com gpt-oss como base aberta para adaptação e testes da lógica do agente. Os dados de apoio, como perfil do usuário, compras de interesse, histórico e regras, são usados para montar o contexto da resposta com mais precisão.

### 3. Demonstração (1 min)
> Mostre o agente funcionando (pode ser gravação de tela)

Na demonstração, eu mostro o usuário enviando mensagens como:

- Comprei um notebook por R\$ 4.200
- Recebi meu salário de R\$ 5.000
- Paguei a conta

O agente responde com:

- classificação do lançamento;
- confirmação do registro;
- alerta quando o valor está acima do esperado;
- pedido de esclarecimento quando a informação está incompleta.

Também mostro que os dados ficam persistidos localmente, por exemplo em SQLite, permitindo consultar histórico e manter o contexto das interações.

### 4. Diferencial e Impacto (30 seg)
> Por que essa solução é inovadora e qual é o impacto dela na sociedade?

O diferencial é unir IA local, baixo custo e controle financeiro pessoal em uma solução simples de usar. Como o agente roda com Ollama e aproveita uma base organizada de conhecimento, ele pode funcionar sem depender totalmente de serviços pagos em nuvem.

O impacto é facilitar educação financeira, reduzir esquecimentos e ajudar o usuário a tomar decisões melhores sobre gastos e metas. Isso torna o controle financeiro mais acessível e prático para o dia a dia.

---

## Checklist do Pitch

- [X] Duração máxima de 3 minutos
- [X] Problema claramente definido
- [X] Solução demonstrada na prática
- [X] Diferencial explicado

---
