from .piece import Piece
from const import Colors


class Pawn(Piece):
    def __init__(self, board, coordinates, color):
        directions = [(0, 1)] if color == Colors.black else [(0, -1)]
        super(Pawn, self).__init__(board, directions, coordinates, color, 2)

    def move(self, coordinates):
        did_move = self.is_moved()
        if not did_move:
            self.set_step(1)

        super(Pawn, self).move(coordinates)
