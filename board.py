from const import Colors
import pieces


class Board:
    def __init__(self):
        in_game_pieces = {}

        """fill board with white pieces"""
        color = Colors.white
        for x in range(0, 8):
            coords = (x, 1)
            in_game_pieces[coords] = pieces.Pawn(coords, color)

        in_game_pieces[(0, 0)] = pieces.Rook((0, 0), color)
        in_game_pieces[(7, 0)] = pieces.Rook((7, 0), color)

        in_game_pieces[(1, 0)] = pieces.Knight((1, 0), color)
        in_game_pieces[(6, 0)] = pieces.Knight((6, 0), color)

        in_game_pieces[(2, 0)] = pieces.Bishop((2, 0), color)
        in_game_pieces[(5, 0)] = pieces.Bishop((5, 0), color)
        
        in_game_pieces[(3, 0)] = pieces.King((3, 0), color)
        
        in_game_pieces[(4, 0)] = pieces.Queen((4, 0), color)
        
        """fill board with black pieces"""
        color = Colors.black
        for x in range(0, 8):
            coords = (x, 6)
            in_game_pieces[coords] = pieces.Pawn(coords, color)

        in_game_pieces[(0, 7)] = pieces.Rook((0, 7), color)
        in_game_pieces[(7, 7)] = pieces.Rook((7, 7), color)

        in_game_pieces[(1, 7)] = pieces.Knight((1, 7), color)
        in_game_pieces[(6, 7)] = pieces.Knight((6, 7), color)

        in_game_pieces[(2, 7)] = pieces.Bishop((2, 7), color)
        in_game_pieces[(5, 7)] = pieces.Bishop((5, 7), color)
        
        in_game_pieces[(3, 7)] = pieces.King((3, 7), color)
        
        in_game_pieces[(4, 7)] = pieces.Queen((4, 7), color)

        self.__pieces = in_game_pieces

    def get_pieces(self):
        return self.__pieces
