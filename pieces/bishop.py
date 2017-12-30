from pieces.piece import Piece


class Bishop(Piece):
    def __init__(self, x, y):
        self.__move_directions = []
        super(Bishop, self).__init__(self.__move_directions, (x, y))
