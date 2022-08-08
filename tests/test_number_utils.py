from coe_number.number_utils import is_fizz_buzz

import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_15_should_fizz_buzz(self):
        #arrange
        number = 15
        excepted_result = 'Fizz Buzz' 
        #act
        result = is_fizz_buzz(number) 
        #assert
        self.assertEqual(result, excepted_result)
