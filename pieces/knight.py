from .piece import Piece


class Knight(Piece):
    def __init__(self, board, coordinates, color):
        directions = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
        super(Knight, self).__init__(board, directions, coordinates, color, 1)
