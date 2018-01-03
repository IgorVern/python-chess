from board import Board
from player import Player
from const import Colors
import os


class Game:
    def __init__(self, user_output, user_input):
        board = Board()
        self.__board = board
        self.__output = user_output
        self.__input = user_input
        self.__players = {Colors.white: Player(board, Colors.white), Colors.black: Player(board, Colors.black)}
        self.__turn = Colors.white
        self.__in_game = True
        print(os.linesep)
        print('===== Welcome to python chess! =====')
        print(os.linesep)

    def start_game(self):
        while self.__in_game:
            pieces = self.__board.get_pieces()
            player = self.__players.get(self.__turn)

            self.__output.update_field(pieces)
            self.__output.render()

            print(player.get_color() + ' player turn')

            piece_coordinates = self.__input.get_user_input('Pick a piece:' + os.linesep)
            piece = pieces.get(piece_coordinates)

            player.pick_piece(piece)

            direction_coordinates = self.__input.get_user_input('Move piece:' + os.linesep)
            player.move_piece(direction_coordinates)

            self.__turn = Colors.white if self.__turn == Colors.black else Colors.black
