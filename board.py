from const import Colors
import pieces


class Board:
    def __init__(self):
        self.__on_board_pieces = None

    def get_on_board_pieces(self):
        return self.__on_board_pieces

    def remove_piece(self, piece_coords):
        self.__on_board_pieces.pop(piece_coords)

    def add_piece(self, piece):
        self.__on_board_pieces[piece.get_position()] = piece

    def fill_board(self):
        in_game_pieces = {}

        """fill board with black pieces"""
        color = Colors.black
        for x in range(0, 8):
            coords = (x, 1)
            in_game_pieces[coords] = pieces.Pawn(self, coords, color)

        in_game_pieces[(0, 0)] = pieces.Rook(self, (0, 0), color)
        in_game_pieces[(7, 0)] = pieces.Rook(self, (7, 0), color)

        in_game_pieces[(1, 0)] = pieces.Knight(self, (1, 0), color)
        in_game_pieces[(6, 0)] = pieces.Knight(self, (6, 0), color)

        in_game_pieces[(2, 0)] = pieces.Bishop(self, (2, 0), color)
        in_game_pieces[(5, 0)] = pieces.Bishop(self, (5, 0), color)

        in_game_pieces[(3, 0)] = pieces.King(self, (3, 0), color)

        in_game_pieces[(4, 0)] = pieces.Queen(self, (4, 0), color)

        """fill board with white pieces"""
        color = Colors.white
        for x in range(0, 8):
            coords = (x, 6)
            in_game_pieces[coords] = pieces.Pawn(self, coords, color)

        in_game_pieces[(0, 7)] = pieces.Rook(self, (0, 7), color)
        in_game_pieces[(7, 7)] = pieces.Rook(self, (7, 7), color)

        in_game_pieces[(1, 7)] = pieces.Knight(self, (1, 7), color)
        in_game_pieces[(6, 7)] = pieces.Knight(self, (6, 7), color)

        in_game_pieces[(2, 7)] = pieces.Bishop(self, (2, 7), color)
        in_game_pieces[(5, 7)] = pieces.Bishop(self, (5, 7), color)

        in_game_pieces[(3, 7)] = pieces.King(self, (3, 7), color)

        in_game_pieces[(4, 7)] = pieces.Queen(self, (4, 7), color)

        """
            board is represented as a dictionary where values is a piece object, key - its coordinates tuple
        """
        self.__on_board_pieces = in_game_pieces
