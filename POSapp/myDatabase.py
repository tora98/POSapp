import sqlite3

try:
    conn = sqlite3.connect('file:posdb.db?mode=rw', uri=True)
    print("Database connected successfully")
except Exception as err:
    print(err)
    print("Creating database...")
    conn = sqlite3.connect("posdb.db")
    print("Database created successfully")

    cursor = conn.cursor()
    cursor.execute("CREATE TABLE products (product_id INTEGER PRIMARY KEY NOT NULL, product_name TEXT NOT NULL,packaging_units REAL NOT NULL , price_per_unit REAL NOT NULL)")
    print("Table 'products' created successfully")
    conn.commit()

    cursor.execute("CREATE TABLE sales (date TEXT PRIMARY KEY NOT NULL, product_id INTEGER NOT NULL, quantity REAL NOT NULL, total_price REAL NOT NULL, user_id INTEGER NOT NULL)")
    print("Table 'sales' created successfully")
    conn.commit()

    cursor.execute("CREATE TABLE users (user_id INTEGER PRIMARY KEY NOT NULL, username TEXT NOT NULL, complete_name TEXT NOT NULL, password TEXT NOT NULL)")    
    print("Table 'users' created successfully")
    conn.commit()

finally:
    conn.close()
    print("Database closed")
    