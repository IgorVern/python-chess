from output import ConsoleOutput
from board import Board


def start_game():
    board = Board()
    output = ConsoleOutput()

    output.render()


start_game()
