from pieces.piece import Piece


class Queen(Piece):
    def __init__(self, x, y):
        self.__move_directions = []
        super(Queen, self).__init__(self.__move_directions, (x, y))
