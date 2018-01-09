from .piece import Piece


class Rook(Piece):
    def __init__(self, coordinates, color):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        super(Rook, self).__init__(directions, coordinates, color)
