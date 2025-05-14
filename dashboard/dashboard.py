import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import requests
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Dashboard de Irrigação", layout="wide")

def carregar_dados():
    conn = sqlite3.connect('sensores.db')
    df = pd.read_sql_query("SELECT * FROM leituras_sensores", conn)
    conn.close()
    return df

def obter_dados_clima():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    cidade = "São Paulo"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

st.title("🌱 Dashboard do Sistema de Irrigação Inteligente")
dados = carregar_dados()
clima = obter_dados_clima()

if clima:
    st.subheader("☀️ Clima Atual - São Paulo")
    st.markdown(f"**Temperatura:** {clima['main']['temp']} °C")
    st.markdown(f"**Umidade:** {clima['main']['humidity']}%")
    st.markdown(f"**Condições:** {clima['weather'][0]['description'].capitalize()}")
else:
    st.warning("Não foi possível obter dados climáticos.")

if dados.empty:
    st.warning("Nenhuma leitura encontrada no banco de dados.")
else:
    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.line(dados, x='data_hora', y='umidade', title='Umidade (%)')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.line(dados, x='data_hora', y='ph', title='pH Simulado')
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("💡 Últimos Status de Irrigação")
    st.dataframe(dados[['data_hora', 'irrigando']].sort_values(by='data_hora', ascending=False).head(10))

    with st.expander("📋 Leitura Completa dos Sensores"):
        st.dataframe(dados.sort_values(by='data_hora', ascending=False))