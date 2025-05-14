import sqlite3
from datetime import datetime

conn = sqlite3.connect('sensores.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS leituras_sensores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_hora TEXT,
    umidade REAL,
    ph INTEGER,
    fosforo TEXT,
    potassio TEXT,
    irrigando TEXT
)
''')
conn.commit()

def inserir_leitura(umidade, ph, fosforo, potassio, irrigando):
    cursor.execute('''
        INSERT INTO leituras_sensores (data_hora, umidade, ph, fosforo, potassio, irrigando)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), umidade, ph, fosforo, potassio, irrigando))
    conn.commit()

def listar_leituras():
    cursor.execute('SELECT * FROM leituras_sensores')
    return cursor.fetchall()

def atualizar_leitura(id, novo_valor_umidade):
    cursor.execute('UPDATE leituras_sensores SET umidade = ? WHERE id = ?', (novo_valor_umidade, id))
    conn.commit()

def deletar_leitura(id):
    cursor.execute('DELETE FROM leituras_sensores WHERE id = ?', (id,))
    conn.commit()