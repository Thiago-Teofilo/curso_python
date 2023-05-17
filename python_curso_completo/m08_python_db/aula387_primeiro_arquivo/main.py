import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'custumers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Deleta a tabela se existir
cursor.execute(
    f'DROP TABLE IF EXISTS {TABLE_NAME}'
)
connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
    )
connection.commit()

# Registrar valores ns colunas da tabela
sql = f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (:n, :w)'

cursor.executemany(sql, (
    {'n': 'Carlao', 'w': 95.80},
    {'n': 'Roger', 'w': 75.00},
    {'n': 'Maguila', 'w': 100.00},
    ))
connection.commit()

cursor.close()
connection.close()