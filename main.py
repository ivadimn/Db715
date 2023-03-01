from PyQt6.QtWidgets import QApplication, QWidget
from ui.main_window import MainWindow
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    sys.exit(app.exec())


