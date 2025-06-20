import sqlite3
import argon2

def get_db():
    name = 'file:posdb.db?mode=rw'
    return name

def get_hash(password):
    hasher = argon2.PasswordHasher()
    key = hasher.hash(password)
    return key

def create_database():
    try:
        database = get_db()
        conn = sqlite3.connect(database, uri=True)
    except sqlite3.Error:
        conn = sqlite3.connect("./posdb.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                complete_name TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                manufacturer TEXT NOT NULL,
                packaging_units TEXT NOT NULL,
                price_per_unit REAL NOT NULL,
                state TEXT NOT NULL
            )
        ''')
        conn.commit()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                total_price REAL NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products(product_id),
                FOREIGN KEY (user_id) REFERENCES employees(employee_id)
            )
        ''')
        conn.commit()

        cursor.execute('''SELECT * FROM employees''')
        if cursor.fetchone() == 'Admin':
            pass
        else:
            pwd = 'admin'
            hashed_password = get_hash(pwd)
            cursor.execute(f'''INSERT INTO employees (
                username,
                complete_name,
                password
                )
                VALUES (
                    'Admin',
                    'Administrator',
                    '{hashed_password}'
                    )''')
            conn.commit()
    conn.close()
