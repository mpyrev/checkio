pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
}


def checkio(expression):
    stack = []
    for c in expression:
        if c in pairs.keys():
            stack.append(c)
        elif c in pairs.values():
            if len(stack) == 0 or pairs[stack.pop()] != c:
                return False
    return len(stack) == 0
