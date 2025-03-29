'''
Main application class
'''

# tandard Library Import
import tkinter as tk

# Local Library Import
from login import Login
import my_database


class Application(tk.Tk):
    '''
    Main application class
    '''

    def __init__(self) -> None:
        super().__init__()
        # initialize main window
        self.title("Delles Agri-Poultry Supply")
        self.geometry("1000x600")
        self.minsize(1000,600)
        self.state("zoomed")

        # add frame segments to window
        self.current_frame: Login = Login(master = self)
        # run the mainloop
        self.mainloop()

# call the app to run


if __name__ == "__main__":
    # Create or Check if Datbase Exists
    my_database.create_database()
    # initialize the app
    my_app: Application = Application()
