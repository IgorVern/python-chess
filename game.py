import pieces
from board import Board
from const import Colors
from exceptions import *
from utils import transform_coordinates, are_coordinates_in_bounds
import os


class Game:
    def __init__(self, user_output, user_input):
        board = Board()
        board.fill_board()
        self.__board = board
        self.__output = user_output
        self.__input = user_input
        self.__current_turn_color = Colors.white
        self.__game_is_ended = False
        self.__en_passant_pawn = None
        self.__pawn_was_promoted = False
        self.__picked_piece = None
        print(os.linesep)
        print('===== Welcome to python chess! =====')
        print(os.linesep)

    def start(self):
        while True:
            on_board_pieces = self.__board.get_on_board_pieces()

            self.__output.render(on_board_pieces)

            print(self.__current_turn_color + ' player turn')

            self.__pick_piece()

            piece = self.__picked_piece

            movement_paths = piece.get_available_cells()
            if not movement_paths:
                print('No available moves for ' + str(piece))
                self.__picked_piece = None
                continue

            self.__output.render(on_board_pieces, piece, movement_paths)

            self.__move_piece(on_board_pieces, movement_paths)

            if self.__game_is_ended:
                print(self.__current_turn_color + ' wins')
                break

            self.__switch_turn()

    def __pick_piece(self):
        on_board_pieces = self.__board.get_on_board_pieces()

        while True:
            try:
                piece_coordinates = self.__input.get_user_input('Pick a piece:' + os.linesep)
            except BoardOutOfBoundsException:
                print('There is no such cell on board')
                continue

            piece = on_board_pieces.get(piece_coordinates)

            if not isinstance(piece, pieces.Piece):
                print('There is no piece at ' + transform_coordinates(piece_coordinates))
                continue

            if piece.get_color() is not self.__current_turn_color:
                print(transform_coordinates(piece_coordinates) + ' is not your piece')
                continue

            self.__picked_piece = piece
            break

    def __move_piece(self, board, movement_paths):
        piece = self.__picked_piece
        while True:
            try:
                target_position = self.__input.get_user_input('Move piece:' + os.linesep)
            except BoardOutOfBoundsException:
                print('There is no such cell on board')
                continue

            if target_position not in movement_paths:
                print("You can't move here")
                continue

            self.__kill_someone(board, target_position)

            if type(piece) is pieces.Pawn:
                target_position = self.__get_pawn_eventual_position(movement_paths, target_position)
                self.__set_en_passant_piece(piece, target_position)
                self.__promote_pawn(piece, target_position)
            else:
                self.__en_passant_pawn = None

            if self.__pawn_was_promoted:
                self.__pawn_was_promoted = False
            else:
                piece.move(target_position)

            self.__picked_piece = None
            break

    def __kill_someone(self, board, target_position):
        if target_position in board:
            target_cell = board.get(target_position)

            if type(target_cell) is pieces.King:
                self.__game_is_ended = True

            self.__board.remove_piece(target_position)

    def __get_pawn_eventual_position(self, movement_paths, target_position):
        tp = target_position
        """determine if there was an en passant move"""
        if self.__en_passant_pawn:
            x, y = self.__en_passant_pawn.get_position()
            en_passant_coords = (x, y - 1 if self.__current_turn_color == Colors.white else y + 1)
            if en_passant_coords in movement_paths:
                tp = en_passant_coords
                self.__board.remove_piece((x, y))
                print('Capture ' + transform_coordinates((x, y)) + ' en passant')

        return tp

    def __promote_pawn(self, pawn, target_position):
        x, y = target_position
        color = self.__current_turn_color
        board = self.__board
        if y == 0 or y == 7:
            while True:
                piece_name = self.__input.get_pawn_promotion_input().lower()
                new_piece = None
                if piece_name == 'queen':
                    new_piece = pieces.Queen(board, target_position, color)
                elif piece_name == 'knight':
                    new_piece = pieces.Knight(board, target_position, color)
                elif piece_name == 'rook':
                    new_piece = pieces.Rook(board, target_position, color)
                elif piece_name == 'bishop':
                    new_piece = pieces.Bishop(board, target_position, color)
                else:
                    print('Invalid piece name')
                    continue
                self.__board.remove_piece(pawn.get_position())
                self.__board.add_piece(new_piece)
                self.__pawn_was_promoted = True
                break

    def __set_en_passant_piece(self, pawn, target_position):
        """is piece suitable for en passant move"""
        current_position = pawn.get_position()
        self.__en_passant_pawn = pawn if abs(target_position[1] - current_position[1]) == 2 else None

    def __switch_turn(self):
        self.__current_turn_color = Colors.white if self.__current_turn_color == Colors.black else Colors.black


    def __get_pawn_enemy_coordinates(self, pawn, board):
        enemy_coords = []

        def add_enemy(possible_enemy_coords):
            if not are_coordinates_in_bounds(possible_enemy_coords):
                return

            cell = board.get(possible_enemy_coords)
            if cell is None:
                return

            if cell.get_color() != self.__current_turn_color:
                enemy_coords.append(possible_enemy_coords)

        if self.__current_turn_color == Colors.white:
            x, y = pawn.get_position()

            add_enemy((x - 1, y - 1))
            add_enemy((x + 1, y - 1))
        else:
            x, y = pawn.get_position()

            add_enemy((x - 1, y + 1))
            add_enemy((x + 1, y + 1))

        """compute pawn en passant move"""
        if self.__en_passant_pawn is not None:
            current_position = pawn.get_position()
            en_passant_hit_direction = None
            x, y = current_position
            en_passant_coords = self.__en_passant_pawn.get_position()
            if en_passant_coords == (x - 1, y):
                en_passant_hit_direction = (x - 1, y - 1 if self.__current_turn_color == Colors.white else y + 1)
            elif en_passant_coords == (x + 1, y):
                en_passant_hit_direction = (x + 1, y - 1 if self.__current_turn_color == Colors.white else y + 1)

            if en_passant_hit_direction and en_passant_hit_direction not in enemy_coords:
                enemy_coords.append(en_passant_hit_direction)

        return enemy_coords

    def __get_castling_positions(self, king, board):
        castling_positions = []
        color = self.__current_turn_color

        if king.is_moved():
            return castling_positions

        rooks = {k: v for k, v in board.items() if type(v) is pieces.Rook
                 and not v.is_moved() and v.get_color() == color}
        rooks = list(rooks.values())

        print(rooks)
        if not rooks:
            return castling_positions

        return castling_positions
