from .input import Input


class ConsoleInput(Input):
    def get_user_input(self):
        data = self.transform_input(input())
        return data
