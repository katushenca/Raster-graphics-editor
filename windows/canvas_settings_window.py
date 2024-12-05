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
import Entities.canvas_entity as canvas_entity
import windows.main_window


class CanvasCreateWindow(QDialog):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setWindowTitle("Создать холст")
        self.setMinimumSize(QSize(canvas_entity.WIDTH, canvas_entity.HEIGHT))

        main_layout = QVBoxLayout()

        main_layout.addWidget(QLabel("Размеры холста:"))
        main_layout.addLayout(self.create_size_layout())

        main_layout.addWidget(QLabel("Цвет холста:"))
        main_layout.addLayout(self.create_color_layout())

        button = QPushButton("Создать")
        main_layout.addWidget(button)
        button.clicked.connect(user.main_window.create_canvas)
        button.clicked.connect(self.close)

        main_layout.addStretch()
        self.setLayout(main_layout)

    def update_canvas_size(self):
        self.user.Canvas.width = self.width_spinbox.value()
        self.user.Canvas.height = self.height_spinbox.value()

    def open_color_dialog(self):
        color = QColorDialog.getColor(self.user.Canvas.qtColor, self, "Выберите цвет")
        if color.isValid():
            self.set_canvas_color(color)

    def set_canvas_color(self, color):
        self.user.Canvas.qtColor = color
        self.color_label.setText(f"Текущий цвет: {color.name()}")
        self.color_label.setStyleSheet(f"background-color: {color.name()}; padding: 10px;")

    def create_size_layout(self):
        layout = QHBoxLayout()

        layout.addWidget(QLabel("Ширина холста:"))
        self.width_spinbox = self._create_spinbox(
            canvas_entity.MIN_WIDTH, canvas_entity.MAX_WIDTH, canvas_entity.WIDTH
        )
        layout.addWidget(self.width_spinbox)
        layout.addWidget(QLabel("px"))

        # Высота
        layout.addSpacing(20)
        layout.addWidget(QLabel("Высота холста:"))
        self.height_spinbox = self._create_spinbox(
            canvas_entity.MIN_HEIGHT, canvas_entity.MAX_HEIGHT, canvas_entity.HEIGHT
        )
        layout.addWidget(self.height_spinbox)
        layout.addWidget(QLabel("px"))

        # Связь сигналов
        self.width_spinbox.valueChanged.connect(self.update_canvas_size)
        self.height_spinbox.valueChanged.connect(self.update_canvas_size)

        return layout

    # Создание layout для выбора цвета
    def create_color_layout(self):
        layout = QVBoxLayout()

        # Кнопка выбора цвета
        self.color_button = QPushButton("Выбрать цвет")
        self.color_button.clicked.connect(self.open_color_dialog)
        layout.addWidget(self.color_button)

        # Метка текущего цвета
        self.user.Canvas.qtColor = canvas_entity.COLOR
        self.color_label = QLabel(f"Текущий цвет: {self.user.Canvas.qtColor.name()}")
        self.color_label.setStyleSheet(
            f"background-color: {self.user.Canvas.qtColor.name()}; padding: 10px;"
        )
        layout.addWidget(self.color_label)

        return layout

    # Метод для создания SpinBox с диапазоном и значением по умолчанию
    def _create_spinbox(self, min_value, max_value, default_value):
        spinbox = QSpinBox()
        spinbox.setRange(min_value, max_value)
        spinbox.setValue(default_value)
        return spinbox

