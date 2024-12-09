from PyQt6.QtGui import QPainter, QColor, QPen, QBrush


class Eraser:
    def __init__(self):
        self.color = QColor(255, 255, 255)
        self.radius = 5
        self.is_chosen = False
