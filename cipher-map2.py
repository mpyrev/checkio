def recall_password(cipher_grille, ciphered_password):
    power = len(cipher_grille)
    result = []
    for n in range(4):
        holes = [(i, j) for i in range(power) for j in range(power) if cipher_grille[i][j] == 'X']
        result.extend(ciphered_password[i][j] for i, j in holes)
        cipher_grille = list(zip(*reversed(cipher_grille)))
    return ''.join(result)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
