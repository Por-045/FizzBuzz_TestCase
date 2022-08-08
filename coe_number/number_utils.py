def is_fizz_buzz(number):
    if (number >= 1 and number <= 1000):
        if (number % 3 == 0) & (number % 5 == 0):
            return 'Fizz Buzz'
        elif number % 3 == 0:
            return 'Fizz'
        elif number % 5 == 0:
            return 'Buzz'