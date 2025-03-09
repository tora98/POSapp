import tkinter as tk
from tkinter import ttk
import datetime

class login(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
                
        self.myframe = ttk.Frame(self)

        self.lbl_username = ttk.Label(self.myframe, text = "User Name:")
        self.entry_username = ttk.Entry(self.myframe, font = ("Arial", 30))
        self.lbl_password = ttk.Label(self.myframe, text = "Password:")
        self.entry_password = ttk.Entry(self.myframe, font = ("Arial", 30)) 
        self.btn_login = ttk.Button(self.myframe, text = "Login", default="active", command=self.show_main)

        self.lbl_username.pack(pady = 5)
        self.entry_username.pack()
        self.lbl_password.pack(pady = 5)
        self.entry_password.pack()
        self.btn_login.pack(pady = 5, ipadx = 10, ipady = 5)

        self.myframe.place(width=600, height=400, relx=0.5, rely=0.5, anchor="center")

        self.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    def show_main(self):
        self.next_frame = main(self, self.entry_username.get())
        

class main(ttk.Frame):
    def __init__(self, master, user):
        super().__init__(master)

        self.user = user
        self.lbl_user = ttk.Label(self, text = self.user).place(relx=0, rely=0, relwidth=0.5, relheight=0.1)
        self.lbl_date = ttk.Label(self, text = "Date:", anchor="e").place(relx=0.5, rely=0, relwidth=0.5, relheight=0.1)

        self.frame1 = self.entry_frame(self)
        self.frame2 = self.table_frame(self)

        self.pack(expand=True, fill="both", ipadx=10, ipady=10)

    class entry_frame(ttk.Frame):
        def __init__(self, master):
            super().__init__(master)


            self.frame1 = ttk.Frame(self, border=1, relief="solid")
            self.lbl_item = ttk.Label(self.frame1, text = "Item Name:").pack()
            self.entry_item = ttk.Entry(self.frame1, font=("Helvetica", 30)).pack(pady=(0,5), padx=10, expand=True, fill="x")
            self.lbl_quantity = ttk.Label(self.frame1, text = "Quantity:").pack()
            self.entry_quantity = ttk.Entry(self.frame1, font=("Helvetica", 30)).pack(pady=(0,5), padx=10, expand=True, fill="x")
            self.lbl_price = ttk.Label(self.frame1, text = "Price:", font=("Helvetica", 20)).pack(pady=10, expand=True, fill="both")
            self.frame1.pack(expand=True, fill="both", ipadx=5)

            self.frame2 = ttk.Frame(self, border=1, relief="solid")
            self.btn_add = ttk.Button(self.frame2, text = "Add", command=self.add_item).pack(side="left", expand=True)
            self.btn_clear = ttk.Button(self.frame2, text = "Clear", command=self.clear_entry).pack(side="left", expand=True)
            self.frame2.pack(expand=True, fill="both", ipadx=5)

            self.place(relx=0, rely=0.1, relwidth=0.6, relheight=0.9)

        def add_item(self):
            pass

        def clear_entry(self):
            self.entry_item.delete(0, tk.END)
            self.entry_quantity.delete(0, tk.END)

    class table_frame(ttk.Frame):
        def __init__(self, master):
            super().__init__(master)

            self.columnconfigure(0, weight=1)
            self.rowconfigure(0, weight=1)

            self.tree = ttk.Treeview(self, columns=("item", "quantity", "price"), show="headings")
            self.tree.heading("item", text="Item Name")
            self.tree.heading("quantity", text="Quantity")
            self.tree.heading("price", text="Price")
            self.tree.pack(padx=10, pady=5, fill="y", expand=True)

            self.place(relx=0.6, rely=0.1, relwidth=0.4, relheight=0.9)

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




               