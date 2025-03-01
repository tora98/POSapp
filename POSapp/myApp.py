import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #initialize main window   
        self.title("Delles Agri-Poultry Supply")
        self.geometry("1000x600")
        self.minsize(1000,600)

        #add frame segments to window
        self.sales = Sales(self)
        self.table = Table(self)
        self.buttons = Buttons(self, self.sales)
        
        #run the mainloop
        self.mainloop()

class Sales(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #set up the frame
        self.columnconfigure((0,1,2,3), weight=1, uniform="a")
        self.rowconfigure((0,1), weight=1, uniform="a")

        #make price variable
        self.price = 0.00

        #create widgets
        self.item_entry = ttk.Entry(self, font="Arial, 40")
        self.lblquantity = ttk.Label(self, text= "Quantity:", font=("Arial", 30))
        self.qty_entry = ttk.Entry(self, font="Arial, 40")
        self.lbl_price = ttk.Label(self, text="Price:", font=("Arial", 30))
        self.lblamount = ttk.Label(self, text=f"Php {self.price}", font="Arial, 30", background="green")

        #place the widgets
        self.item_entry.grid(column=0, rows=1, columnspan=4, sticky="nsew")
        self.lblquantity.grid(column=0, row=1)
        self.qty_entry.grid(column=1, row=1, sticky="nsew")
        self.lbl_price.grid(column=2, row=1)
        self.lblamount.grid(column=3, row=1, sticky="nsew")

        #place frame/self to the parent window
        self.place(x=0, y=0, relheight=0.2, relwidth=1)

    def add_items(self):
            pass

    def clear(self):
            self.item_entry.delete(0, tk.END)
            self.qty_entry.delete(0, tk.END)
class Table(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        #create widgets
        label = ttk.Label(self, text="row 2", background="Red")

        #place widgets to frame/self
        label.pack(expand=True, fill="both")

        #place frame/self to parent window
        self.place(relx=0, rely=0.2, relheight=0.8, relwidth=1)


class Buttons(tk.Frame):
    def __init__(self, parent, entry_frame):
        super().__init__(parent)

        #set up grids
        self.columnconfigure((0,1), weight=1)
        self.rowconfigure(0, weight=1)

        #create widgets
        btnadd = ttk.Button(self, text="Add", command=entry_frame.add_items)
        btnclear = ttk.Button(self, text="Clear", command=entry_frame.clear)

        #place widgets to frame/self
        btnadd.grid(column=0, row=0)
        btnclear.grid(column=1, row=0)

        #place frame/self to parent window
        self.place(relx=0, rely=0.9, relheight=0.1, relwidth=1)

#call the app to run
if __name__ == "__main__":
    Application()