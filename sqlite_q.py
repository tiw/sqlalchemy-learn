import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('SELECT * FROM person')
print c.fetchall()
c.execute('SELECT * from address')
print c.fetchall()
conn.close()
