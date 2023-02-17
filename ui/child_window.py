import tkinter as tk
from tkinter import PhotoImage


class ChildWindow(tk.Toplevel):
    def __init__(self, root, title: str, width: int, height: int, icon=None):
        super().__init__(root)
        self.init_window(title, width, height, icon)

    def init_window(self, title: str, width: int, height: int, icon=None):
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()

        #x = (sw - width) // 2
        #y = (sh - height) // 2
        self.title(title)
        self.geometry("{0}x{1}+{2}+{3}".format(width, height, 200, 300))
        self.resizable(False, False)
        if icon:
            photo = PhotoImage(icon)
            self.iconphoto(False, photo)
        self.grab_set()
        self.focus_set()
