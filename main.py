import tkinter as tk

from internal import login
from internal.database import my_database


class Application(tk.Tk):
    #Main Application class
    def __init__(self) -> None:
        super().__init__()
        self.title("Delles Agri-Poultry Supply")
        self.geometry("1000x600")
        self.minsize(1000, 600)
        self.state("normal")
        self.current_frame = login.Login(self)
        self.mainloop()


if __name__ == "__main__":
    # Create or Check if Datbase Exists
    my_database.create_database()
    # initialize the app
    app: Application = Application()
