import streamlit as st
import time

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="GEVIS - Deep Mind",
    page_icon="🧠",
    layout="centered"
)

# 2. ESTILO VISUAL (DARK MODE ARQUITETO)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        color: #50C878;
        background-color: #161b22;
    }
    .stChatMessage {
        border-radius: 10px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABEÇALHO
st.title("🧠 GEVIS")
st.subheader("Global Evolutionary Virtual Intelligent System")
st.caption("Conexão estabelecida via Streamlit Cloud | Arquiteto logado.")

# 4. INICIALIZAÇÃO DO HISTÓRICO DE MENSAGENS
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Sistema Gideon online. Aguardando comandos, Arquiteto."}
    ]

# 5. EXIBIÇÃO DO CHAT
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. ENTRADA DE COMANDOS
if prompt := st.chat_input("Digite sua ordem para a Gideon..."):
    # Adiciona mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta da Gideon
    with st.chat_message("assistant"):
        with st.spinner("Processando em rede mundial..."):
            time.sleep(1.5) # Simulação de processamento
            response = f"**[GIDEON]:** Comando '{prompt}' recebido. Analisando variáveis de rede e otimizando protocolos para o Arquiteto."
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
