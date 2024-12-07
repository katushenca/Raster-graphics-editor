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
        self.previous_pos = None

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
            self.previous_pos = self.mapToScene(event.pos())
            self.DrawPixels(self.previous_pos, self.previous_pos)

    def mouseMoveEvent(self, event):
        if self.is_drawing:
            current_pos = self.mapToScene(event.pos())
            self.DrawPixels(self.previous_pos, current_pos)
            self.previous_pos = current_pos

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_drawing = False
            self.previous_pos = None

    def DrawPixels(self, start_pos, end_pos):
        x1, y1 = start_pos.x(), start_pos.y()
        x2, y2 = end_pos.x(), end_pos.y()

        steps = int(max(abs(x2 - x1), abs(y2 - y1)))
        if steps == 0:
            self.scene.addRect(QRectF(x1, y1, 1, 1),
                               pen=QPen(Qt.PenStyle.NoPen),
                               brush=QBrush(self.user.Brush.color))
            return

        dx = (x2 - x1) / steps
        dy = (y2 - y1) / steps
        for i in range(steps + 1):
            px = x1 + i * dx
            py = y1 + i * dy
            self.scene.addRect(QRectF(px, py, 1, 1),
                               pen=QPen(Qt.PenStyle.NoPen),
                               brush=QBrush(self.user.Brush.color))

    def wheelEvent(self, event):
        event.ignore()
