class Oar:
    def __init__(self, side: str):
        self.side = side
        self.in_use = False

    def use(self):
        self.in_use = True
        return f"{self.side.capitalize()} oar is used."

    def release(self):
        self.in_use = False
        return f"{self.side.capitalize()} oar is released."
