from coe_number.number_utils import is_fizz_buzz

import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_5_should_buzz(self):
        #arrange
        number = 5
        excepted_result = 'Buzz' 
        #act
        result = is_fizz_buzz(number) 
        #assert
        self.assertEqual(result, excepted_result)
