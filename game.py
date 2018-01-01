from board import Board
from player import Player
from const import Colors
import os


class Game:
    def __init__(self, output):
        board = Board()
        self.__board = board
        self.__output = output
        self.__white_player = Player(board, Colors.white)
        self.__black_player = Player(board, Colors.black)
        print(os.linesep)
        print('===== Welcome to python chess! =====')
        print(os.linesep)

    def start_game(self):
        self.__output.update_field(self.__board.get_pieces())
        self.__output.render()
