from tkinter import ttk

from window import Window
from products import Products
from users import Users
from about import About
from settings import Settings


class Tabs(ttk.Notebook):
    '''
    Tabs for navigation
    '''

    def __init__(self, master, user):
        super().__init__(master)

        if user == "Admin":
            self.maintab = Window(self, user)
            self.productstab = Products(self)
            self.adduserstab = Users(self)
            self.abouttab = About(self)
            self.settingstab = Settings(self)
            self.add(self.maintab, text="Daily Sales")
            self.add(self.productstab, text="Products")
            self.add(self.adduserstab, text="Users")
            self.add(self.abouttab, text="About")
            self.add(self.settingstab, text="Settings")

        else:
            self.maintab = Window(self, user)
            self.productstab = Products(self)
            self.settingstab = Settings(self)
            self.add(self.maintab, text="Daily Sales")
            self.add(self.productstab, text="Products List")

        self.pack(expand=True, fill="both")
