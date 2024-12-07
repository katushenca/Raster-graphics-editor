from Entities.canvas_entity import Canvas
from Entities.Brush import Brush


class User:
    def __init__(self, canvas=Canvas(), brush=Brush()):
        self.Canvas = canvas
        self.Brush = brush
        self.main_window = None
