from pieces.piece import Piece


class Queen(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = []
        super(Queen, self).__init__(self.__move_directions, coordinates, color)
