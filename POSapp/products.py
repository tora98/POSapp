"""Scrollbar update by claude
def __init__(self, master):
    super().__init__(master)

    # Create a frame to hold the treeview and scrollbar
    tree_frame = ttk.Frame(master)
    tree_frame.pack(expand=True, fill="both")

    # Create the scrollbars
    y_scrollbar = ttk.Scrollbar(tree_frame, orient="vertical")
    x_scrollbar = ttk.Scrollbar(tree_frame, orient="horizontal")

    # Create the treeview
    self.tree = ttk.Treeview(tree_frame, columns=(
        "product_id",
        "product_name",
        "manufacturer",
        "packaging_units",
        "price_per_unit",
        "state"),
        show="headings",
        yscrollcommand=y_scrollbar.set,
        xscrollcommand=x_scrollbar.set
        )

    # Configure the scrollbars
    y_scrollbar.config(command=self.tree.yview)
    x_scrollbar.config(command=self.tree.xview)

    # Place the treeview and scrollbars
    self.tree.grid(row=0, column=0, sticky="nsew")
    y_scrollbar.grid(row=0, column=1, sticky="ns")
    x_scrollbar.grid(row=1, column=0, sticky="ew")

    # Configure the grid weights
    tree_frame.columnconfigure(0, weight=1)
    tree_frame.rowconfigure(0, weight=1)

    # Configure columns and headings
    self.tree.column("product_id", width=10)
    self.tree.heading("product_id", text="ID")
    # ... other column configurations ...

    # Rest of your code...
"""

# update sql queries to avoid sql injection using parameterized queries
from tkinter import ttk
import sqlite3

DATABASE = "file:posdb.db?mode=rw"


class Products(ttk.Frame):
    """
    Frame for adding new products
    """

    def __init__(self, master):
        super().__init__(master)

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 15))

        self.frame1 = ProductEntry(self, "", "", "", "", "")
        self.frame2 = ProductList(self)

        self.pack(expand=True, fill="both")


class ProductEntry(ttk.Frame):
    def __init__(
        self,
        master,
        product_ID,
        product_name,
        manufacturer,
        packaging_units,
        price_per_unit,
    ):
        super().__init__(master)

        self.product_ID = product_ID
        self.product_name = product_name
        self.manufacturer = manufacturer
        self.packaging_units = packaging_units
        self.price_per_unit = price_per_unit

        self.lbl_product_name = ttk.Label(
            self, text="Product Name:", font=("Helvetica", 20)
        )
        self.lbl_product_name.pack(pady=(10, 0))
        self.entry_product_name = ttk.Entry(self, font=("Arial", 30))
        self.entry_product_name.pack(pady=(0, 10))
        self.lbl_manufacturer = ttk.Label(
            self, text="Manufacturer:", font=("Helvetica", 20)
        )
        self.lbl_manufacturer.pack(pady=(10, 0))
        self.entry_manufacturer = ttk.Entry(self, font=("Arial", 30))
        self.entry_manufacturer.pack(pady=(0, 10))
        self.lbl_packaging_units = ttk.Label(
            self,
            text="Packaging Units (Number of kilos or pieces per Bag/Box/Bottle):",
            font=("Helvetica", 10),
        )
        self.lbl_packaging_units.pack(pady=(10, 0))
        self.entry_packaging_units = ttk.Entry(self, font=("Arial", 30))
        self.entry_packaging_units.pack(pady=(0, 10))
        self.lbl_price_per_unit = ttk.Label(
            self, text="Price Per Unit:", font=("Helvetica", 20)
        )
        self.lbl_price_per_unit.pack(pady=(10, 0))
        self.entry_price_per_unit = ttk.Entry(self, font=("Arial", 30))
        self.entry_price_per_unit.pack(pady=(0, 10))

        self.insert(product_name, manufacturer, packaging_units, price_per_unit)

        self.lbl_error = ttk.Label(
            self, text="", foreground="red", font=("Helvetica", 10)
        )
        self.lbl_error.pack(pady=10)
        self.btn_add = ttk.Button(self, text="Add", command=self.add_product)
        self.btn_add.pack(side="left", pady=10, expand=True)
        self.btn_clear = ttk.Button(self, text="Clear", command=self.clear_entry)
        self.btn_clear.pack(side="left", pady=10, expand=True)
        self.btn_update = ttk.Button(self, text="Update", command=self.update)
        self.btn_update.pack(side="left", pady=10, expand=True)
        self.btn_cancel = ttk.Button(self, text="Cancel", command=self.cancel)
        self.btn_cancel.pack(side="left", pady=10, expand=True)

        self.entry_price_per_unit.bind("<Return>", self.add_product)

        self.pack(expand=True, fill="both", side="left", ipadx=10, ipady=10)

    def insert(self, product_name, manufacturer, packaging_units, price_per_unit):
        self.entry_product_name.insert("end", product_name)
        self.entry_manufacturer.insert("end", manufacturer)
        self.entry_packaging_units.insert("end", packaging_units)
        self.entry_price_per_unit.insert("end", price_per_unit)

    def add_product(self, event=None):
        """
        Add a product to the database
        """
        get_product_name = self.entry_product_name.get()
        get_manufacturer = self.entry_manufacturer.get()
        get_packaging_units = self.entry_packaging_units.get()
        get_price_per_unit = self.entry_price_per_unit.get()

        if (
            get_product_name == ""
            or get_manufacturer == ""
            or get_packaging_units == ""
            or get_price_per_unit == ""
        ):
            self.lbl_error.config(text="Please fill out all fields.")
        else:
            conn = sqlite3.connect(DATABASE, uri=True)
            cursor = conn.cursor()
            try:
                product_name = self.entry_product_name.get()
                manufacturer = self.entry_manufacturer.get()
                packaging_units = self.entry_packaging_units.get()
                price_per_unit = self.entry_price_per_unit.get()
                cursor.execute(f"""INSERT INTO products (
                    product_name,
                    manufacturer,
                    packaging_units,
                    price_per_unit,
                    state
                    ) VALUES (
                    '{product_name}',
                    '{manufacturer}',
                    '{packaging_units}',
                    '{price_per_unit}',
                    'available'
                    )
                """)
                conn.commit()
                conn.close()
                self.lbl_error.config(text="Product added successfully.")
                self.clear_entry()

            except sqlite3.IntegrityError as err:
                self.lbl_error.config(text=str(err))

    def clear_entry(self):
        """
        Clear the entry fields
        """
        self.entry_product_name.delete(0, "end")
        self.entry_manufacturer.delete(0, "end")
        self.entry_packaging_units.delete(0, "end")
        self.entry_price_per_unit.delete(0, "end")
        self.lbl_error.config(text="")

    def update(self):
        conn = sqlite3.connect(DATABASE, uri=True)
        cursor = conn.cursor()

        get_product_name = self.entry_product_name.get()
        get_manufacturer = self.entry_manufacturer.get()
        get_packaging_units = self.entry_packaging_units.get()
        get_price_per_unit = self.entry_price_per_unit.get()

        cursor.execute(
            """UPDATE products SET
            product_name = ?,
            manufacturer = ?,
            packaging_units = ?,
            price_per_unit = ?
            WHERE product_id = ?""",
            (
                get_product_name,
                get_manufacturer,
                get_packaging_units,
                get_price_per_unit,
                self.product_ID,
            ),
        )

        conn.commit()
        conn.close()

        # Refresh the table after update
        for widget in self.master.winfo_children():
            if isinstance(widget, ProductList):
                widget.refresh_table()

    def cancel(self):
        self.destroy()


