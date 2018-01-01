class Input(object):
    def __init__(self):
        pass

    @staticmethod
    def transform_input(data):
        coords = data.split()
        coordinates = []
        """replace chars with ints"""
        for c in coords:
            coordinates.append(int(c.replace(c[0], str(ord(c[0]) - 96), 1)))

        return tuple(coordinates)

    def get_user_input(self):
        pass
