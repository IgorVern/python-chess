def transform_coordinates(coordinates):
    """ Transform array coordinates into game coordinates """
    return chr(coordinates[0] + 97) + str(8 - coordinates[1])
