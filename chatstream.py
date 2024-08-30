import streamlit as st
import openai
from config import OPENAI_API_KEY  # Importe a chave da API de config.py

# Configure a chave API da OpenAI
openai.api_key = OPENAI_API_KEY

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Função para traduzir texto no contexto de cibersegurança
def traduzir_texto_tecnico(texto):
    prompt = f"Traduza o seguinte texto para um contexto técnico de cibersegurança: {texto}"
    return chat_with_gpt(prompt)

# Interface com Streamlit
st.title("Assistente de Tradução Técnica em Cibersegurança")
st.write("Insira o texto que deseja traduzir para um contexto técnico de cibersegurança.")

# Campo de entrada de texto do usuário
user_input = st.text_area("Texto Original", "")

if st.button("Traduzir"):
    if user_input:
        # Obtenha a tradução técnica
        traducao = traduzir_texto_tecnico(user_input)
        # Exiba a tradução
        st.write("Tradução Técnica:")
        st.write(traducao)
    else:
        st.write("Por favor, insira um texto para traduzir.")
