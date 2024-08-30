import streamlit as st
import openai
import os

# Configure a chave API da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")  # Use a variável de ambiente

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def traduzir_texto_tecnico(texto):
    prompt = f"Traduza o seguinte texto para um contexto técnico de cibersegurança: {texto}"
    return chat_with_gpt(prompt)

st.title("Assistente de Tradução Técnica em Cibersegurança")
st.write("Insira o texto que deseja traduzir para um contexto técnico de cibersegurança.")

user_input = st.text_area("Texto Original", "")

if st.button("Traduzir"):
    if user_input:
        traducao = traduzir_texto_tecnico(user_input)
        st.write("Tradução Técnica:")
        st.write(traducao)
    else:
        st.write("Por favor, insira um texto para traduzir.")
