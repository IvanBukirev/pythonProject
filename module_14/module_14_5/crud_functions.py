import sqlite3


def initiate_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
     ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL    
       )
    ''')
    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    products = c.execute('SELECT * FROM Products').fetchall()
    conn.commit()
    conn.close()
    return products


def add_user(username, email, age):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''
    INSERT INTO Users (username, email, age, balance)
    VALUES (?,?,?,?)
    ''', (username, email, age, 1000))
    conn.commit()
    conn.close()



def is_included(username):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('SELECT id FROM Users WHERE username = ?', (username,))
    result = c.fetchone()
    conn.commit()
    conn.close()
    if result:
        return True
    else:
        return False
