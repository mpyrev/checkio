def min(*args, **kwargs):
    key = kwargs.get("key", None)
    it = iter(args if len(args) > 1 else args[0])
    n = next(it)
    for i in it:
        a, b = (key(i), key(n)) if key is not None else (i, n)
        n = i if a < b else n
    return n


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    it = iter(args if len(args) > 1 else args[0])
    n = next(it)
    for i in it:
        a, b = (key(i), key(n)) if key is not None else (i, n)
        n = i if a > b else n
    return n


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
