from PyQt6.QtGui import QPainter, QColor, QPen, QBrush


class Brush:
    def __init__(self, color=QColor(255, 255, 255)):
        self.color = color
        self.radius = 3
        self.is_chosen = False
