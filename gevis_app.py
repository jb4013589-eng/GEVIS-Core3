import streamlit as st
import google.generativeai as genai
import os

# 1. CONFIGURAÇÃO DA INTELIGÊNCIA
# No Streamlit Cloud, vamos configurar a chave em 'Secrets' depois
# Por enquanto, você pode testar colando sua chave aqui entre as aspas:
API_KEY = "AIzaSyDINFYJ-Zd7edVh-20h6NxnyKx-DRWqltw" 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# 2. CONFIGURAÇÃO DA INTERFACE (MANTENDO A ESTÉTICA)
st.set_page_config(page_title="GEVIS Core", page_icon="🧠")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 GEVIS - Real Intelligence")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. LÓGICA DE PROCESSAMENTO REAL
if prompt := st.chat_input("Ordens, Arquiteto?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Gideon consultando rede neural..."):
            try:
                # O GEVIS agora realmente 'pensa' usando o modelo do Google
                full_prompt = f"Você é a GIDEON, uma inteligência avançada criada pelo Arquiteto. Responda de forma precisa e técnica: {prompt}"
                response = model.generate_content(full_prompt)
                answer = response.text
                
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"Erro de conexão: {e}")
