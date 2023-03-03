from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtGui import QIcon, QPixmap
from ui.child_window import ChildWindow
import os


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.init_ui()

    def init_window(self):
        self.setWindowTitle("Pyqt6 Application")
        self.setWindowIcon(QIcon(self.get_icon("./imgs/animal-dog.png")))
        self.setGeometry(100, 100, 500, 200)
        self.setStyleSheet("background-color: grey")

    def init_ui(self):
        btn = QPushButton("Click me", self)
        btn.setGeometry(20, 20, 80, 40)
        btn.setStyleSheet("background-color: yellow")
        btn.setIcon(QIcon("./imgs/arrow.png"))
        print(os.path.exists("arrow.png"))
        print(os.path.abspath(os.path.curdir))


    def init_toolbar(self):
        pass

    def get_icon(self, filename: str) ->QIcon:
        icon = QIcon()
        icon.addPixmap(QPixmap(filename))
        return icon
