import tkinter as tk
from tkinter import ttk


class About(ttk.Frame):
    #Show information about the app

    def __init__(self, master):
        super().__init__(master)

        ttk.Label(
            self,
            text="This is a POS System App",
            anchor="center",
            font=("Helvetica", 20)).pack(pady=10, expand=True, fill="both")
        ttk.Label(
            self,
            text="Created by Tora98",
            anchor="center",
            font=("Helvetica", 20)).pack(pady=10, expand=True, fill="both")
        ttk.Label(
            self,
            text="For Educational Purposes!",
            anchor="center",
            font=("Helvetica", 20)).pack(pady=10, expand=True, fill="both")
