from utils import are_coordinates_in_bounds, transform_coordinates


class Piece(object):
    def __init__(self, board, directions, coordinates, color, step=7):
        self.__did_move = False
        self.__directions = directions
        self.__coordinates = coordinates
        self.__color = color
        self.__step = step
        self.__board = board

    def __str__(self):
        return type(self).__name__ + ' position: ' + transform_coordinates(self.__coordinates)

    def get_color(self):
        return self.__color

    def get_position(self):
        return self.__coordinates

    def move(self, coordinates):
        if not self.__did_move:
            self.__did_move = True

        self.__board.remove_piece(self.__coordinates)
        self.__coordinates = coordinates
        self.__board.add_piece(self)

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

    def get_board(self):
        return self.__board

    def get_available_cells(self):
        board = self.__board.get_on_board_pieces()
        movement_directions = self.__directions
        step = self.__step
        current_position = self.__coordinates
        directions = []

        for direction in movement_directions:
            possible_position = current_position
            x, y = direction
            for i in range(0, step):
                x1, y1 = possible_position
                possible_position = (x1 + x, y1 + y)
                if not are_coordinates_in_bounds(possible_position):
                    break

                board_cell = board.get(possible_position)
                if isinstance(board_cell, Piece):
                    if board_cell.get_color() == self.__color:
                        break
                    directions.append(possible_position)
                    break

                directions.append(possible_position)

        return directions
