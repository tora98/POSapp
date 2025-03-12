import tkinter as tk
from tkinter import ttk
import datetime as dt
import sqlite3

class login(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
                
        #TODO: Add Validation for users

        self.myframe = ttk.Frame(self)

        self.lbl_username = ttk.Label(self.myframe, text = "User Name:", font=("Helvetica", 20))
        self.entry_username = ttk.Entry(self.myframe, font = ("Arial", 30))
        self.lbl_password = ttk.Label(self.myframe, text = "Password:", font=("Helvetica", 20))
        self.entry_password = ttk.Entry(self.myframe, font = ("Arial", 30)) 
        self.btn_login = ttk.Button(self.myframe, text = "Login", default="active", command=self.show_tabs)

        self.lbl_username.pack(pady = 5)
        self.entry_username.pack()
        self.lbl_password.pack(pady = 5)
        self.entry_password.pack()
        self.btn_login.pack(pady = 5, ipadx = 10, ipady = 5)

        self.myframe.place(width=600, height=400, relx=0.5, rely=0.5, anchor="center")

        self.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    def show_tabs(self):
        self.next_frame = tabs(self, self.entry_username.get())

class tabs(ttk.Notebook):
    def __init__(self, master, user):
        super().__init__(master)    

        self.maintab = main(self, user)
        self.productstab = products(self)
        self.addproductstab = add_products(self)
        self.abouttab = about(self)
        self.add(self.maintab, text="Daily Sales")
        self.add(self.productstab, text="Products List")
        self.add(self.addproductstab, text="Add Products")
        self.add(self.abouttab, text="About")   

        self.pack(expand=True, fill="both") 

class main(ttk.Frame):
    def __init__(self, master, user):
        super().__init__(master)

        self.frame1 = self.nav_frame(self, user)
        self.frame2 = self.entry_frame(self)
        self.frame3 = self.table_frame(self)

        self.pack(expand=True, fill="both", ipadx=10, ipady=10)

    class nav_frame(ttk.Frame):
        def __init__(self, master, user):
            super().__init__(master)

            self.user = user
            self.date = dt.datetime.now()

            self.lbl_user = ttk.Label(self, text = self.user, font=("Helvetica", 20), anchor="w").pack(side="left", expand=True, fill="x")
            self.lbl_date = ttk.Label(self, text = f"{self.date:%A, %B %d %Y}", font=("Helvetica", 20), anchor="e").pack(side="left", expand=True, fill="x")

            self.pack(fill="x")

    class entry_frame(ttk.Frame):
        def __init__(self, master):
            super().__init__(master)

            self.f1 = self.frame1(self)

            self.config(border=1, relief="solid")

            self.pack(side="left", expand=True, fill="both")
            # self.place(relx=0.01, rely=0.11, relwidth=0.58, relheight=0.88)

        class frame1(ttk.Frame):
            def __init__(self, master):
                super().__init__(master)

                #TODO: Show Autocomplete when typing        

                self.style = ttk.Style()
                self.style.configure("TButton", font=("Helvetica", 15))

                self.lbl_item = ttk.Label(self, text = "Item Name:", font=("Helvetica", 20))
                self.lbl_item.pack(pady=(10,0))
                self.combo_item = ttk.Combobox(self, font=("Helvetica", 30))
                self.combo_item.pack(pady=(0,10), padx=10, expand=True, fill="x")
                self.combo_item['values'] = self.insert_values()
                self.lbl_quantity = ttk.Label(self, text = "Quantity:", font=("Helvetica", 20))
                self.lbl_quantity.pack(pady=(5,0))
                self.spinbox_quantity = ttk.Spinbox(self, font=("Helvetica", 30), values=(range(1, 100)))
                self.spinbox_quantity.pack(pady=(0,10), padx=10, expand=True, fill="x")
                self.lbl_price = ttk.Label(self, text = "Price:", font=("Helvetica", 20))
                self.lbl_price.pack(expand=True, fill="x")
                self.lbl_value = ttk.Label(self, text="0.00", font=("Helvetica", 30), anchor="center")
                self.lbl_value.pack(pady=(0, 10), expand=True, fill="both")

                self.btn_add = ttk.Button(self, text = "Add", command=self.add_sale).pack(pady=10, side="left", expand=True)
                self.btn_clear = ttk.Button(self, text = "Clear", command=self.clear_entry).pack(pady=10, side="left", expand=True)
                self.pack(expand=True, fill="both", ipadx=5)

            def insert_values(self):
                product_list = []
                conn = sqlite3.connect("posdb.db")
                cursor = conn.cursor()
                cursor.execute("SELECT product_name FROM products")
                rows = cursor.fetchall()

                for row in rows:
                    product_list.append(row[0])

                return product_list

            def add_sale(self):
                pass
                # conn = sqlite3.connect("posdb.db")
                # cursor = conn.cursor()
                # cursor.execute(f"INSERT INTO sales (date, product_id, quantity, total_price, user_id) VALUES (?, ?, ?, ?, ?), ({self.master.master.date}, {self.master.combo_item.get()}, {self.master.entry_quantity.get()}, {self.master.master.user})")
                # conn.commit()
                # conn.close()

            def clear_entry(self):
                self.combo_item.delete(0, "end")
                self.spinbox_quantity.delete(0, "end")

    class table_frame(ttk.Frame):
        def __init__(self, master):
            super().__init__(master)

            #TODO: Add a scroll bar to tree view

            self.tree = ttk.Treeview(self, columns=("item", "quantity", "price"), show="headings")
            self.tree.column("item", stretch=True, anchor="w")
            self.tree.heading("item", text="Item Name")
            self.tree.column("quantity", width=60, anchor="e")
            self.tree.heading("quantity", text="Quantity")
            self.tree.column("price", width=100, anchor="e", stretch=True)
            self.tree.heading("price", text="Price")
            self.tree.pack(padx= (5, 0), expand=True, fill="both")

            self.pack(side="left", expand=True, fill="both")
            # self.place(relx=0.6, rely=0.1, relwidth=0.4, relheight=0.9)

class products(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        #TODO: Add scrollbar to treeview 

        self.tree = ttk.Treeview(self, columns=("product_id", "product_name", "manufacturer", "packaging_units", "price_per_unit"), show="headings")
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

        self.show = self.refresh_table()

        self.btn_update = ttk.Button(self, text = "Update", command=self.update_product)
        self.btn_update.pack(side="left", pady=10, expand=True)
        self.btn_delete = ttk.Button(self, text = "Delete", command=self.delete_product)
        self.btn_delete.pack(side="left", pady=10, expand=True)

        self.pack(expand=True, fill="both", ipadx=10, ipady=10)

    def refresh_table(self):
        conn = sqlite3.connect("posdb.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)
        conn.close()

    def update_product(self):
        pass
        # conn = sqlite3.connect("posdb.db")
        # cursor = conn.cursor()
        # cursor.execute(f"UPDATE products SET product_name = '{self.tree.item(self.tree.selection())['values'][1]}', manufacturer = '{self.tree.item(self.tree.selection())['values'][2]}', packaging_units = '{self.tree.item(self.tree.selection())['values'][3]}', price_per_unit = '{self.tree.item(self.tree.selection())['values'][4]}' WHERE product_id = {self.tree.item(self.tree.selection())['values'][0]}")
        # conn.commit()
        # conn.close()
        # self.refresh_table()

    def delete_product(self):
        pass
        # conn = sqlite3.connect("posdb.db")
        # cursor = conn.cursor()
        # cursor.execute(f"DELETE FROM products WHERE product_id = {self.tree.item(self.tree.selection())['values'][0]}")
        # conn.commit()
        # conn.close()
        # self.refresh_table()

class add_products(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        #TODO: Check if product already exists before adding

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 15))

        self.lbl_product_name = ttk.Label(self, text = "Product Name:", font=("Helvetica", 20))
        self.lbl_product_name.pack(pady =(10,0))
        self.entry_product_name = ttk.Entry(self, font = ("Arial", 30))
        self.entry_product_name.pack(pady =(0, 10))
        self.lbl_manufacturer = ttk.Label(self, text = "Manufacturer:", font=("Helvetica", 20))
        self.lbl_manufacturer.pack(pady =(10,0))
        self.entry_manufacturer = ttk.Entry(self, font = ("Arial", 30))
        self.entry_manufacturer.pack(pady =(0, 10))
        self.lbl_packaging_units = ttk.Label(self, text = "Packaging Units (Number of kilos or pieces per Bag/Box/Bottle):", font=("Helvetica", 10))
        self.lbl_packaging_units.pack(pady =(10,0))
        self.entry_packaging_units = ttk.Entry(self, font = ("Arial", 30))
        self.entry_packaging_units.pack(pady =(0, 10))
        self.lbl_price_per_unit = ttk.Label(self, text = "Price Per Unit:", font=("Helvetica", 20))
        self.lbl_price_per_unit.pack(pady =(10,0))
        self.entry_price_per_unit = ttk.Entry(self, font = ("Arial", 30))
        self.entry_price_per_unit.pack(pady =(0, 10))

        self.lbl_error = ttk.Label(self, text = "", foreground="red", font=("Helvetica", 10))
        self.lbl_error.pack(pady=10)

        self.btn_add = ttk.Button(self, text = "Add", command=self.add_product)
        self.btn_add.pack(side="left", pady=10, expand=True)
        self.btn_clear = ttk.Button(self, text = "Clear", command=self.clear_entry)
        self.btn_clear.pack(side="left", pady=10, expand=True) 

        self.pack(expand=True, fill="both", ipadx=10, ipady=10)

    def add_product(self):
        if self.entry_product_name.get() == "" or self.entry_manufacturer.get() == "" or self.entry_packaging_units.get() == "" or self.entry_price_per_unit.get() == "":
            self.lbl_error.config(text = "Please fill out all fields.")
        else:
            conn = sqlite3.connect("posdb.db")
            cursor = conn.cursor()
            try:
                cursor.execute(f"INSERT INTO products (product_name, manufacturer, packaging_units, price_per_unit) VALUES ('{self.entry_product_name.get()}', '{self.entry_manufacturer.get()}', '{self.entry_packaging_units.get()}', '{self.entry_price_per_unit.get()}')")
                conn.commit()
                conn.close()
                self.lbl_error.config(text = "Product added successfully.")
                self.clear_entry()

            except Exception as err:
            # except sqlite3.IntegrityError:
                # self.lbl_error.config(text = "Product already exists.")
                self.lbl_error.config(text = str(err))
                

    def clear_entry(self):
        self.entry_product_name.delete(0, "end")
        self.entry_manufacturer.delete(0, "end")
        self.entry_packaging_units.delete(0, "end")
        self.entry_price_per_unit.delete(0, "end")

class add_user(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)


        self.myframe = ttk.Frame(self, bg="light blue")

        self.lbl_complete_name = ttk.Label(self.myframe, text = "Complete Name:", font=("Helvetica", 20))	
        self.entry_complete_name = ttk.Entry(self.myframe, font = ("Arial", 30))
        self.lbl_username = ttk.Label(self.myframe, text = "User Name:", font=("Helvetica", 20))
        self.entry_username = ttk.Entry(self.myframe, font = ("Arial", 30))
        self.lbl_password = ttk.Label(self.myframe, text = "Password:", font=("Helvetica", 20))
        self.entry_password = ttk.Entry(self.myframe, font = ("Arial", 30))
        self.btn_back = ttk.Button(self.myframe, text = "Back", command=self.back)

        self.lbl_username.pack(pady = 5)
        self.entry_username.pack()
        self.lbl_password.pack(pady = 5)
        self.entry_password.pack()
        self.lbl_complete_name.pack(pady = 5)
        self.entry_complete_name.pack()
        self.btn_back.pack(pady = 5)

        self.myframe.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        self.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    def back(self):
        self.destroy()

class about(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.lbl_about = ttk.Label(self, text = "   This is a POS System App\n\n               Created by:\n\n       Miler Lubid Bayangan\nFor Educational Purposes Only", anchor="center", font=("Helvetica", 20))
        self.lbl_about.pack(pady=10, expand=True, fill="both")


               