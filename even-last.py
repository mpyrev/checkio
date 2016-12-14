def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    return sum(array[::2]) * array[-1] if len(array) else 0
