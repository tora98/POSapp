"""
This type stub file was generated by pyright.
"""

from tkinter import ttk

"""
Authors: Mitja Martini and Russell Adams
License: "Licensed same as original by Mitja Martini or public domain, whichever is less restrictive"
Source: https://mail.python.org/pipermail/tkinter-discuss/2012-January/003041.html

Edited by RedFantom for ttk and Python 2 and 3 cross-compatibility and <Enter> binding
Edited by Juliette Monsel to include Tcl code to navigate the dropdown by Pawel Salawa
(https://wiki.tcl-lang.org/page/ttk%3A%3Acombobox, copyright 2011)
"""
tk_umlauts = ...
class AutocompleteCombobox(ttk.Combobox):
    """:class:`ttk.Combobox` widget that features autocompletion."""
    def __init__(self, master=..., completevalues=..., **kwargs) -> None:
        """
        Create an AutocompleteCombobox.

        :param master: master widget
        :type master: widget
        :param completevalues: autocompletion values
        :type completevalues: list
        :param kwargs: keyword arguments passed to the :class:`ttk.Combobox` initializer
        """
        ...
    
    def set_completion_list(self, completion_list): # -> None:
        """
        Use the completion list as drop down selection menu, arrows move through menu.

        :param completion_list: completion values
        :type completion_list: list
        """
        ...
    
    def autocomplete(self, delta=...): # -> None:
        """
        Autocomplete the Combobox.

        :param delta: 0, 1 or -1: how to cycle through possible hits
        :type delta: int
        """
        ...
    
    def handle_keyrelease(self, event): # -> None:
        """
        Event handler for the keyrelease event on this widget.

        :param event: Tkinter event
        """
        ...
    
    def handle_return(self, event): # -> None:
        """
        Function to bind to the Enter/Return key so if Enter is pressed the selection is cleared

        :param event: Tkinter event
        """
        ...
    
    def config(self, **kwargs): # -> None:
        """Alias for configure"""
        ...
    
    def configure(self, **kwargs):
        """Configure widget specific keyword arguments in addition to :class:`ttk.Combobox` keyword arguments."""
        ...
    
    def cget(self, key): # -> list[Any] | Any | None:
        """Return value for widget specific keyword arguments"""
        ...
    
    def keys(self): # -> list[str]:
        """Return a list of all resource names of this widget."""
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def __getitem__(self, item): # -> list[Any] | Any | None:
        ...
    


