'''
Application Frames
'''
from tkinter import ttk
import datetime as dt
import sqlite3

from ttkwidgets.autocomplete import AutocompleteCombobox

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
        #TODO: Bind Enter key
        self.btn_login.bind("<Return>")

        self.myframe.place(width=600, height=400, relx=0.5, rely=0.5, anchor="center")

        self.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    def show_tabs(self) -> None:
        """
        Replace the current frame with the tabs frame after successful login.

        :returns: None
        """
        #TODO: Validate users from database
        if self.entry_username.get() == "" or self.entry_password.get() == "":
            self.entry_username.focus_set()
            self.lbl_error.config(text = "Please fill out all fields.")
            return
        
        elif self.entry_username.get() == "Administrator" and self.entry_password.get() == "p@ssw0rd":
            user_name = self.entry_username.get()
            Tabs(self, user_name)

        else:
            self.lbl_error.config(text = "Not a valid username or password.")

class Tabs(ttk.Notebook):
    '''
    Tabs for navigation
    '''
    def __init__(self, master, user):
        super().__init__(master)    

        if user == "Administrator":
            self.maintab = Main(self, user)
            self.productstab = Products(self)
            self.addproductstab = AddProducts(self)
            self.adduserstab = Users(self)
            self.abouttab = About(self)
            self.settingstab = Settings(self)
            self.add(self.maintab, text="Daily Sales")
            self.add(self.productstab, text="Products List")
            self.add(self.addproductstab, text="Add Products")
            self.add(self.adduserstab, text = "Users")
            self.add(self.abouttab, text="About") 
            self.add(self.settingstab, text="Settings")  

        else:
            self.maintab = Main(self, user)
            self.productstab = Products(self)
            self.settingstab = Settings(self)
            self.add(self.maintab, text="Daily Sales")
            self.add(self.productstab, text="Products List")

        self.pack(expand=True, fill="both") 

class Main(ttk.Frame):
    def __init__(self, master, user):
        super().__init__(master)

        self.frame1 = self.NavFrame(self, user)
        self.frame2 = self.EntryFrame(self)
        self.frame3 = self.TableFrame(self)

        self.pack(expand=True, fill="both", ipadx=10, ipady=10)

    class NavFrame(ttk.Frame):
        '''
        Frame for navigation
        '''
        def __init__(self, master, user):
            super().__init__(master)

            self.user = user
            self.date = dt.datetime.now()

            self.lbl_user = ttk.Label(self, text = self.user, font=("Helvetica", 20), anchor="w")
            self.lbl_user.pack(side="left", expand=True, fill="x")
            self.lbl_date = ttk.Label(self, text = f"{self.date:%A, %B %d %Y}", font=("Helvetica", 20), anchor="e")
            self.lbl_date.pack(side="left", expand=True, fill="x")

            self.pack(fill="x")

    class EntryFrame(ttk.Frame):
        '''
        Frame for adding sales
        '''
        def __init__(self, master):
            super().__init__(master)

            self.f1 = self.Frame1(self)

            self.config(border=1, relief="solid")

            self.pack(side="left", expand=True, fill="both")

        class Frame1(ttk.Frame):
            '''
            Frame for adding sales
            '''
            def __init__(self, master):
                super().__init__(master)       

                self.style = ttk.Style()
                self.style.configure("TButton", font=("Helvetica", 15))

                self.lbl_item = ttk.Label(self, text = "Item Name:", font=("Helvetica", 20))
                self.lbl_item.pack(pady=(10,0))
                self.combo_item = AutocompleteCombobox(self, font=("Helvetica", 30), completevalues=self.insert_values())
                self.combo_item.pack(pady=(0,10), padx=10, expand=True, fill="x")
                self.lbl_quantity = ttk.Label(self, text = "Quantity:", font=("Helvetica", 20))
                self.lbl_quantity.pack(pady=(5,0))
                self.spinbox_quantity = ttk.Spinbox(self, font=("Helvetica", 30), values=(range(1, 100)))
                self.spinbox_quantity.pack(pady=(0,10), padx=10, expand=True, fill="x")
                self.lbl_price = ttk.Label(self, text = "Price:", font=("Helvetica", 20))
                self.lbl_price.pack(expand=True, fill="x")
                self.lbl_value = ttk.Label(self, text="0.00", font=("Helvetica", 30), anchor="center")
                self.lbl_value.pack(pady=(0, 10), expand=True, fill="both")

                self.btn_add = ttk.Button(self, text = "Add", command=self.add_sale)
                self.btn_add.pack(pady=10, side="left", expand=True)
                self.btn_clear = ttk.Button(self, text = "Clear", command=self.clear_entry)
                self.btn_clear.pack(pady=10, side="left", expand=True)
                self.pack(expand=True, fill="both", ipadx=5)

            def insert_values(self):
                '''
                Insert values to combobox
                '''
                product_list = []
                conn = sqlite3.connect("posdb.db")
                cursor = conn.cursor()
                cursor.execute("SELECT manufacturer, product_name FROM products")
                rows = cursor.fetchall()

                for row in rows:
                    item = (f"{row[0]} - {row[1]}")
                    product_list.append(item)

                return product_list

            def add_sale(self):
                '''
                Add sale to database
                '''
                date = dt.datetime.now()
                user = self.master.master.user
                item_name = self.master.combo_item.get()
                item_quantity = self.master.entry_quantity.get()
                try: 
                    conn = sqlite3.connect("posdb.db")
                    cursor = conn.cursor()
                    cursor.execute(f"INSERT INTO sales (date, product_id, quantity, total_price, user_id) VALUES (?, ?, ?, ?, ?), ({date}, {item_name}, {item_quantity}, {user})")
                    conn.commit()
                except sqlite3.IntegrityError as err:
                    print(err)
                finally:
                    conn.close()

            def clear_entry(self):
                '''
                Clear entry fields
                '''
                self.combo_item.delete(0, "end")
                self.spinbox_quantity.delete(0, "end")

    class TableFrame(ttk.Frame):
        '''
        Frame for table
        '''
        def __init__(self, master):
            super().__init__(master)

            #TODO: Add a scroll bar to tree view
            #TODO: Add Table Values

            self.tree = ttk.Treeview(self, columns=("item", "quantity", "price"), show="headings")
            self.tree.column("item", stretch=True, anchor="w")
            self.tree.heading("item", text="Item Name")
            self.tree.column("quantity", width=60, anchor="e")
            self.tree.heading("quantity", text="Quantity")
            self.tree.column("price", width=100, anchor="e", stretch=True)
            self.tree.heading("price", text="Price")
            self.tree.pack(padx= (5, 0), expand=True, fill="both")

            self.btn_delete = ttk.Button(self, text="Delete", command=self.delete_item)
            self.btn_delete.pack(pady=10, side="left", expand=True)
            self.btn_update = ttk.Button(self, text="Update", command=self.update_item)
            self.btn_update.pack(pady=10, side="left", expand=True)

            self.pack(side="left", expand=True, fill="both")

        def delete_item(self):
            '''
            Delete item from table
            '''
            selected = self.tree.selection()
            for item in selected:
                self.tree.delete(item)

        def update_item(self):
            '''
            Update item in table
            '''
            pass

        def refresh_table(self):
            '''
            Refresh table
            '''
            pass

            #TODO: Logic for Delete Function
            #TODO: Logic for Update Function

