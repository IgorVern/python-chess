from exceptions import WrongPieceException, EmptyCellException
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

