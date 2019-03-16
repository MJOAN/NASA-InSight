import sqlite3 as sql
conn = sql.connect('"users.db')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS users')


def insertPhone(phone):
    conn = sql.connect("users.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (phone) VALUES (?)", (phone,))
    conn.commit()
    conn.close()

def insertEmail(email):
    conn = sql.connect("users.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (email) VALUES (?)", (email,))
    conn.commit()
    conn.close()

def getUsers():
    conn = sql.connect("users.db")
    cur = conn.cursor()
    cur.execute('SELECT * from users')
    users = cur.fetchall()
    conn.close()
    return users


# get user info from cli 
# sqlite3 database.db "select * from users"

conn.commit()
conn.close()