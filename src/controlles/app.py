# controllers/app.py
from PySide6.QtWidgets import QApplication
from ..views.main_window import Window
from .main_controller import MainController
import sys

def main():
    app = QApplication(sys.argv)
    win = Window()
    controller = MainController(win)
    win.show()
    sys.exit(app.exec())
