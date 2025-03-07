import tkinter as tk
from tkinter import ttk
import frames

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #initialize main window   
        self.title("Delles Agri-Poultry Supply")
        self.geometry("1000x600")
        self.minsize(1000,600)

        #add frame segments to window
        # self.sales = Sales(self)
        # self.table = Table(self)
        # self.buttons = Buttons(self, self.sales)
        self.current_frame = frames.Login(self)
        
        #run the mainloop
        self.mainloop()

#call the app to run
if __name__ == "__main__":
    Application()