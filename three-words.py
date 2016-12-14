def checkio(words):
    bools = [w.isalpha() for w in words.split()]
    compressed_str = ''.join(str(int(b)) for b in bools)
    return any(len(s) >= 3 for s in compressed_str.split('0'))
