class Board:
    def __init__(self, x, o):
        self.x = x
        self.o = o
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def __repr__(self):
        return "==========\n" + self.board[0] + " | " + self.board[1] + " | " + self.board[2] + "\n" + self.board[
            3] + " | " + self.board[4] + " | " + self.board[5] + "\n" + self.board[6] + " | " + self.board[7] + " | " + \
               self.board[8] + "\n" + "=========="

    def add_to_board(self, move: int = -1, player: str = " "):
        if move == -1:
            return True

        if not self.is_taken(move):
            self.board[move] = player
            return False
        else:
            print("Place is already in use...")
            return True

    def is_taken(self, move):
        return self.board[move] != " "

