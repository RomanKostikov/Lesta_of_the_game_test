class Anchor:
    def __init__(self):
        self.dropped = False

    def drop(self):
        self.dropped = True
        return self.dropped

    def lift(self):
        self.dropped = False
        return not self.dropped
