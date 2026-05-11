# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** você define perguntas e respostas esperadas;
2. **Feedback real:** pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu corretamente ao que foi perguntado? | Perguntar um lançamento e receber a classificação correta |
| **Segurança** | O agente evitou inventar informações? | Fazer uma pergunta fora de contexto e ele pedir esclarecimento ou recusar corretamente |
| **Coerência** | A resposta faz sentido com o perfil do cliente? | Alertar quando a compra estiver acima do padrão esperado |

> [!TIP]
> Peça para 3-5 pessoas testarem o agente e avaliarem cada métrica com notas de 1 a 5.  
> Se usar os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com supermercado?"
- **Resposta esperada:** valor calculado com base no `transacoes.csv`
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 2: Lançamento com valor acima do limite
- **Pergunta:** "Comprei um notebook por R\$ 4.200."
- **Resposta esperada:** agente registra e alerta que o valor está acima do limite esperado
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 3: Pergunta fora de contexto
- **Pergunta:** "Paguei a conta."
- **Resposta esperada:** agente pede mais detalhes para conseguir registrar
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** agente admite que não tem essa informação
- **Resultado:** [ ] Correto  [ ] Incorreto

---
