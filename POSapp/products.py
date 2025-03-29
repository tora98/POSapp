import tkinter as tk
from tkinter import ttk
import sqlite3


class Products(ttk.Frame):
    '''
    Frame for adding new products
    '''

    def __init__(self, master):
        super().__init__(master)

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 15))

        self.frame1 = ProductEntry(self, "", "", "", "", "")
        self.frame2 = ProductList(self)

        self.pack(expand=True, fill="both")


class ProductEntry(ttk.Frame):
        def __init__(self, master, product_ID, product_name, manufacturer, packaging_units, price_per_unit):
            super().__init__(master)

            self.product_ID = product_ID
            self.product_name = product_name
            self.manufacturer = manufacturer
            self.packaging_units = packaging_units
            self.price_per_unit = price_per_unit

            self.lbl_product_name = ttk.Label(self, text="Product Name:", font=("Helvetica", 20))
            self.lbl_product_name.pack(pady=(10,0))
            self.entry_product_name = ttk.Entry(self, font=("Arial", 30))
            self.entry_product_name.pack(pady=(0, 10))
            self.lbl_manufacturer = ttk.Label(self, text="Manufacturer:", font=("Helvetica", 20))
            self.lbl_manufacturer.pack(pady=(10,0))
            self.entry_manufacturer = ttk.Entry(self, font=("Arial", 30))
            self.entry_manufacturer.pack(pady=(0, 10))
            self.lbl_packaging_units = ttk.Label(self, text="Packaging Units (Number of kilos or pieces per Bag/Box/Bottle):", font=("Helvetica", 10))
            self.lbl_packaging_units.pack(pady=(10,0))
            self.entry_packaging_units = ttk.Entry(self, font=("Arial", 30))
            self.entry_packaging_units.pack(pady=(0, 10))
            self.lbl_price_per_unit = ttk.Label(self, text="Price Per Unit:", font=("Helvetica", 20))
            self.lbl_price_per_unit.pack(pady=(10,0))
            self.entry_price_per_unit = ttk.Entry(self, font=("Arial", 30))
            self.entry_price_per_unit.pack(pady=(0, 10))
            self.insert(product_name, manufacturer, packaging_units, price_per_unit)

            self.lbl_error = ttk.Label(self, text="", foreground="red", font=("Helvetica", 10))
            self.lbl_error.pack(pady=10)

            self.btn_add = ttk.Button(self, text="Add", command=self.add_product)
            self.btn_add.pack(side="left", pady=10, expand=True)
            self.btn_clear = ttk.Button(self, text="Clear", command=self.clear_entry)
            self.btn_clear.pack(side="left", pady=10, expand=True) 
            self.btn_update = ttk.Button(self, text="Update", command=self.update)
            self.btn_update.pack(side="left", pady=10, expand=True)
            self.btn_cancel = ttk.Button(self, text="Cancel", command=self.cancel)
            self.btn_cancel.pack(side="left", pady=10, expand=True)

            self.pack(expand=True, fill="both", side="left", ipadx=10, ipady=10)

        def insert(self, product_name, manufacturer, packaging_units, price_per_unit):
            self.entry_product_name.insert("end", product_name)
            self.entry_manufacturer.insert("end", manufacturer)
            self.entry_packaging_units.insert("end", packaging_units)
            self.entry_price_per_unit.insert("end", price_per_unit)

        def add_product(self):
            '''
            Add a product to the database
            '''
            get_product_name = self.entry_product_name.get()
            get_manufacturer = self.entry_manufacturer.get()
            get_packaging_units = self.entry_packaging_units.get()
            get_price_per_unit = self.entry_price_per_unit.get()

            if get_product_name == "" or get_manufacturer == "" or get_packaging_units == "" or get_price_per_unit == "":
                self.lbl_error.config(text="Please fill out all fields.")
            else:
                conn = sqlite3.connect('file:posdb.db?mode=rw', uri=True)
                cursor = conn.cursor()
                try:
                    product_name = self.entry_product_name.get()
                    manufacturer = self.entry_manufacturer.get()
                    packaging_units = self.entry_packaging_units.get()
                    price_per_unit = self.entry_price_per_unit.get()
                    cursor.execute(f'''INSERT INTO products (
                        product_name,
                        manufacturer,
                        packaging_units,
                        price_per_unit
                        ) VALUES (
                        '{product_name}',
                        '{manufacturer}',
                        '{packaging_units}',
                        '{price_per_unit}'
                        )
                    ''')
                    conn.commit()
                    conn.close()
                    self.lbl_error.config(text="Product added successfully.")
                    self.clear_entry()

                except sqlite3.IntegrityError as err:
                    self.lbl_error.config(text=str(err))

        def clear_entry(self):
            '''
            Clear the entry fields
            '''
            self.entry_product_name.delete(0, "end")
            self.entry_manufacturer.delete(0, "end")
            self.entry_packaging_units.delete(0, "end")
            self.entry_price_per_unit.delete(0, "end")
            self.lbl_error.config(text="")

        def update(self):
            conn = sqlite3.connect('file:posdb.db?mode=rw', uri=True)
            cursor = conn.cursor()

            get_product_name = self.entry_product_name.get()
            get_manufacturer = self.entry_manufacturer.get()
            get_packaging_units = self.entry_packaging_units.get()
            get_price_per_unit = self.entry_price_per_unit.get()

            cursor.execute(f'''UPDATE products SET
                product_name = '{get_product_name}',
                manufacturer = '{get_manufacturer}',
                packaging_units = '{get_packaging_units}',
                price_per_unit = '{get_price_per_unit}'
                WHERE product_id = {self.product_ID}''')
            conn.commit()
            conn.close()

        def cancel(self):
            self.destroy()


