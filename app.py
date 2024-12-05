from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QDialog,
    QLabel,
    QSpinBox,
    QHBoxLayout,
    QColorDialog,
    QPushButton
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QColor
import sys


class CanvasCreateWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Создать холст")
        self.setMinimumSize(QSize(800, 400))
        self.canvas_width = 10

        container = QVBoxLayout()
        label = QLabel("Размеры холста:")
        container.addWidget(label)
        width_label = QLabel("Ширина холста:")

        self.width_spinbox = QSpinBox()
        self.width_spinbox.setRange(1, 800)
        self.width_spinbox.setValue(600)  # Значение по умолчанию

        px_label1 = QLabel("px")

        height_label = QLabel("Высота холста:")
        self.height_spinbox = QSpinBox()
        self.height_spinbox.setRange(1, 800)  # Диапазон значений
        self.height_spinbox.setValue(600)  # Значение по умолчанию
        px_label2 = QLabel("px")

        self.width_spinbox.valueChanged.connect(self.update_canvas_size)
        self.height_spinbox.valueChanged.connect(self.update_canvas_size)

        layout = QHBoxLayout()
        layout.addWidget(width_label)
        layout.addWidget(self.width_spinbox)
        layout.addWidget(px_label1)
        layout.addSpacing(20)
        layout.addWidget(height_label)
        layout.addWidget(self.height_spinbox)
        layout.addWidget(px_label2)
        container.addLayout(layout)

        color_label = QLabel("Цвет холста")
        container.addWidget(color_label)

        # Текущий цвет
        self.current_color = QColor(255, 255, 255) # Белый по умолчанию

        # Кнопка для выбора цвета
        self.color_button = QPushButton("Выбрать цвет")
        self.color_button.clicked.connect(self.open_color_dialog)

        # Метка для отображения текущего цвета
        self.color_label = QLabel("Текущий цвет: #FFFFFF")
        self.color_label.setStyleSheet(
            f"background-color: {self.current_color.name()}; padding: 10px;")

        # Расположение виджетов
        color_layout = QVBoxLayout()
        color_layout.addWidget(self.color_button)
        color_layout.addWidget(self.color_label)
        container.addLayout(color_layout)


        container.addStretch()
        self.setLayout(container)

    def update_canvas_size(self):
        width = self.width_spinbox.value()
        height = self.height_spinbox.value()
        print(f"Ширина: {width}px, Высота: {height}px")

    def open_color_dialog(self):
        # Открытие диалога выбора цвета
        color = QColorDialog.getColor(self.current_color, self,
                                      "Выберите цвет")

        # Проверка, что пользователь выбрал цвет
        if color.isValid():
            self.current_color = color
            self.color_label.setText(f"Текущий цвет: {color.name()}")
            self.color_label.setStyleSheet(
                f"background-color: {color.name()}; padding: 10px;")


# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fiitoshop")
        self.setMinimumSize(QSize(1280, 720))
        self.setMaximumSize(QSize(1920, 1080))
        self.show()

        layout = QVBoxLayout()
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("Холст")

        new_action = QAction("Создать", self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

    def new_file(self):
        print("Создание нового файла")
        canvas_window = CanvasCreateWindow()
        canvas_window.exec()

app = QApplication(sys.argv) # всегда только один экземпляр

window = MainWindow() # widget qt окно
window.show() # по умолчанию окно скрыто

app.exec() # запускаем цикл событий

# пока из цикла не выйдем (из приложения) сюда не доберемся

