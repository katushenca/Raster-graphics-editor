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

class EraserSettingsWindow(QDialog):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setWindowTitle("Изменить Ластик")
        self.setMinimumSize(QSize(WIDTH, HEIGHT))

        main_layout = QVBoxLayout()

        # размер
        main_layout.addWidget(QLabel("Размер ластика:"))
        main_layout.addLayout(self.choose_size_layout())

        button = QPushButton("Изменить")
        main_layout.addWidget(button)

        button.clicked.connect(self.close)

        main_layout.addStretch()
        self.setLayout(main_layout)

    def choose_size_layout(self):
        layout = QVBoxLayout()
        # Ползунок
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(1, 10)
        self.slider.setValue(self.user.Eraser.radius)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.valueChanged.connect(self.update_size)
        layout.addWidget(self.slider)
        return layout

    def update_size(self, value):
        self.user.Eraser.radius = value