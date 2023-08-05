import sqlite3

conn = sqlite3.connect('meu_banco_de_dados.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE carros
    (id INTEGER PRIMARY KEY, marca TEXT, modelo TEXT, cor TEXT, ano INTEGER)
''')
conn.commit()
conn.close()