def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    return -1 if n > len(array)-1 else array[n] ** n
