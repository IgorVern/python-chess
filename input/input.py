class Input(object):
    def __init__(self):
        pass

    @staticmethod
    def transform_input(coords):
        """replace chars with ints"""
        coords = coords.replace(coords[0], str(ord(coords[0]) - 96), 1)
        return tuple([int(coords[0]) - 1, 8 - int(coords[1])])
