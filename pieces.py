from const import Colors


class Piece(object):
    def __init__(self, directions, coordinates, color, step=7):
        self.__alive = True
        self.__did_move = False
        self.__directions = directions
        self.__coordinates = coordinates
        self.__color = color
        self.__step = step

    def is_alive(self):
        return self.__alive

    def die(self):
        self.__alive = False

    def get_color(self):
        return self.__color

    def get_position(self):
        return self.__coordinates

    def move(self, coordinates):
        if not self.__did_move:
            self.__did_move = True

        self.__coordinates = coordinates

    def set_movement_directions(self, directions):
        self.__directions = directions

    def get_movement_directions(self):
        return self.__directions

    def is_moved(self):
        return self.__did_move

    def set_step(self, step):
        self.__step = step

    def get_step(self):
        return self.__step


class Bishop(Piece):
    def __init__(self, coordinates, color):
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        super(Bishop, self).__init__(directions, coordinates, color)


class King(Piece):
    def __init__(self, coordinates, color):
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        super(King, self).__init__(directions, coordinates, color, 1)


class Knight(Piece):
    def __init__(self, coordinates, color):
        directions = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
        super(Knight, self).__init__(directions, coordinates, color, 1)


class Pawn(Piece):
    def __init__(self, coordinates, color):
        directions = [(0, 1)] if color == Colors.black else [(0, -1)]
        super(Pawn, self).__init__(directions, coordinates, color, 2)

    def move(self, coordinates):
        did_move = self.is_moved()
        if not did_move:
            self.set_step(1)

        super(Pawn, self).move(coordinates)


class Queen(Piece):
    def __init__(self, coordinates, color):
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        super(Queen, self).__init__(directions, coordinates, color)


class Rook(Piece):
    def __init__(self, coordinates, color):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        super(Rook, self).__init__(directions, coordinates, color)
