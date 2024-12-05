from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction
from windows.canvas_settings_window import CanvasCreateWindow


class MenuBar(QMenuBar):
    def __init__(self, user):
        super().__init__()
        self.user = user
        file_menu = self.addMenu("Холст")

        new_action = QAction("Создать", self)
        change_action = QAction("Изменить", self)
        new_action.triggered.connect(self.new_canvas)
        change_action.triggered.connect(self.change_canvas)
        file_menu.addAction(new_action)
        file_menu.addAction(change_action)


    def new_canvas(self):
        canvas_window = CanvasCreateWindow(self.user, True)
        canvas_window.exec()

    def change_canvas(self):
        canvas_window = CanvasCreateWindow(self.user, False)
        canvas_window.exec()

