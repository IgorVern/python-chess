import os
from .output import Output
from const import PiecesSymbols, Colors
from pieces import *


class ConsoleOutput(Output):

    def __init__(self):
        self.__symbols = PiecesSymbols()
        super(ConsoleOutput, self).__init__()

    @staticmethod
    def __transform_cell(cell):
        if cell is None:
            return u'|   '
        color = cell.get_color()

        pieces_symbols = PiecesSymbols.black if color == Colors.black else PiecesSymbols.white

        if type(cell) is King:
            return '| ' + pieces_symbols['king'] + ' '
        elif type(cell) is Queen:
            return '| ' + pieces_symbols['queen'] + ' '
        elif type(cell) is Rook:
            return '| ' + pieces_symbols['rook'] + ' '
        elif type(cell) is Bishop:
            return '| ' + pieces_symbols['bishop'] + ' '
        elif type(cell) is Knight:
            return '| ' + pieces_symbols['knight'] + ' '
        elif type(cell) is Pawn:
            return '| ' + pieces_symbols['pawn'] + ' '

    def get_output(self):
        row_numbers = tuple(9 - i for i in range(1, 9))
        line = '_' * 37
        letter_grid = '  | a | b | c | d | e | f | g | h | '
        output = [letter_grid, line]

        for index, row in enumerate(self.get_field()):
            row_number = str(row_numbers[index])
            transformed_row = [row_number + ' ']
            transformed_row.extend(list(map(self.__transform_cell, row)))
            transformed_row.append('| ' + row_number)
            output.append(''.join(transformed_row))
            output.append(line)

        output.append(letter_grid)

        return os.linesep.join(output)

    def render(self):
        print(self.get_output())

    def update_field(self, board, picked_piece=None, highlighted_cells=None):
        field = list(self.get_empty_field())

        for coordinates, piece in board.items():
            x, y = coordinates
            field[y][x] = piece

        self.set_field(field)
