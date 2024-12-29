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



    conn.commit()
    conn.close()



def get_all_products():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    products = c.execute('SELECT * FROM Products').fetchall()
    conn.commit()
    conn.close()
    return products
