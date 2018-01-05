from board import Board
from player import Player
from const import Colors
from pieces import Piece, King, Pawn
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

            self.__move_piece(board, player, movement_paths)

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

    def __move_piece(self, board, player, movement_paths):
        while True:
            try:
                direction_coordinates = self.__input.get_user_input('Move piece:' + os.linesep)
            except BoardOutOfBoundsException:
                print('There is no such cell on board')
                continue

            if direction_coordinates not in movement_paths:
                print("You can't move here")
                continue

            if direction_coordinates in board:
                piece = board.get(direction_coordinates)

                if type(piece) is King:
                    self.__game_is_ended = True

                self.__board.remove_piece(direction_coordinates)

            player.move_piece(direction_coordinates)
            break

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
                if isinstance(board_cell, Piece):
                    if board_cell.get_color() == self.__current_player_color:
                        break
                    directions.append(possible_position)
                    break

                directions.append(possible_position)

        if type(piece) is Pawn:
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

            if cell.get_color() == Colors.black:
                enemy_coords.append(possible_enemy_coords)

        if self.__current_player_color == Colors.white:
            x, y = pawn.get_position()

            add_enemy((x - 1, y - 1))
            add_enemy((x + 1, y - 1))
        else:
            x, y = pawn.get_position()

            add_enemy((x - 1, y + 1))
            add_enemy((x + 1, y + 1))

        return enemy_coords

    @staticmethod
    def __are_coordinates_in_bounds(coordinates):
        x, y = coordinates
        return x < 8 or x >= 0 or y < 8 or y >= 0