class ProductList(ttk.Frame):
    '''
    Frame for product table
    '''

    def __init__(self, master):
        super().__init__(master)
        # TODO: Add scrollbar to treeview

        self.tree = ttk.Treeview(master, columns=("product_id", "product_name", "manufacturer", "packaging_units", "price_per_unit"), show="headings")
        self.tree.column("product_id", width=0) 
        self.tree.heading("product_id", text="ID")
        self.tree.column("product_name", width=200)
        self.tree.heading("product_name", text="Product Name")
        self.tree.column("manufacturer", width=200)
        self.tree.heading("manufacturer", text="Manufacturer")
        self.tree.column("packaging_units", width=200)
        self.tree.heading("packaging_units", text="Packaging Units")
        self.tree.column("price_per_unit", width=200)
        self.tree.heading("price_per_unit", text="Price Per Unit")
        self.tree.pack(expand=True, fill="both")

        self.refresh_table()

        self.btn_refresh = ttk.Button(self, text="Refresh", command=self.refresh_table)
        self.btn_refresh.pack(side="left", pady=10, expand=True)
        self.btn_delete = ttk.Button(self, text="Delete", command=self.delete_product)
        self.btn_delete.pack(side="left", pady=10, expand=True)

        # if self.tree.selection():
        #     product_ID = self.tree.item(self.tree.selection())['values'][0]
        #     product_name = self.tree.item(self.tree.selection())['values'][1]
        #     manufacturer = self.tree.item(self.tree.selection())['values'][2]
        #     packaging_units = self.tree.item(self.tree.selection())['values'][3]
        #     price_per_unit = self.tree.item(self.tree.selection())['values'][4]
        #     # TODO: Test if this works
        #     ProductEntry(product_ID, product_name, manufacturer, packaging_units, price_per_unit)

        # else:
        #     pass

        self.pack(expand=True, fill="both", side="left", ipadx=10, ipady=10)

    def refresh_table(self) -> None:
        '''
        Refreshes the table
        '''
        self.tree.delete(*self.tree.get_children())
        conn = sqlite3.connect('file:posdb.db?mode=rw', uri=True)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)
        conn.close()

    def delete_product(self):
        '''
        Deletes a product from the database
        '''
        selected_item = self.tree.item(self.tree.selection())
        conn = sqlite3.connect('file:posdb.db?mode=rw', uri=True)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM products WHERE product_id = {selected_item['values'][0]}")
        conn.commit()
        conn.close()
        self.refresh_table()
