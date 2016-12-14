def checkio(number):
    result = str(number)
    if number % 3 == 0 and number % 5 == 0:
        result = 'Fizz Buzz'
    elif number % 3 == 0:
        result = 'Fizz'
    elif number % 5 == 0:
        result = 'Buzz'
    return result
