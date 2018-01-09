def are_coordinates_in_bounds(coordinates):
    x, y = coordinates
    return x < 8 or x >= 0 or y < 8 or y >= 0
