import tkinter as tk
from child_window import ChildWindow


class MainWindow(tk.Frame):
    def __init__(self, root: tk.Tk, title: str, width: int, height: int, resizeble=(True, True), icon=None):
        super().__init__(root)
        self.root = root
        self.init_window(title, width, height, resizeble, icon)
        self.init_toolbar()

    def init_window(self, title: str, width: int, height: int, resizeble=(True, True), icon=None):
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - width) // 2
        y = (sh - height) // 2
        self.root.title(title)
        self.root.geometry("{0}x{1}+{2}+{3}".format(width, height, 100, 100))
        self.root.resizable(resizeble[0], resizeble[1])
        if icon:
            photo = tk.PhotoImage(icon)
            self.root.iconphoto(False, photo)

    def init_toolbar(self):
        toolbar = tk.Frame(bg="#d7d8e0", bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        #self.add_img =

    def run(self):
        self.root.mainloop()

    def open_dialog(self):
        ChildWindow(self.root, "Add any", 300, 200)