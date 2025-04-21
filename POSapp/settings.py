from tkinter import ttk


class Settings(ttk.Frame):
    '''
    Settings frame that include logging out
    '''

    def __init__(self, master):
        super().__init__(master)

        self.btn_logout = ttk.Button(self, text="Logout", command=self.logout)
        self.btn_logout.pack(side="left", pady=10, expand=True)

        self.pack(expand=True, fill="both", side="left", ipadx=10, ipady=10)

    def logout(self):
        '''
        Log out the user
        '''
        self.master.destroy()
