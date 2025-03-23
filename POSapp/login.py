'''
Application Frames
'''
import tkinter as tk
from tkinter import ttk
import datetime as dt
import sqlite3

from tabs import Tabs

class Login(ttk.Frame):
    '''
    Login Frame
    '''
    def __init__(self, master):
        super().__init__(master)
                
        #TODO: Add Validation for users

        self.myframe = ttk.Frame(self)

        self.lbl_username = ttk.Label(self.myframe, text = "User Name:", font=("Helvetica", 20))
        self.entry_username = ttk.Entry(self.myframe, font = ("Arial", 30))
        self.lbl_password = ttk.Label(self.myframe, text = "Password:", font=("Helvetica", 20))
        self.entry_password = ttk.Entry(self.myframe, font = ("Arial", 30)) 
        self.lbl_error = ttk.Label(self.myframe, text = "")
        self.btn_login = ttk.Button(self.myframe, text = "Login", default="active", command = self.show_tabs)

        self.lbl_username.pack(pady = 5)
        self.entry_username.pack()
        self.lbl_password.pack(pady = 5)
        self.entry_password.pack()
        self.lbl_error.pack(pady = 5)
        self.btn_login.pack(pady = 5, ipadx = 10, ipady = 5)

        self.entry_username.focus_set()
        self.entry_password.bind('<Return>', self.show_tabs)
        self.myframe.place(width=600, height=400, relx=0.5, rely=0.5, anchor="center")

        self.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    def show_tabs(self, event = None) -> None:
        """
        Replace the current frame with the tabs frame after successful login.

        :returns: None
        """
        #TODO: Validate users from database
        get_name = self.entry_username.get()
        get_password = self.entry_password.get()

        if get_name == "" or get_password == "":
            self.entry_username.focus_set()
            self.lbl_error.config(text = "Please fill out all fields.")
            return
        
        elif self.validate(get_name, get_password):
            Tabs(self, get_name)
            self.clear_entry()

        else:
            self.lbl_error.config(text = "Not a valid username or password.")

    def validate(self, get_name, get_password):
        conn = sqlite3.connect("posdb.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM employees WHERE username = '{get_name}' AND password = '{get_password}'")
        result = cursor.fetchall()
        if result:
            return True
        else:
            return False
               
    def clear_entry(self):
        self.entry_username.delete(0, "end")
        self.entry_password.delete(0, "end")
        self.lbl_error.config(text="")
