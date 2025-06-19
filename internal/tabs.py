from tkinter import ttk

from internal import (
    products,
    sales,
    products,
    users,
    about,
    settings
)

class Tabs(ttk.Notebook):
    '''
    Tabs for navigation
    '''

    def __init__(self, master, user):
        super().__init__(master)
        if user != "Admin":
            self.maintab = sales.Window(self, user)
            self.productstab = products.Products(self)
            self.abouttab = about.About(self)
            self.settingstab = settings.Settings(self)
            self.add(self.maintab, text="Daily Sales")
            self.add(self.productstab, text="Products List")
            self.add(self.abouttab, text="About")
            self.add(self.settingstab, text="Settings")
        else:
            self.maintab = sales.Window(self, user)
            self.productstab = products.Products(self)
            self.adduserstab = users.Users(self)
            self.abouttab = about.About(self)
            self.settingstab = settings.Settings(self)
            self.add(self.maintab, text="Daily Sales")
            self.add(self.productstab, text="Products")
            self.add(self.adduserstab, text="Users")
            self.add(self.abouttab, text="About")
            self.add(self.settingstab, text="Settings")

        self.pack(expand=True, fill="both")
