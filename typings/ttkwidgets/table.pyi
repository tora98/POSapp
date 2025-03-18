"""
This type stub file was generated by pyright.
"""

from tkinter import ttk

"""
Author: Juliette Monsel
License: GNU GPLv3
Source: This repository

Table made out of a Treeview with possibility to drag rows and columns and to sort columns.
"""
IM_DRAG = ...
class Table(ttk.Treeview):
    """
    Table widget displays a table with options to drag rows and columns and
    to sort columns.

    This widget is based on the :class:`ttk.Treeview` and shares many options and methods
    with it.
    """
    _initialized = ...
    def __init__(self, master=..., show=..., drag_cols=..., drag_rows=..., sortable=..., class_=..., **kwargs) -> None:
        """
        Create a Table.

        :param master: master widget
        :type master: widget
        :param drag_cols: whether columns are draggable
        :type drag_cols: bool
        :param drag_rows: whether rows are draggable
        :type drag_rows: bool
        :param sortable: whether columns are sortable by clicking on their
                         headings. The sorting order depends on the type of
                         data (str, float, ...) which can be set with the column
                         method.
        :type sortable: bool
        :param show: which parts of the treeview to show (same as the Treeview option)
        :type show: str
        :param kwargs: options to be passed on to the :class:`ttk.Treeview` initializer
        """
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def __getitem__(self, key): # -> bool | Any:
        ...
    
    def cget(self, key): # -> bool | Any:
        """
        Query widget option.

        :param key: option name
        :type key: str
        :return: value of the option

        To get the list of options for this widget, call the method :meth:`~Table.keys`.
        """
        ...
    
    def column(self, column, option=..., **kw): # -> type[str] | _TreeviewColumnDict | None:
        """
        Query or modify the options for the specified column.

        If `kw` is not given, returns a dict of the column option values. If
        `option` is specified then the value for that option is returned.
        Otherwise, sets the options to the corresponding values.

        :param id: the column's identifier (read-only option)
        :param anchor: "n", "ne", "e", "se", "s", "sw", "w", "nw", or "center":
                       alignment of the text in this column with respect to the cell
        :param minwidth: minimum width of the column in pixels
        :type minwidth: int
        :param stretch: whether the column's width should be adjusted when the widget is resized
        :type stretch: bool
        :param width: width of the column in pixels
        :type width: int
        :param type: column's content type (for sorting), default type is `str`
        :type type: type

        """
        ...
    
    def configure(self, cnf=..., **kw): # -> tuple[Literal['drag_cols'], bool | Any] | tuple[Literal['drag_rows'], bool] | tuple[Literal['sortable'], bool | Any] | dict[str, tuple[str, str, str, Any, Any]] | None:
        """
        Configure resources of the widget.

        To get the list of options for this widget, call the method :meth:`~Table.keys`.
        See :meth:`~Table.__init__` for a description of the widget specific option.
        """
        ...
    
    def delete(self, *items): # -> None:
        """
        Delete all specified items and all their descendants. The root item may not be deleted.

        :param items: list of item identifiers
        :type items: sequence[str]
        """
        ...
    
    def detach(self, *items): # -> None:
        """
        Unlinks all of the specified items from the tree.

        The items and all of their descendants are still present, and may be
        reinserted at another point in the tree, but will not be displayed.
        The root item may not be detached.

        :param items: list of item identifiers
        :type items: sequence[str]
        """
        ...
    
    def heading(self, column, option=..., **kw):
        """
        Query or modify the heading options for the specified column.

        If `kw` is not given, returns a dict of the heading option values. If
        `option` is specified then the value for that option is returned.
        Otherwise, sets the options to the corresponding values.

        :param text: text to display in the column heading
        :type text: str
        :param image: image to display to the right of the column heading
        :type image: PhotoImage
        :param anchor: "n", "ne", "e", "se", "s", "sw", "w", "nw", or "center":
                       alignement of the heading text
        :type anchor: str
        :param command: callback to be invoked when the heading label is pressed.
        :type command: function
        """
        ...
    
    def insert(self, parent, index, iid=..., **kw): # -> str:
        """
        Creates a new item and return the item identifier of the newly created item.
        
        :param parent: identifier of the parent item
        :type parent: str
        :param index: where in the list of parent's children to insert the new item
        :type index: int or "end"
        :param iid: item identifier, iid must not already exist in the tree. If iid is None a new unique identifier is generated.
        :type iid: None or str
        :param kw: item's options: see :meth:`~Table.item`
        
        :return: the item identifier of the newly created item
        :rtype: str
        """
        ...
    
    def item(self, item, option=..., **kw):
        """
        Query or modify the options for the specified item.

        If no options are given, a dict with options/values for the item is returned.
        If option is specified then the value for that option is returned.
        Otherwise, sets the options to the corresponding values as given by `kw`.
        
        :param text: item's label
        :type text: str
        :param image: image to be displayed on the left of the item's label
        :type image: PhotoImage
        :param values: values to put in the columns
        :type values: sequence
        :param open: whether the item's children should be displayed
        :type open: bool
        :param tags: list of tags associated with this item
        :type tags: sequence[str]
        """
        ...
    
    def keys(self): # -> list[str]:
        ...
    
    def move(self, item, parent, index): # -> None:
        """
        Moves item to position index in parent’s list of children.

        It is illegal to move an item under one of its descendants. If index is
        less than or equal to zero, item is moved to the beginning, if greater
        than or equal to the number of children, it is moved to the end.
        If item was detached it is reattached.

        :param item: item's identifier
        :type item: str
        :param parent: new parent of item
        :type parent: str
        :param index: where in the list of parent’s children to insert item
        :type index: int of "end"
        """
        ...
    
    reattach = ...
    def set(self, item, column=..., value=...): # -> dict[str, Any]:
        """
        Query or set the value of given item.

        With one argument, return a dictionary of column/value pairs for the
        specified item. With two arguments, return the current value of the
        specified column. With three arguments, set the value of given column
        in given item to the specified value.

        :param item: item's identifier
        :type item: str
        :param column: column's identifier
        :type column: str, int or None
        :param value: new value
        """
        ...
    
    def set_children(self, item, *newchildren): # -> None:
        """
        Replaces item’s children with newchildren.

        Children present in item that are not present in newchildren are detached
        from tree. No items in newchildren may be an ancestor of item.

        :param newchildren: new item's children (list of item identifiers)
        :type newchildren: sequence[str]
        """
        ...
    


