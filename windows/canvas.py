from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QFrame
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QSize



class Canvas(QGraphicsView):
    def __init__(self, canvas_entity, parent=None):
        super().__init__(parent)
        self.canvas_entity = canvas_entity
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Настройки холста
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setFixedSize(QSize(canvas_entity.width, canvas_entity.height))
        self.setBackgroundBrush(canvas_entity.qtColor)

        # Убираем рамки
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setFrameShadow(QFrame.Shadow.Plain)
        self.setStyleSheet("border: none;")
        # Убираем внутренние отступы
        self.setContentsMargins(0, 0, 0, 0)

        # Отключаем скроллбары
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint |
                            Qt.WindowType.WindowStaysOnTopHint)