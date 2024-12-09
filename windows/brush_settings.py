from PyQt6.QtWidgets import (
    QVBoxLayout,
    QDialog,
    QLabel,
    QSpinBox,
    QHBoxLayout,
    QColorDialog,
    QPushButton,
    QSlider
)
from PyQt6.QtCore import QSize, Qt

WIDTH = 400
HEIGHT = 400

class BrushSettingsWindow(QDialog):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setWindowTitle("Изменить кисть")
        self.setMinimumSize(QSize(WIDTH, HEIGHT))

        main_layout = QVBoxLayout()

        # цвет
        main_layout.addWidget(QLabel("Цвет кисти:"))
        main_layout.addLayout(self.create_color_layout())

        # размер
        main_layout.addWidget(QLabel("Размер кисти:"))
        main_layout.addLayout(self.choose_size_layout())

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

    def choose_size_layout(self):
        layout = QVBoxLayout()
        # Ползунок
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(1, 10)
        self.slider.setValue(self.user.Brush.radius)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.valueChanged.connect(self.update_size)
        layout.addWidget(self.slider)
        return layout

    def update_size(self, value):
        self.user.Brush.radius = value