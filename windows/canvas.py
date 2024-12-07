from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QFrame
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush
from PyQt6.QtCore import Qt, QSize, QRectF


class Canvas(QGraphicsView):
    def __init__(self, canvas_entity, user, parent=None):
        super().__init__(parent)
        self.user = user
        self.is_drawing = False
        self.canvas_entity = canvas_entity
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setFixedSize(QSize(canvas_entity.width, canvas_entity.height))
        self.setBackgroundBrush(canvas_entity.qtColor)

        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setFrameShadow(QFrame.Shadow.Plain)
        self.setStyleSheet("border: none;")

        self.setContentsMargins(0, 0, 0, 0)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint |
                            Qt.WindowType.WindowStaysOnTopHint)

    def change(self, width, height, color):
        self.setFixedSize(QSize(width, height))
        self.setBackgroundBrush(color)
        self.canvas_entity.width = width
        self.canvas_entity.height = height
        self.canvas_entity.qtColor = color

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_drawing = True
            self.DrawPixels(event)

    def mouseMoveEvent(self, event):
        if self.is_drawing:
            self.DrawPixels(event)

    def DrawPixels(self, event):
        self.start_pos = self.mapToScene(event.pos())
        x, y = self.start_pos.x(), self.start_pos.y()
        pixel_size = 1
        self.scene.addRect(QRectF(x, y, pixel_size, pixel_size),
                           pen=QPen(Qt.PenStyle.NoPen),
                           brush=QBrush(self.user.Brush.color))

    def wheelEvent(self, event):
        event.ignore()
