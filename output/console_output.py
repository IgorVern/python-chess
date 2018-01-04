import os
from .output import Output
from const import PiecesSymbols, Colors
from pieces import *


class ConsoleOutput(Output):

    def __init__(self):
        self.__symbols = PiecesSymbols()
        self.__picked_piece = None
        self.__highlighted_cells = None
        super(ConsoleOutput, self).__init__()

    def __get_row(self, row):
        result_row = []
        
        for cell in row:
            if cell is None:
                result_row.append(u'|   ')
                continue
    
            color = cell.get_color()
            pieces_symbols = PiecesSymbols.black if color == Colors.black else PiecesSymbols.white
    
            cell_prefix = '| '
            cell_suffix = ' '
            if type(cell) is King:
                result_row.append(cell_prefix + pieces_symbols['king'] + cell_suffix)
            elif type(cell) is Queen:
                result_row.append(cell_prefix + pieces_symbols['queen'] + cell_suffix)
            elif type(cell) is Rook:
                result_row.append(cell_prefix + pieces_symbols['rook'] + cell_suffix)
            elif type(cell) is Bishop:
                result_row.append(cell_prefix + pieces_symbols['bishop'] + cell_suffix)
            elif type(cell) is Knight:
                result_row.append(cell_prefix + pieces_symbols['knight'] + cell_suffix)
            elif type(cell) is Pawn:
                result_row.append(cell_prefix + pieces_symbols['pawn'] + cell_suffix)

        return result_row
        
    def get_output(self):
        row_numbers = tuple(9 - i for i in range(1, 9))
        line = '_' * 37
        letter_grid = '  | a | b | c | d | e | f | g | h | '
        output = [letter_grid, line]

        for index, row in enumerate(self.get_field()):
            row_number = str(row_numbers[index])
            transformed_row = [row_number + ' ']
            transformed_row.extend(self.__get_row(row))
            transformed_row.append('| ' + row_number)
            output.append(''.join(transformed_row))
            output.append(line)

        output.append(letter_grid)

        return os.linesep.join(output)

    def render(self):
        print(self.get_output())

    def update_field(self, board, picked_piece=None, highlighted_cells=None):
        field = list(self.get_empty_field())
        self.__picked_piece = picked_piece
        self.__highlighted_cells = highlighted_cells

        for coordinates, piece in board.items():
            x, y = coordinates
            field[y][x] = piece

        self.set_field(field)