class Products(ttk.Frame):
    '''
    Frame for products
    '''
    def __init__(self, master) -> None:
        super().__init__(master)

        #TODO: Add scrollbar to treeview 
        #TODO: Logic for Delete Function 
        #TODO: Logic for Update Function 

        self.tree = ttk.Treeview(master = self, columns=("product_id", "product_name", "manufacturer", "packaging_units", "price_per_unit"), show="headings")
        self.tree.column("product_id", width=0) 
        self.tree.heading("product_id", text="ID")
        self.tree.column("product_name", width=200)
        self.tree.heading("product_name", text="Product Name")
        self.tree.column("manufacturer", width=200)
        self.tree.heading("manufacturer", text="Manufacturer")
        self.tree.column("packaging_units", width=200)
        self.tree.heading("packaging_units", text="Packaging Units")
        self.tree.column("price_per_unit", width=200)
        self.tree.heading("price_per_unit", text="Price Per Unit")
        self.tree.pack(expand=True, fill="both")

        self.refresh_table()

        self.btn_refresh = ttk.Button(self, text = "Refresh", command=self.refresh_table)
        self.btn_refresh.pack(side="left", pady=10, expand=True)
        self.btn_update = ttk.Button(self, text = "Update", command=self.update_product)
        self.btn_update.pack(side="left", pady=10, expand=True)
        self.btn_delete = ttk.Button(self, text = "Delete", command=self.delete_product)
        self.btn_delete.pack(side="left", pady=10, expand=True)

        self.pack(expand=True, fill="both", ipadx=10, ipady=10)

    def refresh_table(self) -> None:
        '''
        Refreshes the table
        '''
        self.tree.delete(*self.tree.get_children())
        conn = sqlite3.connect("posdb.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)
        conn.close()

    def update_product(self):
        '''
        Updates a product in the database
        '''
        product_name = self.tree.item(self.tree.selection())['values'][1]
        manufacturer = self.tree.item(self.tree.selection())['values'][2]
        packaging_units = self.tree.item(self.tree.selection())['values'][3]
        price_per_unit = self.tree.item(self.tree.selection())['values'][4]
        conn = sqlite3.connect("posdb.db")
        cursor = conn.cursor()
        cursor.execute(f'''UPDATE products SET 
                                product_name = '{self.tree.item(self.tree.selection())['values'][1]}', 
                                manufacturer = '{self.tree.item(self.tree.selection())['values'][2]}', 
                                packaging_units = '{self.tree.item(self.tree.selection())['values'][3]}', 
                                price_per_unit = '{self.tree.item(self.tree.selection())['values'][4]}' 
                                WHERE product_id = {self.tree.item(self.tree.selection())['values'][0]}''')
        conn.commit()
        conn.close()
        self.refresh_table()

    def delete_product(self):
        '''
        Deletes a product from the database
        '''
        selected_item = self.tree.item(self.tree.selection())
        conn = sqlite3.connect("posdb.db")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM products WHERE product_id = {selected_item['values'][0]}")
        conn.commit()
        conn.close()
        self.refresh_table()

class AddProducts(ttk.Frame):
    '''
    Frame for adding new products
    '''
    def __init__(self, master):
        super().__init__(master)

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 15))

        self.lbl_product_name = ttk.Label(self, text = "Product Name:", font=("Helvetica", 20))
        self.lbl_product_name.pack(pady =(10,0))
        self.entry_product_name = ttk.Entry(self, font = ("Arial", 30))
        self.entry_product_name.pack(pady =(0, 10))
        self.lbl_manufacturer = ttk.Label(self, text = "Manufacturer:", font=("Helvetica", 20))
        self.lbl_manufacturer.pack(pady =(10,0))
        self.entry_manufacturer = ttk.Entry(self, font = ("Arial", 30))
        self.entry_manufacturer.pack(pady =(0, 10))
        self.lbl_packaging_units = ttk.Label(self, text = "Packaging Units (Number of kilos or pieces per Bag/Box/Bottle):", font=("Helvetica", 10))
        self.lbl_packaging_units.pack(pady =(10,0))
        self.entry_packaging_units = ttk.Entry(self, font = ("Arial", 30))
        self.entry_packaging_units.pack(pady =(0, 10))
        self.lbl_price_per_unit = ttk.Label(self, text = "Price Per Unit:", font=("Helvetica", 20))
        self.lbl_price_per_unit.pack(pady =(10,0))
        self.entry_price_per_unit = ttk.Entry(self, font = ("Arial", 30))
        self.entry_price_per_unit.pack(pady =(0, 10))

        self.lbl_error = ttk.Label(self, text = "", foreground="red", font=("Helvetica", 10))
        self.lbl_error.pack(pady=10)

        self.btn_add = ttk.Button(self, text = "Add", command=self.add_product)
        self.btn_add.pack(side="left", pady=10, expand=True)
        self.btn_clear = ttk.Button(self, text = "Clear", command=self.clear_entry)
        self.btn_clear.pack(side="left", pady=10, expand=True) 

        self.pack(expand=True, fill="both", ipadx=10, ipady=10)

    def add_product(self):
        '''
        Add a product to the database
        '''
        if self.entry_product_name.get() == "" or self.entry_manufacturer.get() == "" or self.entry_packaging_units.get() == "" or self.entry_price_per_unit.get() == "":
            self.lbl_error.config(text = "Please fill out all fields.")
        else:
            conn = sqlite3.connect("posdb.db")
            cursor = conn.cursor()
            try:
                product_name = self.entry_product_name.get()
                manufacturer = self.entry_manufacturer.get()
                packaging_units = self.entry_packaging_units.get()
                price_per_unit = self.entry_price_per_unit.get()
                cursor.execute(f"INSERT INTO products (product_name, manufacturer, packaging_units, price_per_unit) VALUES ('{product_name}', '{manufacturer}', '{packaging_units}', '{price_per_unit}')")
                conn.commit()
                conn.close()
                self.lbl_error.config(text = "Product added successfully.")
                self.clear_entry()

            except sqlite3.IntegrityError as err:
                self.lbl_error.config(text = str(err))
                

    def clear_entry(self):
        '''
        Clear the entry fields    
        '''
        self.entry_product_name.delete(0, "end")
        self.entry_manufacturer.delete(0, "end")
        self.entry_packaging_units.delete(0, "end")
        self.entry_price_per_unit.delete(0, "end")
        self.lbl_error.config(text="")

