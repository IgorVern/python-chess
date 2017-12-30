class Piece:
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
