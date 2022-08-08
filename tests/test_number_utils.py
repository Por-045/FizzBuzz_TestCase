from coe_number.number_utils import is_fizz_buzz

import unittest

mylist = [0, 1, 2]

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_should_fizz(self):
        number = 3
        excepted_result = 'Fizz'

        result = is_fizz_buzz(number) 

        self.assertEqual(result, excepted_result)
