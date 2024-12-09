from Entities.canvas_entity import Canvas
from Entities.Brush import Brush
from Entities.Eraser import Eraser

class User:
    def __init__(self, canvas=Canvas(), brush=Brush(), eraser=Eraser()):
        self.Canvas = canvas
        self.Brush = brush
        self.main_window = None
        self.Eraser = eraser

        self.is_line_drawing = False
        self.lines_dots_count = 0

        self.previous_coord = None

        self.is_rect_drawing = False
        self.rectangle_dots_count = 0

        self.is_ellipse_drawing = False
        self.ellipse_dots_count = 0