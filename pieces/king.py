from .piece import Piece


class King(Piece):
    def __init__(self, coordinates, color):
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        super(King, self).__init__(directions, coordinates, color, 1)
        