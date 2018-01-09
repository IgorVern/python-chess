from .piece import Piece


class Bishop(Piece):
    def __init__(self, coordinates, color):
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        super(Bishop, self).__init__(directions, coordinates, color)
