import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
  )''')
# for i in range(1, 11):
#     cursor.execute('''
#     INSERT INTO Users ( username, email, age, balance)
#     VALUES (?,?,?,?)
#     ''', ('user' + str(i), 'example' + str(i) + '@gmail.com', i * 10, 1000))


cursor.execute('''UPDATE Users SET balance = 500 WHERE (id - 1) % 2 = 0''')

cursor.execute('''DELETE FROM Users WHERE (id - 1) % 3 = 0''')

cursor.execute('''SELECT username, email, age, balance FROM Users WHERE age != 60''')
result = cursor.fetchall()
for username, email, age, balance in result:
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

cursor.execute(''' DELETE FROM Users WHERE id = 6''')

cursor.execute(''' SELECT COUNT(*) FROM Users''')
total_users = cursor.fetchone()[0]

cursor.execute(''' SELECT SUM(balance) FROM Users''')
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

connection.commit()
connection.close()
