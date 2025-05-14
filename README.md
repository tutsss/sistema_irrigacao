# Projeto de Sistema de Irrigação Inteligente 🌱

Este projeto simula um sistema de irrigação automatizado com sensores simulados usando ESP32, armazenamento em banco de dados e visualização em dashboard.

## Estrutura

- `esp32_sensor_control`: Código C++ para ESP32 com sensores de umidade, fósforo, potássio e pH (simulado).
- `python_backend`: Script Python com SQLite para armazenar dados e executar operações CRUD.
- `dashboard`: Aplicação em Streamlit para visualização de dados em tempo real.

## Requisitos

```bash
pip install -r requirements.txt
```

## Executando o Dashboard

```bash
cd dashboard
streamlit run app.py
```

## Inserindo dados no banco (exemplo)

Use o script `database.py` para inserir leituras simuladas.
