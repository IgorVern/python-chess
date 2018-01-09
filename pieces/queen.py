from .piece import Piece


class Queen(Piece):
    def __init__(self, coordinates, color):
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        super(Queen, self).__init__(directions, coordinates, color)
