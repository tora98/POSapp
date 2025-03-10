import tkinter as tk
from tkinter import ttk
import datetime as dt
import sqlite3

class login(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
                
        self.myframe = ttk.Frame(self)

        self.lbl_username = ttk.Label(self.myframe, text = "User Name:")
        self.entry_username = ttk.Entry(self.myframe, font = ("Arial", 30))
        self.lbl_password = ttk.Label(self.myframe, text = "Password:")
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
        self.abouttab = about(self)
        self.add(self.maintab, text="Daily Sales")
        self.add(ttk.Frame(self), text="Weekly Sales")
        self.add(self.abouttab, text="About")   

        self.pack(expand=True, fill="both") 

class main(ttk.Frame):
    def __init__(self, master, user):
        super().__init__(master)

        self.date = dt.datetime.now()
        self.user = user
        self.lbl_user = ttk.Label(self, text = self.user).place(relx=0, rely=0, relwidth=0.5, relheight=0.1)
        self.lbl_date = ttk.Label(self, text = f"{self.date:%A, %B %d %Y}", anchor="e").place(relx=0.5, rely=0, relwidth=0.5, relheight=0.1)

        self.frame1 = self.entry_frame(self)
        self.frame2 = self.table_frame(self)

        self.pack(expand=True, fill="both", ipadx=10, ipady=10)

    class entry_frame(ttk.Frame):
        def __init__(self, master):
            super().__init__(master)

            self.f1 = self.frame1(self)

            self.config(border=1, relief="solid")

            self.place(relx=0.01, rely=0.11, relwidth=0.58, relheight=0.88)

        class frame1(ttk.Frame):
            def __init__(self, master):
                super().__init__(master)

                self.style = ttk.Style()
                self.style.configure("TButton", font=("Helvetica", 15))

                self.lbl_item = ttk.Label(self, text = "Item Name:")
                self.lbl_item.pack(pady=(5,0))
                self.combo_item = ttk.Combobox(self, font=("Helvetica", 30))
                self.combo_item.pack(pady=(0,5), padx=10, expand=True, fill="x")
                self.lbl_quantity = ttk.Label(self, text = "Quantity:")
                self.lbl_quantity.pack(pady=(5,0))
                self.entry_quantity = ttk.Entry(self, font=("Helvetica", 30))
                self.entry_quantity.pack(pady=(0,5), padx=10, expand=True, fill="x")
                self.lbl_price = ttk.Label(self, text = "Price:", font=("Helvetica", 20))
                self.lbl_price.pack(pady=10, expand=True, fill="both")

                self.btn_add = ttk.Button(self, text = "Add", command=self.add_sale).pack(pady=10, side="left", expand=True)
                self.btn_clear = ttk.Button(self, text = "Clear", command=self.clear_entry).pack(pady=10, side="left", expand=True)
                self.pack(expand=True, fill="both", ipadx=5)

            def add_sale(self):
                pass
                # conn = sqlite3.connect("posdb.db")
                # cursor = conn.cursor()
                # cursor.execute(f"INSERT INTO sales (date, product_id, quantity, total_price, user_id) VALUES (?, ?, ?, ?, ?), ({self.master.master.date}, {self.master.combo_item.get()}, {self.master.entry_quantity.get()}, {self.master.master.user})")
                # conn.commit()
                # conn.close()

            def clear_entry(self):
                self.combo_item.delete(0, "end")
                self.entry_quantity.delete(0, "end")

    class table_frame(ttk.Frame):
        def __init__(self, master):
            super().__init__(master)

            self.tree = ttk.Treeview(self, columns=("item", "quantity", "price"), show="headings")
            self.tree.column("item", stretch=True, anchor="w")
            self.tree.heading("item", text="Item Name", )
            self.tree.column("quantity", width=60, anchor="e")
            self.tree.heading("quantity", text="Quantity")
            self.tree.column("price", width=100, anchor="e", stretch=True)
            self.tree.heading("price", text="Price")
            self.tree.pack(padx=(0,10), pady=5, fill="y", expand=True)

            self.place(relx=0.6, rely=0.1, relwidth=0.4, relheight=0.9)

class products(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.pack()

class add_products(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)


        self.pack()

class add_user(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)


        self.myframe = ttk.Frame(self, bg="light blue")

        self.lbl_complete_name = ttk.Label(self.myframe, text = "Complete Name:")	
        self.entry_complete_name = ttk.Entry(self.myframe, font = ("Arial", 30))
        self.lbl_username = ttk.Label(self.myframe, text = "User Name:")
        self.entry_username = ttk.Entry(self.myframe, font = ("Arial", 30))
        self.lbl_password = ttk.Label(self.myframe, text = "Password:")
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

        self.lbl_about = ttk.Label(self, text = "   This is a POS System App\n\n               Created by:\n\n       Miler Lubid Bayangan\nFor Educational Purposes Only", anchor="center")
        self.lbl_about.pack(pady=10, expand=True, fill="both")


               