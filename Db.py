import sqlite3

# Ainda não implementado


conn = sqlite3.connect('db_carros.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE carros
    (id INTEGER PRIMARY KEY, marca TEXT, modelo TEXT, cor TEXT, ano INTEGER)
''')
conn.commit()
conn.close()