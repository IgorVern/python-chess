from .input import Input


class ConsoleInput(Input):
    def get_user_input(self, message):
        data = self.transform_input(input(message))
        return data
