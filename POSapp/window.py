# TODO: Edit refresh table to function properly
import sqlite3
import datetime as dt
from tkinter import ttk, messagebox

from ttkwidgets.autocomplete import AutocompleteCombobox

DATABASE = "file:posdb.db?mode=rw"


class Window(ttk.Frame):
    """Main Frame after login"""

    def __init__(self, master, user):
        super().__init__(master)

        self.user = user

        self.frame1 = self.NavFrame(self, user)
        self.frame2 = self.EntryFrame(self)
        self.frame3 = self.TableFrame(self)

        self.pack(expand=True, fill="both", ipadx=10, ipady=10)

    class NavFrame(ttk.Frame):
        # Frame for Header

        def __init__(self, master, user):
            super().__init__(master)

            self.user = user
            self.date = dt.datetime.now()

            self.lbl_user = ttk.Label(
                self, text=self.user, font=("Helvetica", 20), anchor="w"
            )
            self.lbl_user.pack(side="left", expand=True, fill="x")
            self.lbl_date = ttk.Label(
                self,
                text=f"{self.date:%A, %B %d %Y}",
                font=("Helvetica", 20),
                anchor="e",
            )
            self.lbl_date.pack(side="left", expand=True, fill="x")

            self.pack(fill="x")

    class EntryFrame(ttk.Frame):
        # Frame for adding sales

        def __init__(self, master):
            super().__init__(master)

            self.f1 = self.SalesFrame(self)

            self.config(border=1, relief="solid")

            self.pack(side="left", expand=True, fill="both")

        class SalesFrame(ttk.Frame):
            # Frame for adding sales

            def __init__(self, master):
                super().__init__(master)
                self.user = master.master.user

                self.numlist = []
                for n in range(1, 51):
                    self.numlist.append(n)

                self.style = ttk.Style()
                self.style.configure("TButton", font=("Helvetica", 15))

                self.lbl_item = ttk.Label(
                    self, text="Item Name:", font=("Helvetica", 20)
                )
                self.lbl_item.pack(pady=(10, 0))
                self.combo_item = AutocompleteCombobox(
                    self, font=("Helvetica", 30), completevalues=self.insert_values()
                )
                self.combo_item.pack(pady=(0, 10), padx=10, expand=True, fill="x")
                self.combo_item.bind("<<ComboboxSelected>>", self.update_price)
                self.lbl_quantity = ttk.Label(
                    self, text="Quantity:", font=("Helvetica", 20)
                )
                self.lbl_quantity.pack(pady=(5, 0))
                self.spinbox_quantity = ttk.Spinbox(
                    self, font=("Helvetica", 30), values=(self.numlist)
                )
                self.spinbox_quantity.set(1)
                self.spinbox_quantity.pack(pady=(0, 10), padx=10, expand=True, fill="x")
                self.spinbox_quantity.bind("<<Increment>>", self.update_price)
                self.spinbox_quantity.bind("<<Decrement>>", self.update_price)
                self.spinbox_quantity.bind("<KeyRelease>", self.update_price)
                self.lbl_price = ttk.Label(self, text="Price:", font=("Helvetica", 20))
                self.lbl_price.pack(expand=True, fill="x")
                self.lbl_value = ttk.Label(
                    self, text="0.00", font=("Helvetica", 30), anchor="center"
                )
                self.lbl_value.pack(pady=(0, 10), expand=True, fill="both")

                self.btn_add = ttk.Button(self, text="Add", command=self.add_sale)
                self.btn_add.pack(pady=10, side="left", expand=True)
                self.btn_clear = ttk.Button(
                    self, text="Clear", command=self.clear_entry
                )
                self.btn_clear.pack(pady=10, side="left", expand=True)
                self.pack(expand=True, fill="both", ipadx=5)

            def insert_values(self):
                """
                Insert values to combobox
                """
                product_list = []
                conn = None

                try:
                    conn = sqlite3.connect(DATABASE, uri=True)
                    cursor = conn.cursor()
                    cursor.execute("SELECT manufacturer, product_name FROM products")
                    rows = cursor.fetchall()

                    for row in rows:
                        item = f"{row[0]} - {row[1]}"
                        product_list.append(item)

                except sqlite3.Error as err:
                    messagebox.showerror(
                        "Database Error", f"failed to load products: {err}"
                    )

                finally:
                    if conn:
                        conn.close()
                return product_list

            def add_sale(self):
                """
                Add sale to database
                """
                curr_date = dt.datetime.now().strftime("%Y-%m-%d")
                user = self.user

                get_item_name = self.combo_item.get()
                if not get_item_name:
                    messagebox.showerror("Error", "Please select an item")

                get_item_quantity = self.spinbox_quantity.get()
                if not get_item_quantity:
                    messagebox.showerror("Error", "Please enter a quantity")

                try:
                    quantity = float(get_item_quantity)
                    if quantity <= 0:
                        messagebox.showwarning(
                            "Input Error", "Quantity must be greater than 0."
                        )
                        return

                except ValueError:
                    messagebox.showwarning("Input Error", "Quantity must be a number.")
                    return

                conn = None

                try:
                    conn = sqlite3.connect(DATABASE, uri=True)
                    cursor = conn.cursor()
                    user_id = self.get_user_id(user)
                    item_id = self.get_product_id(get_item_name)
                    total_price = self.get_total_price(get_item_name, get_item_quantity)
                    cursor.execute(
                        "INSERT INTO sales (date, product_id, quantity, total_price, user_id)VALUES (?, ?, ?, ?, ?)",
                        (curr_date, item_id, get_item_quantity, total_price, user_id),
                    )
                    conn.commit()

                except sqlite3.Error as err:
                    messagebox.showerror("DatabaseError", f"Database Error: {err}")

                finally:
                    if conn:
                        conn.close()

            def get_total_price(self, item_name, quantity):
                total = 0
                conn = None

                try:
                    conn = sqlite3.connect(DATABASE, uri=True)
                    cursor = conn.cursor()
                    conn.execute(
                        "SELECT price_per_unit FROM products WHERE product_name = '?'",
                        (item_name),
                    )
                    price = cursor.fetchone()
                    total = float(quantity) * price[0]

                except sqlite3.Error as err:
                    messagebox.showerror(
                        "Database Error", f"Failed to get total price: {err}"
                    )

                finally:
                    if conn:
                        conn.close()
                    return total

            def get_product_id(self, product_name):
                if not product_name or " - " not in product_name:
                    return None

                manufacturer, name = product_name.split(" - ", 1)
                conn = None
                try:
                    conn = sqlite3.connect(DATABASE, uri=True)
                    cursor = conn.cursor()
                    cursor.execute(
                        "SELECT id FROM products WHERE manufacturer = '?' AND product_name = '?'",
                        (manufacturer, name),
                    )
                    result = cursor.fetchone()
                    return result[0] if result else None

                except sqlite3.Error as err:
                    messagebox.showerror(
                        "Database Error", f"failed to load item id: {err}"
                    )
                    return None

                finally:
                    if conn:
                        conn.close()

            def get_product_price(self, product_name):
                if not product_name or " - " not in product_name:
                    return 0.0

                manufacturer, name = product_name.split(" - ", 1)
                conn = None
                try:
                    conn = sqlite3.connect("posdb.db")
                    cursor = conn.cursor()
                    cursor.execute(
                        "SELECT price FROM products WHERE manufacturer = ? AND product_name = ?",
                        (manufacturer, name),
                    )
                    result = cursor.fetchone()
                    return float(result[0]) if result else 0.0
                except sqlite3.Error as e:
                    messagebox.showerror(
                        "Database Error", f"Failed to get product price: {e}"
                    )
                    return 0.0
                finally:
                    if conn:
                        conn.close()

            def update_price(self, event=None):
                product = self.combo_item.get()

                try:
                    quantity = int(self.spinbox_quantity.get())
                except ValueError:
                    quantity = 1
                    self.spinbox_quantity.set("1")

                if product:
                    unit_price = self.get_product_price(product)
                    total_price = unit_price * quantity
                    self.lbl_value.config(text=f"${total_price:.2f}")
                else:
                    self.lbl_value.config(text="$0.00")

            def get_user_id(self, user):
                u_id = ""
                conn = None
                try:
                    conn = sqlite3.connect(DATABASE, uri=True)
                    cursor = conn.cursor()
                    cursor.execute(
                        "SELECT * FROM employees WHERE username = '?'", (user)
                    )
                    result = cursor.fetchone()
                    u_id = result[0]
                except sqlite3.DatabaseError as err:
                    messagebox.showerror(
                        "Database Error", f"Failed to get user id: {err}"
                    )
                finally:
                    if conn:
                        conn.close()
                    return u_id

            def clear_entry(self):
                """
                Clear entry fields
                """
                self.combo_item.delete(0, "end")
                self.spinbox_quantity.delete(0, "end")
                self.spinbox_quantity.insert(0, "1")
                self.lbl_value.config(text="$0.00")

    class TableFrame(ttk.Frame):
        """
        Frame for table
        """

        def __init__(self, master):
            super().__init__(master)

            # TODO: Add a scroll bar to tree view
            # TODO: Add Table Values

            self.tree = ttk.Treeview(
                self, columns=("item", "quantity", "price"), show="headings"
            )
            self.tree.column("item", stretch=True, anchor="w")
            self.tree.heading("item", text="Item Name")
            self.tree.column("quantity", width=60, anchor="e")
            self.tree.heading("quantity", text="Quantity")
            self.tree.column("price", width=100, anchor="e", stretch=True)
            self.tree.heading("price", text="Price")
            self.tree.pack(padx=(5, 0), expand=True, fill="both")

            self.btn_delete = ttk.Button(self, text="Delete", command=self.delete_item)
            self.btn_delete.pack(pady=10, side="left", expand=True)
            self.btn_refresh = ttk.Button(
                self, text="Refresh", command=self.refresh_table
            )
            self.btn_refresh.pack(pady=10, side="left", expand=True)

            self.pack(side="left", expand=True, fill="both")

            self.refresh_table()

        def delete_item(self):
            selected = self.tree.selection()
            if not selected:
                messagebox.showinfo("Selection", "Please select an item to delete")
                return

            if messagebox.askyesno(
                "Confirm", "Are you sure you want to delete the selected item(s)?"
            ):
                conn = None
                try:
                    conn = sqlite3.connect("posdb.db")
                    cursor = conn.cursor()

                    for item in selected:
                        item_id = self.tree.item(item, "values")[0]

                        cursor.execute("DELETE FROM sales WHERE id = ?", (item_id,))

                        self.tree.delete(item)

                    conn.commit()
                    messagebox.showinfo("Success", "Item(s) deleted successfully")

                except sqlite3.Error as e:
                    messagebox.showerror("Database Error", f"Failed to delete: {e}")
                finally:
                    if conn:
                        conn.close()

        def refresh_table(self):
            self.tree.delete(*self.tree.get_children())
            date = str(dt.datetime.now().strftime("%Y-%m-%d"))
            conn = None
            try:
                conn = sqlite3.connect(DATABASE, uri=True)
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM sales WHERE date = '?'", (date))
                rows = cursor.fetchall()

                for row in rows:
                    self.tree.insert("", "end", values=row)

            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"Failed to refresh table: {e}")
            finally:
                if conn:
                    conn.close()
