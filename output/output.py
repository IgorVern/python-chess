class Output(object):
    __empty_row = [None, None, None, None, None, None, None, None]

    def __init__(self):
        field = []
        for i in range(0, 8):
            field.append(list(self.__empty_row))
        self.__field = field

    def get_field(self):
        return self.__field

    def get_empty_field(self):
        field = []
        for i in range(0, 8):
            field.append(list(self.__empty_row))
        return field

    def set_field(self, field):
        self.__field = field

    def update_field(self, board):
        pass

    def get_output(self):
        pass
