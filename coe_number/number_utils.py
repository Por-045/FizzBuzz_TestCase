def is_fizz_buzz(number):
    if (number >= 1 & number <= 1000):
        if number % 3 == 0 & number % 5 == 0:
            return 0
        elif number % 3 == 0:
            return 1
        elif number % 5 == 0:
            return 2