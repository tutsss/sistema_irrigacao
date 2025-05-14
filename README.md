# 🌿 Sistema de Irrigação Inteligente com ESP32, Python e Dashboard

Este projeto simula um sistema de irrigação inteligente com sensores de umidade, luz, presença de nutrientes, integração com clima externo via API e visualização de dados em um dashboard interativo.

## 📁 Estrutura do Projeto

```
├── esp32/
│   └── main.ino                  # Código para o ESP32 com sensores
│
├── backend/
│   ├── sensores_db.py            # CRUD para leituras dos sensores
│   ├── coleta_clima.py           # Coleta dados do OpenWeatherMap
│   └── sensores.db               # Banco de dados SQLite
│
├── dashboard/
│   └── app.py                    # Dashboard com Streamlit
│
├── requirements.txt             # Dependências Python
└── README.md                    # Este arquivo
```

## 🚀 Como Executar

### 1. Simulação do ESP32 (Wokwi)

* Abra o arquivo `main.ino` no [https://wokwi.com](https://wokwi.com)
* Configure os seguintes componentes:

  * DHT22 no pino 21
  * LDR no pino 34
  * Botões (fósforo e potássio) nos pinos 12 e 14
  * LED ou relé no pino 26

### 2. Instale as dependências Python

```bash
pip install -r requirements.txt
```

### 3. Execute o backend (armazenamento de dados)

```bash
python backend/sensores_db.py
```

### 4. Execute o script de clima

```bash
python backend/coleta_clima.py
```

> Este script coleta os dados do clima e salva no banco de dados.

### 5. Execute o dashboard

```bash
streamlit run dashboard/app.py
```

## 🌐 API Utilizada

* OpenWeatherMap
* A chave utilizada já está inserida no código `coleta_clima.py`.

## 🧠 Sensores Simulados

* **DHT22:** Umidade do solo
* **LDR:** Simula pH
* **Botões:** Presença de fósforo e potássio
* **Relé/LED:** Liga a irrigação automaticamente

## 📊 Funcionalidades do Dashboard

* Gráficos de umidade e pH
* Leitura das últimas leituras
* Status da irrigação
* (Sugestão) Leitura climática externa

## 📌 Observações

* O banco de dados é gerado automaticamente na primeira execução.
* Os dados de sensores são simulados.

---

Desenvolvido para a disciplina de **Gestão do Agronegócio - Fase 3 (FIAP)**.

