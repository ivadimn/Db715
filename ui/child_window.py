import tkinter as tk
from tkinter import PhotoImage


class ChildWindow(tk.Toplevel):
    def __init__(self, root: tk.Tk, title: str, width: int, height: int, icon=None):
        super().__init__(root)
        self.root = root
        self.init_window(title, width, height, icon)

    def init_window(self, title: str, width: int, height: int, icon=None):
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - width) // 2
        y = (sh - height) // 2
        self.root.title(title)
        self.root.geometry("{0}x{1}+{2}+{3}".format(width, height, x, y))
        self.root.resizable(False, False)
        if icon:
            photo = PhotoImage(icon)
            self.root.iconphoto(False, photo)
        self.grab_set()
        self.focus_set()
