import tkinter as tk
from tkinter import ttk
import sqlite3

class Users(ttk.Frame):
    '''
    Add user frame
    '''
    def __init__(self, master):
        super().__init__(master)

        self.add_user = self.AddUser(self)
        self.user_list = self.UserList(self)

        self.pack(expand=True, fill="both")

    class AddUser(ttk.Frame):
        '''
        Add user frame
        '''
        def __init__(self, master):
            super().__init__(master)
            self.lbl_complete_name = ttk.Label(self, text = "Complete Name:",
                                                    font=("Helvetica", 20))
            self.lbl_complete_name.pack(pady = (10, 0))
            self.entry_complete_name = ttk.Entry(self, font = ("Arial", 30))
            self.entry_complete_name.pack()
            self.lbl_username = ttk.Label(self, text = "User Name:",
                                                font=("Helvetica", 20))
            self.lbl_username.pack(pady = (10, 0))
            self.entry_username = ttk.Entry(self, font = ("Arial", 30))
            self.entry_username.pack()
            self.lbl_password = ttk.Label(self, text = "Password:",
                                                font=("Helvetica", 20))
            self.lbl_password.pack(pady = (10, 0))
            self.entry_password = ttk.Entry(self, font = ("Arial", 30))
            self.entry_password.pack()

            self.lbl_error = ttk.Label(self, text = "")
            self.lbl_error.pack(pady=10)

            self.btn_add = ttk.Button(self, text = "Add", command=self.add_user)
            self.btn_add.pack(side="left", pady=10, expand=True)
            self.btn_clear = ttk.Button(self, text = "Clear", command=self.clear_entry)
            self.btn_clear.pack(side="left", pady=10, expand=True)

            self.pack(expand=True, fill="both", side="left", ipadx=10, ipady=10)

        def add_user(self):
            '''
            Add a new user to the database
            '''
            complete_name = self.entry_complete_name.get()
            username = self.entry_username.get()
            password = self.entry_password.get()
            if complete_name == "" or username == "" or password == "":
                self.lbl_error.config(text = "Please fill out all fields.", )
            else:
                conn = sqlite3.connect('file:posdb.db?mode=rw', uri=True)
                cursor = conn.cursor()
                try:
                    cursor.execute(f"INSERT INTO employees (username, complete_name, password) VALUES ('{self.entry_username.get()}', '{self.entry_complete_name.get()}', '{self.entry_password.get()}')")
                    conn.commit()
                    conn.close()
                    self.lbl_error.config(text = "User added successfully.")
                    self.clear_entry()

                # Need to catch IntegrityError and other error if possible
                except sqlite3.IntegrityError as err:
                # except sqlite3.IntegrityError:
                    # self.lbl_error.config(text = "User already exists.")
                    self.lbl_error.config(text = str(err))


        def clear_entry(self):
            '''
            Clear the entry fields
            '''
            self.entry_complete_name.delete(0, "end")
            self.entry_username.delete(0, "end")
            self.entry_password.delete(0, "end")
            self.lbl_error.config(text="")

    class UserList(ttk.Frame):
        '''
        Show list of users
        '''
        def __init__(self, master):
            super().__init__(master)

            self.tree = ttk.Treeview(master = self, columns = ("complete_name", "username"), show = "headings")
            self.tree.heading("username", text = "User Name")
            self.tree.heading("complete_name", text = "Complete Name")
            self.tree.pack(expand=True, fill="both")

            self.btn_delete = ttk.Button(self, text="Delete", command=self.delete_item)
            self.btn_delete.pack(pady=10, side="left", expand=True)
            self.btn_update = ttk.Button(self, text="Update", command=self.update_item)
            self.btn_update.pack(pady=10, side="left", expand=True)

            self.pack(expand=True, fill="both", side="left", ipadx=10, ipady=10)

        def delete_item(self):
            '''
            Delete item from table
            '''
            selected = self.tree.selection()
            for item in selected:
                self.tree.delete(item)

        def update_item(self):
            '''
            Update item in table
            '''
            pass

        def refresh_table(self):
            '''
            Refresh table
            '''
            pass