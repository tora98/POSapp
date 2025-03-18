"""
This type stub file was generated by pyright.
"""

from tkinter import ttk

"""
Author: Juliette Monsel
License: GNU GPLv3
Source: This repository
"""
class AutoHideScrollbar(ttk.Scrollbar):
    """Scrollbar that automatically hides when not needed."""
    def __init__(self, master=..., **kwargs) -> None:
        """
        Create a scrollbar.

        :param master: master widget
        :type master: widget
        :param kwargs: options to be passed on to the :class:`ttk.Scrollbar` initializer
        """
        ...
    
    def set(self, lo, hi): # -> None:
        """
        Set the fractional values of the slider position.
        
        :param lo: lower end of the scrollbar (between 0 and 1)
        :type lo: float
        :param hi: upper end of the scrollbar (between 0 and 1)
        :type hi: float
        """
        ...
    
    def place(self, **kw): # -> None:
        """
        Place a widget in the parent widget.
        
        :param in\_: master relative to which the widget is placed
        :type in\_: widget
        :param x: locate anchor of this widget at position x of master
        :type x: int
        :param y: locate anchor of this widget at positiony of master
        :type y: int
        :param relx: locate anchor of this widget between 0 and 1
                      relative to width of master (1 is right edge)
        :type relx: float
        :param rely: locate anchor of this widget between 0 and 1
                      relative to height of master (1 is bottom edge)
        :type rely: float
        :param anchor: position anchor according to given direction 
                        ("n", "s", "e", "w" or combinations)
        :type anchor: str
        :param width: width of this widget in pixel
        :type width: int
        :param height: height of this widget in pixel
        :type height: int
        :param relwidth: width of this widget between 0.0 and 1.0
                          relative to width of master (1.0 is the same width
                          as the master)
        :type relwidth: float
        :param relheight: height of this widget between 0.0 and 1.0
                           relative to height of master (1.0 is the same
                           height as the master)
        :type relheight: float
        :param bordermode: "inside" or "outside": whether to take border width of master widget into account
        :type bordermode: str
        """
        ...
    
    def pack(self, **kw): # -> None:
        """
        Pack a widget in the parent widget.
        
        :param after: pack it after you have packed widget
        :type after: widget
        :param anchor: position anchor according to given direction 
                        ("n", "s", "e", "w" or combinations)
        :type anchor: str
        :param before: pack it before you will pack widget
        :type before: widget
        :param expand: expand widget if parent size grows
        :type expand: bool
        :param fill: "none" or "x" or "y" or "both": fill widget if widget grows
        :type fill: str
        :param in\_: widget to use as container
        :type in\_: widget
        :param ipadx: add internal padding in x direction
        :type ipadx: int
        :param ipady: add internal padding in y direction
        :type ipady: int
        :param padx: add padding in x direction
        :type padx: int
        :param pady: add padding in y irection
        :type pady: int
        :param side: "top" (default), "bottom", "left" or "right": where to add this widget
        :type side: str
        """
        ...
    
    def grid(self, **kw): # -> None:
        """
        Position a widget in the parent widget in a grid. 
        
        :param column: use cell identified with given column (starting with 0)
        :type column: int
        :param columnspan: this widget will span several columns
        :type columnspan: int
        :param in\_: widget to use as container
        :type in\_: widget
        :param ipadx: add internal padding in x direction
        :type ipadx: int
        :param ipady: add internal padding in y direction
        :type ipady: int
        :param padx: add padding in x direction
        :type padx: int
        :param pady: add padding in y irection
        :type pady: int
        :param row: use cell identified with given row (starting with 0)
        :type row: int
        :param rowspan: this widget will span several rows
        :type rowspan: int
        :param sticky: "n", "s", "e", "w" or combinations: if cell is 
                       larger on which sides will this widget stick to 
                       the cell boundary
        :type sticky: str
        """
        ...
    