class Users(ttk.Frame):
    '''
    Add user frame
    '''
    def __init__(self, master):
        super().__init__(master)

        self.add_user = self.AddUser(self)
        self.user_list = self.UserList(self)

        self.pack(expand=True, fill="both")

    class AddUser(ttk.Frame):
        '''
        Add user frame
        '''
        def __init__(self, master):
            super().__init__(master)
            self.lbl_complete_name = ttk.Label(self, text = "Complete Name:",
                                                    font=("Helvetica", 20))
            self.lbl_complete_name.pack(pady = (10, 0))
            self.entry_complete_name = ttk.Entry(self, font = ("Arial", 30))
            self.entry_complete_name.pack()
            self.lbl_username = ttk.Label(self, text = "User Name:",
                                                font=("Helvetica", 20))
            self.lbl_username.pack(pady = (10, 0))
            self.entry_username = ttk.Entry(self, font = ("Arial", 30))
            self.entry_username.pack()
            self.lbl_password = ttk.Label(self, text = "Password:",
                                                font=("Helvetica", 20))
            self.lbl_password.pack(pady = (10, 0))
            self.entry_password = ttk.Entry(self, font = ("Arial", 30))
            self.entry_password.pack()

            self.lbl_error = ttk.Label(self, text = "")
            self.lbl_error.pack(pady=10)

            self.btn_add = ttk.Button(self, text = "Add", command=self.add_user)
            self.btn_add.pack(side="left", pady=10, expand=True)
            self.btn_clear = ttk.Button(self, text = "Clear", command=self.clear_entry)
            self.btn_clear.pack(side="left", pady=10, expand=True)

            self.pack(expand=True, fill="both", side="left", ipadx=10, ipady=10)

        def add_user(self):
            '''
            Add a new user to the database
            '''
            complete_name = self.entry_complete_name.get()
            username = self.entry_username.get()
            password = self.entry_password.get()
            if complete_name == "" or username == "" or password == "":
                self.lbl_error.config(text = "Please fill out all fields.", )
            else:
                conn = sqlite3.connect("posdb.db")
                cursor = conn.cursor()
                try:
                    cursor.execute(f"INSERT INTO employees (username, complete_name, password) VALUES ('{self.entry_username.get()}', '{self.entry_complete_name.get()}', '{self.entry_password.get()}')")
                    conn.commit()
                    conn.close()
                    self.lbl_error.config(text = "User added successfully.")
                    self.clear_entry()

                # Need to catch IntegrityError and other error if possible
                except sqlite3.IntegrityError as err:
                # except sqlite3.IntegrityError:
                    # self.lbl_error.config(text = "User already exists.")
                    self.lbl_error.config(text = str(err))


        def clear_entry(self):
            '''
            Clear the entry fields
            '''
            self.entry_complete_name.delete(0, "end")
            self.entry_username.delete(0, "end")
            self.entry_password.delete(0, "end")
            self.lbl_error.config(text="")

    class UserList(ttk.Frame):
        '''
        Show list of users
        '''
        def __init__(self, master):
            super().__init__(master)

            self.tree = ttk.Treeview(master = self, columns = ("complete_name", "username"), show = "headings")
            self.tree.heading("username", text = "User Name")
            self.tree.heading("complete_name", text = "Complete Name")
            self.tree.pack(expand=True, fill="both")

            self.btn_delete = ttk.Button(self, text="Delete", command=self.delete_item)
            self.btn_delete.pack(pady=10, side="left", expand=True)
            self.btn_update = ttk.Button(self, text="Update", command=self.update_item)
            self.btn_update.pack(pady=10, side="left", expand=True)

            self.pack(expand=True, fill="both", side="left", ipadx=10, ipady=10)

        def delete_item(self):
            '''
            Delete item from table
            '''
            selected = self.tree.selection()
            for item in selected:
                self.tree.delete(item)

        def update_item(self):
            '''
            Update item in table
            '''
            pass

        def refresh_table(self):
            '''
            Refresh table
            '''
            pass

class About(ttk.Frame):
    '''
    Show information about the app
    '''
    def __init__(self, master):
        super().__init__(master)

        self.lbl_about = ttk.Label(self, text = "   This is a POS System App\n\n               Created by:\n\n       Miler Lubid Bayangan\nFor Educational Purposes Only", anchor="center", font=("Helvetica", 20))
        self.lbl_about.pack(pady=10, expand=True, fill="both")

class Settings(ttk.Frame):
    '''
    Settings frame that include logging out
    '''
    def __init__(self, master):
        super().__init__(master)

        self.btn_logout = ttk.Button(self, text = "Logout", command=self.logout)
        self.btn_logout.pack(side="left", pady=10, expand=True)

        self.pack(expand=True, fill="both", side="left", ipadx=10, ipady=10)

    def logout(self):
        '''
        Log out the user
        '''
        self.master.destroy()
               
