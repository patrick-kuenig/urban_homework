import sqlite3


def initiate_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INT PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL)
    """)

    for i in range(1, 6):
        cursor.execute("""
        INSERT INTO Products (title, description, price) VALUES (?, ?, ?)
        """, (f'Product {i}', f'Product {i} is the greatest product ever', i * 30))

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()

    connection.commit()
    connection.close()

    return all_products


def add_user(username, email, age):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)""", (username, email, age, 1000))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    users = cursor.execute("""
    SELECT username FROM Users
    """).fetchall()
    for user in users:
        if username == user[0]:
            return True
    return False


if __name__ == '__main__':
    initiate_db()
