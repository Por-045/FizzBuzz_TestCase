from unittest import result
from numpy import number
from coe_number.number_utils import is_fizz_buzz

import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_should_fizz(self):
        #arrange
        number = 3
        excepted_result = 'Fizz' 
        #act
        result = is_fizz_buzz(number) 
        #assert
        self.assertEqual(result, excepted_result)

    def test_give_5_should_buzz(self):
        #arrange
        number = 5
        excepted_result = 'Buzz' 
        #act
        result = is_fizz_buzz(number) 
        #assert
        self.assertEqual(result, excepted_result)
    
    def test_give_15_should_fizz_buzz(self):
        #arrange
        number = 15
        excepted_result = 'Fizz Buzz' 
        #act
        result = is_fizz_buzz(number) 
        #assert
        self.assertEqual(result, excepted_result)
    
    def test_give_0_should_less_than_one(self):
        number = 0
        excepted_result = 'less than one'

        result = is_fizz_buzz(number)

        self.assertEqual(result, excepted_result)

    def test_give_1001_should_more_than_thousand(self):
        number = 1001
        excepted_result = 'more than thousand'

        result = is_fizz_buzz(number)

        self.assertEqual(result, excepted_result)
