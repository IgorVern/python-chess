from pieces.piece import Piece


class Rook(Piece):
    def __init__(self, x, y):
        self.__move_directions = []
        super(Rook, self).__init__(self.__move_directions, (x, y))
