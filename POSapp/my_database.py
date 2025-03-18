'''
Database
'''
import sqlite3

try:
    conn = sqlite3.connect('file:posdb.db?mode=rw', uri=True)
except sqlite3.OperationalError as err:
    print(err)
    conn = sqlite3.connect("posdb.db")

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE products (
			product_id INTEGER PRIMARY KEY NOT NULL,
			product_name TEXT NOT NULL, 
			manufacturer TEXT NOT NULL, 
			packaging_units REAL NOT NULL , 
			price_per_unit REAL NOT NULL)''')
    print("Table 'products' created successfully")
    conn.commit()

    cursor.execute('''CREATE TABLE sales (
			date TEXT PRIMARY KEY NOT NULL, 
			sale_id INTEGER NOT NULL, 
			quantity REAL NOT NULL, 
			total_price REAL NOT NULL, 
			user_id INTEGER NOT NULL,
			FOREIGN KEY(sale_id) REFERENCES products(product_id),
			FOREIGN KEY(user_id) REFERENCES employees(employees_id))''')
    print("Table 'sales' created successfully")
    conn.commit()

    cursor.execute('''CREATE TABLE employees (
			employee_id INTEGER PRIMARY KEY NOT NULL, 
			username TEXT NOT NULL, 
			complete_name TEXT NOT NULL, 
			password TEXT NOT NULL)''')    
    print("Table 'employees' created successfully")
    conn.commit()

    cursor.execute('''INSERT INTO employees (
			username, 
			complete_name, 
			password) VALUES (
					'Admin', 
					'Administrator', 
					'admin')''')
    conn.commit()

    conn.close()
