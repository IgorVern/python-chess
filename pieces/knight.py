from pieces.piece import Piece


class Knight(Piece):
    def __init__(self, x, y):
        self.__move_directions = []
        super(Knight, self).__init__(self.__move_directions, (x, y))
