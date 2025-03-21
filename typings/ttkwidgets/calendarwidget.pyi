"""
This type stub file was generated by pyright.
"""

from tkinter import ttk

"""
Author: The Python Team
License: The Python License
Source: http://svn.python.org/projects/sandbox/trunk/ttk-gsoc/samples/ttkcalendar.py
"""
def get_calendar(locale, fwday): # -> TextCalendar | LocaleTextCalendar:
    ...

class Calendar(ttk.Frame):
    """
    ttk Widget that enables a calender within a frame, allowing the user to select dates.
    
    | Credits to: The Python team
    | Source: The Python/ttk samples
    | License: The Python GPL-compatible license
    """
    datetime = ...
    timedelta = ...
    def __init__(self, master=..., **kw) -> None:
        """
        Create a Calendar.
        
        :param master: master widget
        :type master: widget
        :param locale: calendar locale (defines the language, date formatting)
        :type locale: str
        :param firstweekday: first day of the week, 0 is monday
        :type firstweekday: int
        :param year: year to display
        :type year: int
        :param month: month to display
        :type month: int
        :param selectbackground: background color of the selected day
        :type selectbackground: str
        :param selectforeground: selectforeground color of the selected day
        :type selectforeground: str
        :param kw: options to be passed on to the :class:`ttk.Frame` initializer
        """
        ...
    
    def __setitem__(self, item, value): # -> None:
        ...
    
    def __getitem__(self, item): # -> Any:
        ...
    
    @property
    def selection(self): # -> None:
        """
        Return the currently selected date.
        
        :rtype: datetime
        """
        ...
    


