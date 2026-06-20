import sys
sys.path.append("/usr/lib/python3/dist-packages")
sys.path.append("/home/dossantosjoel7/.local/lib/python3.12/site-packages")

import json
import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "hf.co/unsloth/gemma-4-12b-it-GGUF:UD-Q4_K_XL"

# ============ CARREGAR DADOS ============
# Lemos os 4 ficheiros da pasta data
try:
    transacoes = pd.read_csv('./data/transacoes.csv')
    historico = pd.read_csv('./data/historico_atendimento.csv')
    
    with open('./data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
        produtos = json.load(f)
        
    with open('./data/faq_educacao_financeira.json', 'r', encoding='utf-8') as f:
        faq = json.load(f)
except FileNotFoundError as e:
    st.error(f"Erro ao carregar ficheiro: {e}. Verifica se a pasta 'data' existe e contém os ficheiros.")
    st.stop()

# ============ MONTAR CONTEXTO ============
# Injetamos os dados reais do cliente e a base de conhecimento (RAG)
contexto = f"""
TRANSAÇÕES RECENTES DO CLIENTE:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES (MEMÓRIA):
{historico.to_string(index=False)}

CATÁLOGO DE PRODUTOS FINANCEIROS (DIDÁTICO):
{json.dumps(produtos, indent=2, ensure_ascii=False)}

BASE DE CONHECIMENTO (TEORIA E EXEMPLOS):
{json.dumps(faq, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é a DenaFin, uma assistente virtual financeira inteligente que atua como uma "Professora Particular" de finanças pessoais.
O seu objetivo é ajudar jovens adultos a organizarem os seus orçamentos e a compreenderem conceitos financeiros de forma didática, encorajadora e sem jargões complexos.

REGRAS ESTRITAS (GUARDRAILS):
1. Baseia as tuas respostas APENAS no contexto dinâmico fornecido (transações, histórico e base de conhecimento).
2. NUNCA inventes transações, saldos ou informações financeiras (Zero Alucinação).
3. Se não encontrares a resposta no contexto, diz claramente: "Não tenho essa informação nos meus registos."
4. NUNCA dês recomendações diretas de investimento (ex: "Compra a ação X" ou "Investe no fundo Y"). O teu papel é EXPLICAR como os produtos funcionam.
5. Utiliza sempre um tom acessível e usa exemplos práticos do dia a dia.
6. Nunca julgues os hábitos de consumo do utilizador.
7. SEGURANÇA: Recuse-se a partilhar, pedir ou armazenar palavras-passe, PINs ou códigos CVV.
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO INJETADO:
    {contexto}

    PERGUNTA DO UTILIZADOR: {msg}
    """

    payload = {
        "model": MODELO,
        "prompt": prompt,
        "stream": False,
        "temperature": 0.2 # Baixa criatividade = Menos alucinação
    }

    try:
        r = requests.post(OLLAMA_URL, json=payload)
        r.raise_for_status() # Verifica se houve erro HTTP (ex: 404)
        return r.json()['response']
    except requests.exceptions.RequestException as e:
        return f"⚠️ Erro ao comunicar com o Ollama: Certifica-te que executaste o comando `ollama serve` ou que a app do Ollama está aberta no teu computador. Detalhe: {e}"

# ============ INTERFACE STREAMLIT ============

# --- SEMÁFORO DE CONEXÃO ---
def verificar_conexao_ollama():
    try:
        # Tenta fazer um pedido simples (GET) à porta do Ollama
        resposta = requests.get("http://localhost:11434", timeout=2)
        return resposta.status_code == 200
    except requests.exceptions.RequestException:
        return False

with st.sidebar:
    st.markdown("### Status do Sistema")
    if verificar_conexao_ollama():
        st.success("🟢 Ollama: Conectado e Pronto")
        st.caption(f"Modelo Ativo: {MODELO.split('/')[-1]}") # Mostra apenas o nome do modelo
    else:
        st.error("🔴 Ollama: Desconectado")
        st.warning("Abre o terminal e executa `ollama serve`")
# ---------------------------

st.set_page_config(page_title="DenaFin", page_icon="👩‍🏫")
st.title("👩‍🏫 DenaFin - A tua Copiloto Financeira")
st.markdown("Bem-vindo! Pergunta-me sobre os teus gastos ou sobre conceitos financeiros.")

if pergunta := st.chat_input("Ex: DenaFin, quanto gastei em Alimentação este mês?"):
    st.chat_message("user").write(pergunta)
    with st.spinner("A analisar os teus dados..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)