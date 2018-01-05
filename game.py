from board import Board
from player import Player
from const import Colors
from pieces import Piece
import os


class Game:
    def __init__(self, user_output, user_input):
        board = Board()
        self.__board = board
        self.__output = user_output
        self.__input = user_input
        self.__players = {Colors.white: Player(board, Colors.white), Colors.black: Player(board, Colors.black)}
        self.__current_player_color = Colors.white
        self.__in_game = True
        print(os.linesep)
        print('===== Welcome to python chess! =====')
        print(os.linesep)

    def start_game(self):
        while self.__in_game:
            board = self.__board.get_board()
            player = self.__players.get(self.__current_player_color)

            self.__output.update_field(board)
            self.__output.render()

            print(player.get_color() + ' player turn')

            piece_coordinates = self.__input.get_user_input('Pick a piece:' + os.linesep)
            piece = board.get(piece_coordinates)

            player.pick_piece(piece)

            movement_paths = self.__compute_movement_paths(piece)

            print(movement_paths)

            self.__output.update_field(board, piece, movement_paths)
            self.__output.render()

            direction_coordinates = self.__input.get_user_input('Move piece:' + os.linesep)
            player.move_piece(direction_coordinates)

            self.__current_player_color = Colors.white if self.__current_player_color == Colors.black else Colors.black

    def __compute_movement_paths(self, piece):
        movement_directions = piece.get_movement_directions()
        step = piece.get_step()
        current_position = piece.get_position()
        board = self.__board.get_board()
        directions = []

        for direction in movement_directions:
            possible_position = current_position
            x, y = direction
            for i in range(0, step):
                x1, y1 = possible_position
                possible_position = (x1 + x, y1 + y)

                if self.__is_not_coordinates_in_bounds(possible_position):
                    break

                board_cell = board.get(possible_position)
                if isinstance(board_cell, Piece):
                    if board_cell.get_color() == self.__current_player_color:
                        break
                    directions.append(possible_position)
                    break

                directions.append(possible_position)

        return directions

    @staticmethod
    def __is_not_coordinates_in_bounds(coordinates):
        x, y = coordinates
        return x > 7 or x < 0 or y > 7 or y < 0
