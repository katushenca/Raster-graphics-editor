from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from widgets.menu_bar import MenuBar
from windows.canvas import Canvas


class MainWindow(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setWindowTitle("Fiitoshop")
        self.setMinimumSize(QSize(1280, 720))
        self.setMaximumSize(QSize(1920, 1080))

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.menu_bar = MenuBar(user)
        self.setMenuBar(self.menu_bar)
        self.show()

    def create_canvas(self):
        self.canvas_window = Canvas(self.user.Canvas, parent=self)
        self.layout.addWidget(self.canvas_window)
        self.canvas_window.show()