from .piece import Piece


class Queen(Piece):
    def __init__(self, board, coordinates, color):
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        super(Queen, self).__init__(board, directions, coordinates, color)
