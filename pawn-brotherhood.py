def safe_pawns(pawns):
    safe_spots = set()
    result = 0
    for pawn in sorted(pawns, key=lambda k: k[1]):
        if pawn in safe_spots:
            result += 1
        x, y = pawn
        if int(y) < 8:
            y = str(int(y)+1)
            if x > 'a':
                safe_spots.add(chr(ord(x)-1)+y)
            if x < 'h':
                safe_spots.add(chr(ord(x)+1)+y)
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
