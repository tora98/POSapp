import tkinter as tk
from tkinter import ttk


class About(ttk.Frame):
    '''
    Show information about the app
    '''

    def __init__(self, master):
        super().__init__(master)

        self.lbl_about = ttk.Label(
            self,
            text="   This is a POS System App\n\n               Created by:\n\n       Miler Lubid Bayangan\nFor Educational Purposes Only",
            anchor="center",
            font=("Helvetica", 20)
            )
        self.lbl_about.pack(pady=10, expand=True, fill="both")
