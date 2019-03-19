class Player:

    def __init__(self, name, xo):
        self.name = name
        self.xo = xo

    def __repr__(self):
        return self.name

    def move(self):
        move: int = input("It's your turn " + self.name + " type (1-9)")
        return int(move) - 1
