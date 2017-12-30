from board import Board
from output import ConsoleOutput


def start_game():
    board = Board()
    output = ConsoleOutput()

    output.update_field(board.get_pieces())
    output.render()


start_game()
