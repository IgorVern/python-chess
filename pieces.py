class Piece(object):
    def __init__(self, possible_directions, coordinates, color):
        self.__alive = True
        self.__did_move = False
        self.__possible_directions = possible_directions
        self.__coordinates = coordinates
        self.color = color

    def is_alive(self):
        return self.__alive

    def die(self):
        self.__alive = False

    def move(self, x, y):
        if not self.__did_move:
            self.__did_move = True

        self.__coordinates = (x, y)

    def get_color(self):
        return self.color


class Bishop(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = []
        super(Bishop, self).__init__(self.__move_directions, coordinates, color)


class King(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = []
        super(King, self).__init__(self.__move_directions, coordinates, color)


class Knight(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = []
        super(Knight, self).__init__(self.__move_directions, coordinates, color)


class Pawn(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = []
        super(Pawn, self).__init__(self.__move_directions, coordinates, color)


class Queen(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = []
        super(Queen, self).__init__(self.__move_directions, coordinates, color)


class Rook(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = []
        super(Rook, self).__init__(self.__move_directions, coordinates, color)
