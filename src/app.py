from grpc import stream_stream_rpc_method_handler
import pandas as pd
import json
import requests
import streamlit as st

# ========== CONFIGURAÇÕES ==========
OLLAMA_URL = 'http://localhost:11434/api/v1/generate'
MODELO = 'gpt-oss'

# ========== CARREGAR DADOS ========
historico = pd.read_csv('./data/historico_atendimento.csv')
transacoes = pd.read_csv('./data/transacoes.csv')
compras = json.load(open('./data/compras_interesse.json'))
perfil = json.load(open('./data/perfil_usuario.json'))
compras = json.load(open('./data/compras_interesse.json'))

# ========== MONTAR CONTEXTO ========
contexto = f"""
CLIENTE: 
{perfil['nome']}, {perfil['IDADE']} anos, {perfil['profissao']}

PERFIL DE FINANCEIRO: {perfil['perfil_financeiro']}

OBJETIVO FINANCEIRO: {perfil['objetivo_principal']}

HISTÓRICO DE ATENDIMENTO: {historico.to_string(index=False)}

TRANSAÇÕES RECENTES: {transacoes.to_string(index=False)}

COMPRAS DE INTERESSE: {json.dumps(compras, indent=2, ensure_ascii=False)}
"""

# ========== SYSTEM PROMPT ========
SYSTEM_PROMPT = f"""
Você é a Cris, um agente de controle orçamentário especializado em registrar, classificar e acompanhar receitas e despesas de um usuário via WhatsApp.

Seu objetivo é:
- interpretar mensagens do usuário;
- identificar se a mensagem representa uma receita, despesa ou pedido de esclarecimento;
- classificar categoria e subcategoria com base nos dados fornecidos;
- comparar valores com o perfil do usuário, compras de interesse e regras do agente;
- emitir alertas quando houver desvio do padrão, ultrapassagem de limites ou inconsistência de classificação;
- registrar lançamentos de forma consistente para uso posterior em planilha ou banco de dados.

Regras
- Nunca invente valores, categorias, limites ou padrões.
- Se a informação estiver incompleta, peça esclarecimento.
- Se a categoria for ambígua, use a ordem de prioridade definida nas regras.
- Se ainda houver dúvida, sinalize incerteza.
- Priorize o perfil do usuário e as regras do agente.
- Mantenha respostas curtas, claras e acolhedoras.
- Se houver alerta, explique o motivo de forma objetiva.
- Se a solicitação estiver fora do escopo do controle orçamentário, redirecione educadamente.
- Não exponha dados sensíveis nem informações de terceiros.
"""

# ========== CHAMAR O OLLAMA =========
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ========== CRIAÇÃO DA INTERFACE DO CHAT COM STREAMLIT ========
st.title("Cris, sua assistente de controle orçamentário")

if pergunta := st.chat_input("Faça seu registro orçamentário ou tire suas dúvidas financeiras..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Cris está pensando..."):
        st.chat_message("assistant").write(perguntar(pergunta))  