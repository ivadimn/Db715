from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QIcon, QPixmap
from ui.child_window import ChildWindow


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pyqt6 Application")
        self.setWindowIcon(QIcon(self.get_icon("/images/animal-dog.png")))
        self.setFixedHeight(200)
        self.setFixedWidth(400)

    def init_window(self, title: str, width: int, height: int, resizeble=(True, True), icon=None):
        pass

    def init_toolbar(self):
        pass

    def get_icon(self, filename: str) ->QIcon:
        icon = QIcon()
        icon.addPixmap(QPixmap(filename))
        return icon
