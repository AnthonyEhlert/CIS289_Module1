import unittest
from unittest import mock

from CIS289_Module1.gathering_input_functions_ehlert import get_num_of_ints, get_ints

"""
Program Name: gathering_input_functions_tests.py
Author: Tony Ehlert
Date: 8/28/2023

Program Description: This program runs unit tests to test the functions contained in the 
gathering_input_functions_ehlert.py file
"""

class MyTestCase(unittest.TestCase):
    def test_get_num_of_ints_good_input(self):
        with mock.patch('builtins.input', return_value= "1"):
            assert get_num_of_ints() == 1

    def test_get_num_of_ints_0_input(self):
        with mock.patch('builtins.input', return_value = "0"):
            with self.assertRaises(ValueError):
                get_num_of_ints()

    def test_get_num_of_ints_neg_input(self):
        with mock.patch('builtins.input', return_value = "-1"):
            with self.assertRaises(ValueError):
                get_num_of_ints()

    def test_get_num_of_ints_string_input(self):
        with mock.patch('builtins.input', return_value = "One"):
            with self.assertRaises(ValueError):
                get_num_of_ints()

    def test_get_num_of_ints_float_input(self):
        with mock.patch('builtins.input', return_value = "1.1"):
            with self.assertRaises(ValueError):
                get_num_of_ints()

    def test_get_ints_good_input(self):
        list_of_ints = []
        num_of_ints = 3

        with mock.patch('builtins.input', side_effect = ["1", "2", "3"]):
            assert get_ints(list_of_ints, num_of_ints) == [1, 2, 3]

    def test_get_ints_string_input(self):
        list_of_ints = []
        num_of_ints = 1

        with mock.patch('builtins.input', side_effect=["One"]):
            with self.assertRaises(ValueError):
                get_ints(list_of_ints, num_of_ints)

    def test_get_ints_float_input(self):
        list_of_ints = []
        num_of_ints = 1

        with mock.patch('builtins.input', side_effect=["1.0"]):
            with self.assertRaises(ValueError):
                get_ints(list_of_ints, num_of_ints)

if __name__ == '__main__':
    unittest.main()
