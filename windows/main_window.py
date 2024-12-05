from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow
from widgets.menu_bar import MenuBar


class MainWindow(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setWindowTitle("Fiitoshop")
        self.setMinimumSize(QSize(1280, 720))
        self.setMaximumSize(QSize(1920, 1080))
        self.show()
        self.menu_bar = MenuBar(user)
        self.setMenuBar(self.menu_bar)
