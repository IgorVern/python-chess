class Piece(object):
    def __init__(self, board, directions, coordinates, color, step=7):
        self.__did_move = False
        self.__directions = directions
        self.__coordinates = coordinates
        self.__color = color
        self.__step = step
        self.__board = board

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
