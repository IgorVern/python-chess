from pieces.piece import Piece


class Knight(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = []
        super(Knight, self).__init__(self.__move_directions, coordinates, color)