from pieces.piece import Piece


class King(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = []
        super(King, self).__init__(self.__move_directions, coordinates, color)
