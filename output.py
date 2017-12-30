import os


class Output(object):
    __empty_row = [None, None, None, None, None, None, None, None]

    def __init__(self):
        field = []
        for i in range(0, 8):
            field.append(list(self.__empty_row))
        self.__field = field

    def get_field(self):
        return self.__field

    def update_field(self, board):
        pass

    def get_output(self):
        pass


class ConsoleOutput(Output):
    def __init__(self):
        super(ConsoleOutput, self).__init__()

    @staticmethod
    def __transform_cell(cell):
        if cell is None:
            return '|  '

    def get_output(self):
        line = '_' * 23
        letter_grid = ' a  b  c  d  e  f  g  h  '
        output = [letter_grid, line]

        for row in self.get_field():
            transformed_row = list(map(self.__transform_cell, row))
            output.append(''.join(transformed_row))
            output.append(line)

        output.append(letter_grid)

        return os.linesep.join(output)

    def render(self):
        print(self.get_output())
