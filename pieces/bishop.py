from pieces.piece import Piece


class Bishop(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = []
        super(Bishop, self).__init__(self.__move_directions, coordinates, color)
