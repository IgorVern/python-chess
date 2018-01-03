class Piece(object):
    def __init__(self, possible_directions, coordinates, color):
        self.__alive = True
        self.__did_move = False
        self.__possible_directions = possible_directions
        self.__coordinates = coordinates
        self.__color = color

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

    def set_move_directions(self, directions):
        self.__possible_directions = directions

    def is_moved(self):
        return self.__did_move


class Bishop(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                                  (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7),
                                  (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),
                                  (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7)]
        super(Bishop, self).__init__(self.__move_directions, coordinates, color)


class King(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        super(King, self).__init__(self.__move_directions, coordinates, color)


class Knight(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
        super(Knight, self).__init__(self.__move_directions, coordinates, color)


class Pawn(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = [(0, 1), (0, 2)]
        super(Pawn, self).__init__(self.__move_directions, coordinates, color)

    def move(self, coordinates):
        did_move = self.is_moved()
        if not did_move:
            self.set_move_directions([(0, 1)])

        super(Pawn, self).move(coordinates)


class Queen(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
                                  (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7),
                                  (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),
                                  (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7),
                                  (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                  (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0),
                                  (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                                  (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7)]
        super(Queen, self).__init__(self.__move_directions, coordinates, color)


class Rook(Piece):
    def __init__(self, coordinates, color):
        self.__move_directions = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                  (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0),
                                  (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                                  (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7)]
        super(Rook, self).__init__(self.__move_directions, coordinates, color)
