import tkinter as tk
from ui.main_window import MainWindow


if __name__ == '__main__':
    root = tk.Tk()
    app = MainWindow(root, "Регламент", 600, 400)
    app.pack()
    app.run()


