from exceptions import InputValidationException
import re


class Input(object):
    def __init__(self):
        pass

    @staticmethod
    def transform_input(coords):
        """replace chars with ints"""
        if len(coords) is not 2:
            raise InputValidationException

        column, row = coords

        if not row.isdigit():
            raise InputValidationException

        if not re.match('^[A-Ha-h]', column):
            raise InputValidationException

        if int(row) not in range(1, 9):
            raise InputValidationException

        column = column.replace(column, str(ord(column) - 96), 1)
        return tuple([int(column) - 1, 8 - int(row)])
