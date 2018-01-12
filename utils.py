def transform_coordinates(coordinates):
    """ Transform array coordinates into game coordinates """
    return chr(coordinates[0] + 97) + str(8 - coordinates[1])


def are_coordinates_in_bounds(coordinates):
    x, y = coordinates
    return (8 > x >= 0) and (8 > y >= 0)
