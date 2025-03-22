from anchor import Anchor
from oar import Oar


class Boat:
    def __init__(self):
        self.anchor = Anchor()
        self.left_oar = Oar(side="left")
        self.right_oar = Oar(side="right")
        self.is_anchored = False
        self.position = 0  # условная координата положения лодки

    def row_forward(self, strokes: int):
        if not self.is_anchored:
            self.position += strokes
            return f"Boat moved forward {strokes} strokes."
        return "Cannot move, anchor is down."

    def row_backward(self, strokes: int):
        if not self.is_anchored:
            self.position -= strokes
            return f"Boat moved backward {strokes} strokes."
        return "Cannot move, anchor is down."

    def drop_anchor(self):
        self.is_anchored = self.anchor.drop()
        return "Anchor dropped."

    def lift_anchor(self):
        self.is_anchored = not self.anchor.lift()
        return "Anchor lifted."