class ProductList(ttk.Frame):
    """
    Frame for product table
    """

    def __init__(self, master):
        super().__init__(master)
        # TODO: Add scrollbar to treeview

        self.tree = ttk.Treeview(
            master,
            columns=(
                "product_id",
                "product_name",
                "manufacturer",
                "packaging_units",
                "price_per_unit",
                "state",
            ),
            show="headings",
        )
        self.tree.column("product_id", width=10)
        self.tree.heading("product_id", text="ID")
        self.tree.column("product_name", width=150)
        self.tree.heading("product_name", text="Product Name")
        self.tree.column("manufacturer", width=150)
        self.tree.heading("manufacturer", text="Manufacturer")
        self.tree.column("packaging_units", width=100)
        self.tree.heading("packaging_units", text="Packaging Units")
        self.tree.column("price_per_unit", width=100)
        self.tree.heading("price_per_unit", text="Price Per Unit")
        self.tree.column("state", width=100)
        self.tree.heading("state", text="State")
        self.tree.pack(expand=True, fill="both")

        self.refresh_table()

        self.btn_refresh = ttk.Button(self, text="Refresh", command=self.refresh_table)
        self.btn_refresh.pack(side="left", pady=10, expand=True)
        self.btn_delete = ttk.Button(self, text="Delete", command=self.delete_product)
        self.btn_delete.pack(side="left", pady=10, expand=True)

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.pack(expand=True, fill="both", side="left", ipadx=10, ipady=10)

    def on_tree_select(self, event=None):
        # First check if anything is actually selected
        selected_items = self.tree.selection()
        if not selected_items:
            return  # No selection, do nothing

        try:
            # Get the values from the selected item
            values = self.tree.item(selected_items[0], "values")
            product_ID = values[0]
            product_name = values[1]
            manufacturer = values[2]
            packaging_units = values[3]
            price_per_unit = values[4]

            # Remove existing ProductEntry frame if it exists
            for widget in self.master.winfo_children():
                if isinstance(widget, ProductEntry):
                    widget.destroy()

            # Create a new ProductEntry with the selected product's data
            ProductEntry(
                self.master,
                product_ID,
                product_name,
                manufacturer,
                packaging_units,
                price_per_unit,
            )

        except (IndexError, TypeError) as e:
            print(f"Error handling selection: {e}")

    def refresh_table(self) -> None:
        """
        Refreshes the table
        """
        self.tree.delete(*self.tree.get_children())
        conn = sqlite3.connect(DATABASE, uri=True)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE state = 'available'")
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)
        conn.close()

    def delete_product(self):
        """
        Disables a product from the database
        """
        selected = self.tree.selection()
        if not selected:
            return
        selected_id = self.tree.item(selected[0], "values")
        item_id = selected_id[0]
        conn = sqlite3.connect(DATABASE, uri=True)
        cursor = conn.cursor()
        cursor.execute(f"""UPDATE products SET
            state = 'unavailable'
            WHERE product_id = {item_id}""")
        conn.commit()
        conn.close()
        self.refresh_table()
