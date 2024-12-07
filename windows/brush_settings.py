from PyQt6.QtWidgets import (
    QVBoxLayout,
    QDialog,
    QLabel,
    QSpinBox,
    QHBoxLayout,
    QColorDialog,
    QPushButton
)
from PyQt6.QtCore import QSize

WIDTH = 400
HEIGHT = 400

class BrushSettingsWindow(QDialog):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setWindowTitle("Изменить кисть")
        self.setMinimumSize(QSize(WIDTH, HEIGHT))

        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Цвет холста:"))
        main_layout.addLayout(self.create_color_layout())

        button = QPushButton("Изменить")
        main_layout.addWidget(button)

        button.clicked.connect(self.close)

        main_layout.addStretch()
        self.setLayout(main_layout)

    def open_color_dialog(self):
        color = QColorDialog.getColor(self.user.Brush.color, self, "Выберите цвет")
        if color.isValid():
            self.change_brush_color(color)

    def change_brush_color(self, color):
        self.user.Brush.color = color
        self.color_label.setText(f"Текущий цвет: {color.name()}")
        self.color_label.setStyleSheet(f"background-color: {color.name()}; padding: 10px;")

    def create_color_layout(self):
        layout = QVBoxLayout()
        self.color_button = QPushButton("Выбрать цвет")
        self.color_button.clicked.connect(self.open_color_dialog)
        layout.addWidget(self.color_button)
        self.color_label = QLabel(f"Текущий цвет: {self.user.Brush.color.name()}")
        self.color_label.setStyleSheet(
            f"background-color: {self.user.Brush.color.name()}; padding: 10px;"
        )
        layout.addWidget(self.color_label)
        return layout

