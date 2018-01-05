from exceptions import WrongPieceException, EmptyCellException, BoardOutOfBoundsException
from pieces import Piece


class Player:
    def __init__(self, board, color):
        self.__board = board
        self.__color = color
        self.__picked_piece = None

    def pick_piece(self, piece):
        if not isinstance(piece, Piece):
            raise EmptyCellException

        if piece.get_color() is not self.__color:
            raise WrongPieceException()

        self.__picked_piece = piece

    def __validate_move(self, coordinates):
        x, y = coordinates

        if x < 0 or x > 7 or y < 0 or y > 7:
            raise BoardOutOfBoundsException()

    def move_piece(self, coordinates):
        piece = self.__picked_piece

        self.__board.remove_piece(piece.get_position())
        self.__picked_piece.move(coordinates)
        self.__board.add_piece(piece)

        self.__picked_piece = None

    def get_color(self):
        return self.__color
