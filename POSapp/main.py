
import sqlite3
import datetime as dt
from tkinter import ttk

from ttkwidgets.autocomplete import AutocompleteCombobox

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

            self.f1 = self.SalesFrame(self)

            self.config(border=1, relief="solid")

            self.pack(side="left", expand=True, fill="both")

        class SalesFrame(ttk.Frame):
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
                get_item_name = self.master.combo_item.get()
                get_item_quantity = self.master.entry_quantity.get()
                try: 
                    conn = sqlite3.connect("posdb.db")
                    cursor = conn.cursor()
                    cursor.execute(f"INSERT INTO sales (date, product_id, quantity, total_price, user_id) VALUES (?, ?, ?, ?, ?), ({date}, {get_item_name}, {get_item_quantity}, {user})")
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
            self.btn_refresh = ttk.Button(self, text="Refresh", command=self.refresh_table)
            self.btn_refresh.pack(pady=10, side="left", expand=True)

            self.pack(side="left", expand=True, fill="both")

        def delete_item(self):
            '''
            Delete item from table
            '''
            selected = self.tree.selection()
            for item in selected:
                self.tree.delete(item)

        def refresh_table(self):
            '''
            Refresh table
            '''
            self.tree.delete(*self.tree.get_children())
            conn = sqlite3.connect("posdb.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sales")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
            conn.close()
