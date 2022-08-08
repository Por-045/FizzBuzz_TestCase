from coe_number.number_utils import is_fizz_buzz

import unittest

mylist = [0, 1, 2]

class FizzBuzzTest(unittest.TestCase):
    def test_give_3(self):
        num = 7
        is_result = is_fizz_buzz(num)
        print(is_result)
        self.assertIn(is_result, mylist)
