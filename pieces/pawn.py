from pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = []
        super(Pawn, self).__init__(self.__move_directions, coordinates, color)
