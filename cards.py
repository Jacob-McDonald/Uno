class StandardCards:
    def __init__(self, c, n):
        self.color = c
        self.number = n

    def as_string(self):
        return self.color + " " + str(self.number)

class WildCard:
    def __init__(self):
        self.is_draw_4 = False

    def as_string(self):
        if self.is_draw_4 == False:
            return "Wild"
        else:
            return "Wild Draw 4"

class ReversCard:
    def __init__(self, c):
        self.color = c

    def as_string(self):
        return self.color + "Reverse"

class SkipCard:
    def __init__(self, c):
        self.color = c

    def as_string(self):
        return self.color + "Skip"

class DrawCard:
    def __init__(self, c):
        DrawCard.color = c

    def as_string(self):
        return self.color + " Draw 2 "