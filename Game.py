from Board import *
from Player import *

if __name__ == '__main__':
    game_over = False

    # x = input("Player X write your name: ")
    # o = input("Player O write your name: ")
    player_x = Player("Player X", "X")
    player_o = Player("Player O", "O")
    board = Board(x=player_x, o=player_o)

    turn_x = True
    turn_o = True
    while not game_over:
        print(board)
        while turn_x:
            move_x = player_x.move()
            turn_x = board.add_to_board(move_x, player_x.xo)
            print(board)
        turn_x = True
        while turn_o:
            move_o = player_o.move()
            turn_o = board.add_to_board(move_o, player_o.xo)
            print(board)
        turn_o = True

