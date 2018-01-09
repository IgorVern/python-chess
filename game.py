import pieces
from board import Board
from player import Player
from const import Colors
from exceptions import *
from utils import transform_coordinates
import os


class Game:
    def __init__(self, user_output, user_input):
        board = Board()
        self.__board = board
        self.__output = user_output
        self.__input = user_input
        self.__players = {Colors.white: Player(board, Colors.white), Colors.black: Player(board, Colors.black)}
        self.__current_player_color = Colors.white
        self.__game_is_ended = False
        self.__en_passant_pawn = None
        self.__pawn_was_promoted = False
        print(os.linesep)
        print('===== Welcome to python chess! =====')
        print(os.linesep)

    def start_game(self):
        while True:
            board = self.__board.get_board()
            player = self.__players.get(self.__current_player_color)

            self.__output.render(board)

            print(self.__current_player_color + ' player turn')

            piece = self.__get_piece(board, player)

            movement_paths = self.__compute_movement_paths(board, piece)

            self.__output.render(board, piece, movement_paths)

            self.__move_piece(board, piece, player, movement_paths)

            if self.__game_is_ended:
                print(self.__current_player_color + ' wins')
                break

            self.__switch_player()

    # TODO   move cell validation logic in game class. Game rules determine players behavior
    def __get_piece(self, board, player):
        while True:
            try:
                piece_coordinates = self.__input.get_user_input('Pick a piece:' + os.linesep)
            except BoardOutOfBoundsException:
                print('There is no such cell on board')
                continue

            piece = board.get(piece_coordinates)

            try:
                player.pick_piece(piece)
                return piece
            except WrongPieceException:
                print(transform_coordinates(piece_coordinates) + ' is not your piece')
            except EmptyCellException:
                print('There is no piece at ' + transform_coordinates(piece_coordinates))

    def __move_piece(self, board, piece, player, movement_paths):
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
                player.move_piece(target_position)

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
            en_passant_coords = (x, y - 1 if self.__current_player_color == Colors.white else y + 1)
            if en_passant_coords in movement_paths:
                tp = en_passant_coords
                self.__board.remove_piece((x, y))
                print('Capture ' + transform_coordinates((x, y)) + ' en passant')

        return tp

    def __promote_pawn(self, pawn, target_position):
        x, y = target_position
        color = self.__current_player_color

        if y == 0 or y == 7:
            while True:
                piece_name = self.__input.get_pawn_promotion_input().lower()
                new_piece = None
                if piece_name == 'queen':
                    new_piece = pieces.Queen(target_position, color)
                elif piece_name == 'knight':
                    new_piece = pieces.Knight(target_position, color)
                elif piece_name == 'rook':
                    new_piece = pieces.Rook(target_position, color)
                elif piece_name == 'bishop':
                    new_piece = pieces.Bishop(target_position, color)
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

    def __switch_player(self):
        self.__current_player_color = Colors.white if self.__current_player_color == Colors.black else Colors.black

    def __compute_movement_paths(self, board, piece):
        movement_directions = piece.get_movement_directions()
        step = piece.get_step()
        current_position = piece.get_position()
        directions = []

        for direction in movement_directions:
            possible_position = current_position
            x, y = direction
            for i in range(0, step):
                x1, y1 = possible_position
                possible_position = (x1 + x, y1 + y)

                if not self.__are_coordinates_in_bounds(possible_position):
                    break

                board_cell = board.get(possible_position)
                if isinstance(board_cell, pieces.Piece):
                    if board_cell.get_color() == self.__current_player_color:
                        break
                    if type(board_cell) is pieces.Pawn:
                        break
                    directions.append(possible_position)
                    break

                directions.append(possible_position)

        if type(piece) is pieces.Pawn:
            enemy_coords = self.__get_pawn_enemy_coordinates(piece, board)
            directions.extend(enemy_coords)

        return directions

    def __get_pawn_enemy_coordinates(self, pawn, board):
        enemy_coords = []

        def add_enemy(possible_enemy_coords):
            if not self.__are_coordinates_in_bounds(possible_enemy_coords):
                return

            cell = board.get(possible_enemy_coords)
            if cell is None:
                return

            if cell.get_color() != self.__current_player_color:
                enemy_coords.append(possible_enemy_coords)

        if self.__current_player_color == Colors.white:
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
                en_passant_hit_direction = (x - 1, y - 1 if self.__current_player_color == Colors.white else y + 1)
            elif en_passant_coords == (x + 1, y):
                en_passant_hit_direction = (x + 1, y - 1 if self.__current_player_color == Colors.white else y + 1)

            if en_passant_hit_direction and en_passant_hit_direction not in enemy_coords:
                enemy_coords.append(en_passant_hit_direction)

        return enemy_coords

    def __get_castling_positions(self, king, board):
        castling_positions = []
        color = self.__current_player_color

        if king.is_moved():
            return castling_positions

        rooks = {k: v for k, v in board.items() if type(v) is pieces.Rook
                 and not v.is_moved() and v.get_color() == color}
        rooks = list(rooks.values())

        print(rooks)
        if not rooks:
            return castling_positions

        return castling_positions

    @staticmethod
    def __are_coordinates_in_bounds(coordinates):
        x, y = coordinates
        return x < 8 or x >= 0 or y < 8 or y >= 0
