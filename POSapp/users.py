import tkinter as tk
from tkinter import ttk
import sqlite3
import argon2

DATABASE = 'file:posdb.db?mode=rw'


class Users(ttk.Frame):
    '''
    Add user frame
    '''

    def __init__(self, master):
        super().__init__(master)

        self.add_user = AddUser(self)
        self.user_list = UserList(self)

        self.pack(expand=True, fill="both")


class AddUser(ttk.Frame):
    '''
    Add user frame
    '''

    def __init__(self, master):
        super().__init__(master)
        self.lbl_complete_name = ttk.Label(self, text="Complete Name:", font=("Helvetica", 20))
        self.lbl_complete_name.pack(pady=(10, 0))
        self.entry_complete_name = ttk.Entry(self, font=("Arial", 30))
        self.entry_complete_name.pack()
        self.lbl_username = ttk.Label(self, text="User Name:", font=("Helvetica", 20))
        self.lbl_username.pack(pady=(10, 0))
        self.entry_username = ttk.Entry(self, font=("Arial", 30))
        self.entry_username.pack()
        self.lbl_password = ttk.Label(self, text="Password:", font=("Helvetica", 20))
        self.lbl_password.pack(pady=(10, 0))
        self.entry_password = ttk.Entry(self, font=("Arial", 30))
        self.entry_password.pack()
        self.lbl_error = ttk.Label(self, text="")
        self.lbl_error.pack(pady=10)
        self.btn_add = ttk.Button(self, text="Add", command=self.add_user)
        self.btn_add.pack(side="left", pady=10, expand=True)
        self.btn_add.bind("<Return>", self.add_user)
        self.btn_clear = ttk.Button(self, text="Clear", command=self.clear_entry)
        self.btn_clear.pack(side="left", pady=10, expand=True)
        self.pack(expand=True, fill="both", side="left", ipadx=10, ipady=10)

    def add_user(self, event=None):
        '''
        Add a new user to the database
        '''
        complete_name = self.entry_complete_name.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        if complete_name == "" or username == "" or password == "":
            self.lbl_error.config(text="Please fill out all fields.")
        else:
            hasher = argon2.PasswordHasher()
            key = hasher.hash(password)
            conn = sqlite3.connect(DATABASE, uri=True)
            cursor = conn.cursor()
            try:
                cursor.execute(f'''INSERT INTO employees (
                    username,
                    complete_name,
                    salt,
                    password)
                    VALUES (
                    '{self.entry_username.get()}',
                    '{self.entry_complete_name.get()}',
                    '{key}'
                    )
                ''')
                conn.commit()
                conn.close()
                self.lbl_error.config(text="User added successfully.")
                self.clear_entry()
            except sqlite3.IntegrityError as err:
                self.lbl_error.config(text=str(err))

    def clear_entry(self):
        '''
        Clear the entry fields
        '''
        self.entry_complete_name.delete(0, "end")
        self.entry_username.delete(0, "end")
        self.entry_password.delete(0, "end")
        self.lbl_error.config(text="")
        self.entry_complete_name.focus_set()

class UserList(ttk.Frame):
    '''
    Show list of users
    '''

    def __init__(self, master):
        super().__init__(master)
        self.tree = ttk.Treeview(self, columns=("complete_name", "username"), show="headings")
        self.tree.heading("username", text="User Name")
        self.tree.heading("complete_name", text="Complete Name")
        self.tree.pack(expand=True, fill="both")
        self.refresh_table()
        self.btn_delete = ttk.Button(self, text="Delete", command=self.delete_item)
        self.btn_delete.pack(pady=10, side="left", expand=True)
        self.btn_refresh = ttk.Button(self, text="Referesh", command=self.refresh_table)
        self.btn_refresh.pack(pady=10, side="left", expand=True)
        self.pack(expand=True, fill="both", side="left", ipadx=10, ipady=10)

    def delete_item(self):
        '''
        Delete item from table
        '''
        selected = self.tree.selection()
        selected_cname = self.tree.item(selected[0], "values")
        username = selected_cname[1]
        conn = sqlite3.connect('file:posdb.db?mode=rw', uri=True)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM employees WHERE username = '{username}'")
        conn.commit()
        conn.close()
        self.refresh_table()

    def update_item(self):
        '''
        Update item in table
        '''
        pass

    def refresh_table(self):
        '''
        Refresh table
        '''
        self.tree.delete(*self.tree.get_children())
        conn = sqlite3.connect(DATABASE, uri=True)
        cursor = conn.cursor()
        cursor.execute("SELECT username, complete_name FROM employees")
        rows = cursor.fetchall()
        for row in rows:
            username = row[0]
            complete_name = row[1]
            self.tree.insert("", "end", values=(complete_name, username))
        conn.close()
