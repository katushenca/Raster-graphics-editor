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
