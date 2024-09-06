import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)''')

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (
        f'User{i}', f'example{i}@ya.ru', i*10, 1000)
    )

cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 = 1', (500,))
cursor.execute('DELETE FROM Users WHERE id = ? OR id = ? OR id = ? or id = ?', (1, 4, 7, 10))

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]}, Возраст: {user[2]}, Баланс: {user[3]}')

cursor.execute('DELETE FROM Users WHERE id = 6')
cursor.execute('SELECT COUNT(*) FROM Users')
count = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
sum_ = cursor.fetchone()[0]
print(round(sum_/count, 2))

connection.commit()
connection.close()
