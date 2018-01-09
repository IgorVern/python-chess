from .piece import Piece
from const import Colors
from helpers import are_coordinates_in_bounds


class Pawn(Piece):
    def __init__(self, board, coordinates, color):
        directions = [(0, 1)] if color == Colors.black else [(0, -1)]
        super(Pawn, self).__init__(board, directions, coordinates, color, 2)

    def move(self, coordinates):
        did_move = self.is_moved()
        if not did_move:
            self.set_step(1)

        super(Pawn, self).move(coordinates)

    def get_available_cells(self):
        directions = super(Pawn, self).get_available_cells()
        pieces_positions = self.get_board().get_board()

        # filter out possible enemy coordinates at the next cell in front of pawn
        directions = list(filter(lambda coords: coords not in pieces_positions, directions))

        enemy_coords = self.__get_pawn_enemy_coordinates()
        directions.extend(enemy_coords)

        return directions

    def __get_pawn_enemy_coordinates(self, ):
        enemy_coords = []
        board = self.get_board().get_board()

        def add_enemy(possible_enemy_coords):
            if not are_coordinates_in_bounds(possible_enemy_coords):
                return

            cell = board.get(possible_enemy_coords)
            if cell is None:
                return

            if cell.get_color() != self.get_color():
                enemy_coords.append(possible_enemy_coords)

        if self.get_color() == Colors.white:
            x, y = self.get_position()

            add_enemy((x - 1, y - 1))
            add_enemy((x + 1, y - 1))
        else:
            x, y = self.get_position()

            add_enemy((x - 1, y + 1))
            add_enemy((x + 1, y + 1))

        # """compute pawn en passant move"""
        # if self.__en_passant_pawn is not None:
        #     current_position = pawn.get_position()
        #     en_passant_hit_direction = None
        #     x, y = current_position
        #     en_passant_coords = self.__en_passant_pawn.get_position()
        #     if en_passant_coords == (x - 1, y):
        #         en_passant_hit_direction = (x - 1, y - 1 if self.__color == Colors.white else y + 1)
        #     elif en_passant_coords == (x + 1, y):
        #         en_passant_hit_direction = (x + 1, y - 1 if self.__color == Colors.white else y + 1)
        #
        #     if en_passant_hit_direction and en_passant_hit_direction not in enemy_coords:
        #         enemy_coords.append(en_passant_hit_direction)

        return enemy_coords
