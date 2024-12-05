from Entities.canvas_entity import Canvas


class User:
    def __init__(self, canvas=Canvas()):
        self.Canvas = canvas
        self.main_window = None

