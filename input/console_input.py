from exceptions import BoardOutOfBoundsException, InputValidationException
from .input import Input


class ConsoleInput(Input):
    def get_user_input(self, message):
        data = None

        while True:
            try:
                data = self.transform_input(input(message))
                break
            except InputValidationException:
                print('Wrong input format')

        x, y = data

        if x > 7 or x < 0 or y > 7 or y < 0:
            raise BoardOutOfBoundsException
        return data

    @staticmethod
    def get_pawn_promotion_input():
        message = 'Enter a piece name in what your pawn will be promoted (queen, knight, bishop or rook):'
        return input(message)
