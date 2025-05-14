import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard de Irrigação", layout="wide")

@st.cache_data
def carregar_dados():
    conn = sqlite3.connect('sensores.db')
    df = pd.read_sql_query("SELECT * FROM leituras_sensores", conn)
    conn.close()
    return df

st.title("🌱 Dashboard do Sistema de Irrigação Inteligente")
dados = carregar_dados()

if dados.empty:
    st.warning("Nenhuma leitura encontrada no banco de dados.")
else:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 Gráfico de Umidade")
        fig1, ax1 = plt.subplots()
        ax1.plot(pd.to_datetime(dados['data_hora']), dados['umidade'], color='blue', marker='o')
        ax1.set_ylabel('Umidade (%)')
        ax1.set_xlabel('Data/Hora')
        st.pyplot(fig1)

    with col2:
        st.subheader("📉 Gráfico de pH (simulado)")
        fig2, ax2 = plt.subplots()
        ax2.plot(pd.to_datetime(dados['data_hora']), dados['ph'], color='green', marker='x')
        ax2.set_ylabel('pH (simulado pelo LDR)')
        ax2.set_xlabel('Data/Hora')
        st.pyplot(fig2)

    st.subheader("💡 Status da Irrigação")
    status = dados[['data_hora', 'irrigando']]
    st.dataframe(status.sort_values(by='data_hora', ascending=False).head(10))

    st.subheader("📋 Leitura Completa dos Sensores")
    st.dataframe(dados.sort_values(by='data_hora', ascending=False))
