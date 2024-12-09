from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QFrame
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush
from PyQt6.QtCore import Qt, QSize, QPointF, QRectF


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
            scene_pos = self.mapToScene(event.pos())

            if self.user.Brush.is_chosen:
                self.is_drawing = True
                self.previous_pos = scene_pos
                self.draw_pixels(self.previous_pos, self.previous_pos)
            elif self.user.Eraser.is_chosen:
                self.remove_pixels(event)
            elif self.user.is_line_drawing:
                if self.user.lines_dots_count == 0:
                    self.user.previous_coord = scene_pos
                    self.user.lines_dots_count = 1
                elif self.user.lines_dots_count == 1:
                    self.draw_line(self.user.previous_coord, scene_pos)
                    self.user.previous_coord = None
                    self.user.lines_dots_count = 0
            elif self.user.is_rect_drawing:
                if self.user.rectangle_dots_count == 0:
                    self.user.previous_coord = scene_pos
                    self.user.rectangle_dots_count = 1
                elif self.user.rectangle_dots_count == 1:
                    self.draw_rectangle(self.user.previous_coord, scene_pos)
                    self.user.previous_coord = None
                    self.user.rectangle_dots_count = 0
            elif self.user.is_ellipse_drawing:
                if self.user.ellipse_dots_count == 0:
                    self.user.previous_coord = scene_pos
                    self.user.ellipse_dots_count = 1
                elif self.user.ellipse_dots_count == 1:
                    self.draw_ellipse(self.user.previous_coord, scene_pos)
                    self.user.previous_coord = None
                    self.user.ellipse_dots_count = 0

    def mouseMoveEvent(self, event):
        if self.is_drawing and self.user.Brush.is_chosen:
            current_pos = self.mapToScene(event.pos())
            self.draw_pixels(self.previous_pos, current_pos)
            self.previous_pos = current_pos
        elif self.user.Eraser.is_chosen:
            self.remove_pixels(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_drawing = False
            self.previous_pos = None

    def draw_pixels(self, start_pos, end_pos):
        x1, y1 = start_pos.x(), start_pos.y()
        x2, y2 = end_pos.x(), end_pos.y()
        radius = self.user.Brush.radius
        steps = int(max(abs(x2 - x1), abs(y2 - y1)))

        dx = (x2 - x1) / steps if steps else 0
        dy = (y2 - y1) / steps if steps else 0

        for i in range(steps + 1):
            px = x1 + i * dx
            py = y1 + i * dy
            self.scene.addRect(px, py, radius, radius,
                               pen=QPen(Qt.PenStyle.NoPen),
                               brush=QBrush(self.user.Brush.color))

    def draw_line(self, start_pos, end_pos):
        line = self.scene.addLine(start_pos.x(), start_pos.y(),
                                  end_pos.x(), end_pos.y(),
                                  pen=QPen(self.user.Brush.color, self.user.Brush.radius))

    def draw_rectangle(self, start_pos, end_pos):
        x1, y1 = start_pos.x(), start_pos.y()
        x2, y2 = end_pos.x(), end_pos.y()
        rect = QRectF(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
        self.scene.addRect(rect, pen=QPen(self.user.Brush.color,
                                          self.user.Brush.radius),
                           brush=QBrush(
                               self.user.Brush.color))

    def draw_ellipse(self, start_pos, end_pos):
        x1, y1 = start_pos.x(), start_pos.y()
        x2, y2 = end_pos.x(), end_pos.y()
        rect = QRectF(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
        self.scene.addEllipse(rect, pen=QPen(self.user.Brush.color,
                                             self.user.Brush.radius),
                              brush=QBrush(self.user.Brush.color))

    def remove_pixels(self, event):
        scene_pos = self.mapToScene(event.pos())
        radius = self.user.Eraser.radius
        rect = QRectF(scene_pos.x() - radius, scene_pos.y() - radius,
                      radius * 2, radius * 2)
        for item in self.scene.items(rect):
            if item is not None:
                self.scene.removeItem(item)
