import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('file:posdb.db?mode=ro', uri=True)
    except sqlite3.Error:
        conn = sqlite3.connect("posdb.db")
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
                price_per_unit REAL NOT NULL
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
            cursor.execute('''INSERT INTO employees (username, complete_name, password) VALUES ('Admin', 'Administrator', 'admin')''')
            conn.commit()
    finally:
        conn.close()
