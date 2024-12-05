from PyQt6.QtGui import QColor

# settings
WIDTH = 800
MIN_WIDTH = 1
MAX_WIDTH = 1280

HEIGHT = 400
MIN_HEIGHT = 1
MAX_HEIGHT = 1280

COLOR = QColor(255, 255, 255)


class Canvas:
    def __init__(self, width: int = 0, height: int = 0, color=QColor(255, 255, 255)):
        self.width = width
        self.height = height
        self.qtColor = color
