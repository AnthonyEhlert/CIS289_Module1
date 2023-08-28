import unittest
import unittest.mock as mock
"""
Program: insurance_quote_tests.py
Author: Tony Ehlert
Date Created: 08/26/2023

The purpose of this program is to get user input that used to calculate an insurance
rate quote
"""

from insurance_quote_ehlert import get_annual_cost, get_driver_name, get_driver_age, get_driver_coverage

class MyTestCase(unittest.TestCase):

    def test_get_driver_name_good_input(self):
        with mock.patch('builtins.input', return_value = "Test Name"):
            assert get_driver_name() == "Test Name"

    def test_get_driver_name_bad_input(self):
        with mock.patch('builtins.input', return_value = "1.1"):
            with self.assertRaises(ValueError):
                get_driver_name()

    def test_get_driver_age_good_input(self):
        with mock.patch('builtins.input', return_value = 16):
            assert get_driver_age() == 16

    def test_get_driver_age_under_16(self):
        with mock.patch('builtins.input', return_value = 15):
            with self.assertRaises(ValueError):
                get_driver_age()

    def test_get_driver_age_float_input(self):
        with mock.patch('builtins.input', return_value = 1.6):
            with self.assertRaises(ValueError):
                get_driver_age()

    def test_get_driver_age_string_input(self):
        with mock.patch('builtins.input', return_value = "age"):
            with self.assertRaises(ValueError):
                get_driver_age()

    def test_get_driver_coverage_lower_l_input(self):
        with mock.patch('builtins.input', return_value = "l"):
            assert get_driver_coverage() == 'L'

    def test_get_driver_coverage_lower_sm_input(self):
        with mock.patch('builtins.input', return_value = "sm"):
            assert get_driver_coverage() == 'SM'

    def test_get_driver_coverage_lower_f_input(self):
        with mock.patch('builtins.input', return_value = "f"):
            assert get_driver_coverage() == 'F'
    def test_get_driver_coverage_bad_input(self):
        with mock.patch('builtins.input', return_value = "Liability"):
            with self.assertRaises(ValueError):
                get_driver_coverage()

    def test_get_driver_coverage_int_input(self):
        with mock.patch('builtins.input', return_value = "16"):
            with self.assertRaises(ValueError):
                get_driver_coverage()

    def test_get_driver_coverage_float_input(self):
        with mock.patch('builtins.input', return_value = "1.6"):
            with self.assertRaises(ValueError):
                get_driver_coverage()

    def test_get_annual_cost_age_16(self):
        # ARRANGE
        driver_info_sm = {"NAME":"Test", "AGE":16, "COVERAGE":"SM", "COST":0.0}
        driver_info_l = {"NAME": "Test", "AGE": 16, "COVERAGE": "L", "COST": 0.0}
        driver_info_f = {"NAME": "Test", "AGE": 16, "COVERAGE": "F", "COST": 0.0}

        expected_sm = 2593
        expected_l = 2957
        expected_f = 6930

        #ACT
        driver_info_sm = get_annual_cost(driver_info_sm)
        actual_sm = driver_info_sm["COST"]
        driver_info_l = get_annual_cost(driver_info_l)
        actual_l = driver_info_l["COST"]
        driver_info_f = get_annual_cost(driver_info_f)
        actual_f = driver_info_f["COST"]

        #ASSERT
        self.assertEqual(actual_sm, expected_sm)
        self.assertEqual(actual_l, expected_l)
        self.assertEqual(actual_f, expected_f)

    def test_get_annual_cost_age_24(self):
        # ARRANGE
        driver_info_sm = {"NAME":"Test", "AGE":24, "COVERAGE":"SM", "COST":0.0}
        driver_info_l = {"NAME": "Test", "AGE": 24, "COVERAGE": "L", "COST": 0.0}
        driver_info_f = {"NAME": "Test", "AGE": 24, "COVERAGE": "F", "COST": 0.0}

        expected_sm = 2593
        expected_l = 2957
        expected_f = 6930

        #ACT
        driver_info_sm = get_annual_cost(driver_info_sm)
        actual_sm = driver_info_sm["COST"]
        driver_info_l = get_annual_cost(driver_info_l)
        actual_l = driver_info_l["COST"]
        driver_info_f = get_annual_cost(driver_info_f)
        actual_f = driver_info_f["COST"]

        #ASSERT
        self.assertEqual(actual_sm, expected_sm)
        self.assertEqual(actual_l, expected_l)
        self.assertEqual(actual_f, expected_f)

    def test_get_annual_cost_age_25(self):
        # ARRANGE
        driver_info_sm = {"NAME": "Test", "AGE": 25, "COVERAGE": "SM", "COST": 0.0}
        driver_info_l = {"NAME": "Test", "AGE": 25, "COVERAGE": "L", "COST": 0.0}
        driver_info_f = {"NAME": "Test", "AGE": 25, "COVERAGE": "F", "COST": 0.0}

        expected_sm = 608
        expected_l = 691
        expected_f = 1745

        # ACT
        driver_info_sm = get_annual_cost(driver_info_sm)
        actual_sm = driver_info_sm["COST"]
        driver_info_l = get_annual_cost(driver_info_l)
        actual_l = driver_info_l["COST"]
        driver_info_f = get_annual_cost(driver_info_f)
        actual_f = driver_info_f["COST"]

        # ASSERT
        self.assertEqual(actual_sm, expected_sm)
        self.assertEqual(actual_l, expected_l)
        self.assertEqual(actual_f, expected_f)

    def test_get_annual_cost_age_34(self):
        # ARRANGE
        driver_info_sm = {"NAME": "Test", "AGE": 34, "COVERAGE":"SM", "COST":0.0}
        driver_info_l = {"NAME": "Test", "AGE": 34, "COVERAGE": "L", "COST": 0.0}
        driver_info_f = {"NAME": "Test", "AGE": 34, "COVERAGE": "F", "COST": 0.0}

        expected_sm = 608
        expected_l = 691
        expected_f = 1745

        #ACT
        driver_info_sm = get_annual_cost(driver_info_sm)
        actual_sm = driver_info_sm["COST"]
        driver_info_l = get_annual_cost(driver_info_l)
        actual_l = driver_info_l["COST"]
        driver_info_f = get_annual_cost(driver_info_f)
        actual_f = driver_info_f["COST"]

        #ASSERT
        self.assertEqual(actual_sm, expected_sm)
        self.assertEqual(actual_l, expected_l)
        self.assertEqual(actual_f, expected_f)

    def test_get_annual_cost_age_35(self):
        # ARRANGE
        driver_info_sm = {"NAME": "Test", "AGE": 35, "COVERAGE":"SM", "COST":0.0}
        driver_info_l = {"NAME": "Test", "AGE": 35, "COVERAGE": "L", "COST": 0.0}
        driver_info_f = {"NAME": "Test", "AGE": 35, "COVERAGE": "F", "COST": 0.0}

        expected_sm = 552
        expected_l = 627
        expected_f = 1564

        #ACT
        driver_info_sm = get_annual_cost(driver_info_sm)
        actual_sm = driver_info_sm["COST"]
        driver_info_l = get_annual_cost(driver_info_l)
        actual_l = driver_info_l["COST"]
        driver_info_f = get_annual_cost(driver_info_f)
        actual_f = driver_info_f["COST"]

        #ASSERT
        self.assertEqual(actual_sm, expected_sm)
        self.assertEqual(actual_l, expected_l)
        self.assertEqual(actual_f, expected_f)

    def test_get_annual_cost_age_44(self):
        # ARRANGE
        driver_info_sm = {"NAME": "Test", "AGE": 44, "COVERAGE":"SM", "COST":0.0}
        driver_info_l = {"NAME": "Test", "AGE": 44, "COVERAGE": "L", "COST": 0.0}
        driver_info_f = {"NAME": "Test", "AGE": 44, "COVERAGE": "F", "COST": 0.0}

        expected_sm = 552
        expected_l = 627
        expected_f = 1564

        #ACT
        driver_info_sm = get_annual_cost(driver_info_sm)
        actual_sm = driver_info_sm["COST"]
        driver_info_l = get_annual_cost(driver_info_l)
        actual_l = driver_info_l["COST"]
        driver_info_f = get_annual_cost(driver_info_f)
        actual_f = driver_info_f["COST"]

        #ASSERT
        self.assertEqual(actual_sm, expected_sm)
        self.assertEqual(actual_l, expected_l)
        self.assertEqual(actual_f, expected_f)

    def test_get_annual_cost_age_45(self):
        # ARRANGE
        driver_info_sm = {"NAME": "Test", "AGE": 45, "COVERAGE":"SM", "COST":0.0}
        driver_info_l = {"NAME": "Test", "AGE": 45, "COVERAGE": "L", "COST": 0.0}
        driver_info_f = {"NAME": "Test", "AGE": 45, "COVERAGE": "F", "COST": 0.0}

        expected_sm = 525
        expected_l = 596
        expected_f = 1469

        #ACT
        driver_info_sm = get_annual_cost(driver_info_sm)
        actual_sm = driver_info_sm["COST"]
        driver_info_l = get_annual_cost(driver_info_l)
        actual_l = driver_info_l["COST"]
        driver_info_f = get_annual_cost(driver_info_f)
        actual_f = driver_info_f["COST"]

        #ASSERT
        self.assertEqual(actual_sm, expected_sm)
        self.assertEqual(actual_l, expected_l)
        self.assertEqual(actual_f, expected_f)

    def test_get_annual_cost_age_54(self):
        # ARRANGE
        driver_info_sm = {"NAME": "Test", "AGE": 54, "COVERAGE":"SM", "COST":0.0}
        driver_info_l = {"NAME": "Test", "AGE": 54, "COVERAGE": "L", "COST": 0.0}
        driver_info_f = {"NAME": "Test", "AGE": 54, "COVERAGE": "F", "COST": 0.0}

        expected_sm = 525
        expected_l = 596
        expected_f = 1469

        #ACT
        driver_info_sm = get_annual_cost(driver_info_sm)
        actual_sm = driver_info_sm["COST"]
        driver_info_l = get_annual_cost(driver_info_l)
        actual_l = driver_info_l["COST"]
        driver_info_f = get_annual_cost(driver_info_f)
        actual_f = driver_info_f["COST"]

        #ASSERT
        self.assertEqual(actual_sm, expected_sm)
        self.assertEqual(actual_l, expected_l)
        self.assertEqual(actual_f, expected_f)

    def test_get_annual_cost_age_55(self):
        # ARRANGE
        driver_info_sm = {"NAME": "Test", "AGE": 55, "COVERAGE":"SM", "COST":0.0}
        driver_info_l = {"NAME": "Test", "AGE": 55, "COVERAGE": "L", "COST": 0.0}
        driver_info_f = {"NAME": "Test", "AGE": 55, "COVERAGE": "F", "COST": 0.0}

        expected_sm = 494
        expected_l = 560
        expected_f = 1363

        #ACT
        driver_info_sm = get_annual_cost(driver_info_sm)
        actual_sm = driver_info_sm["COST"]
        driver_info_l = get_annual_cost(driver_info_l)
        actual_l = driver_info_l["COST"]
        driver_info_f = get_annual_cost(driver_info_f)
        actual_f = driver_info_f["COST"]

        #ASSERT
        self.assertEqual(actual_sm, expected_sm)
        self.assertEqual(actual_l, expected_l)
        self.assertEqual(actual_f, expected_f)

    def test_get_annual_cost_age_64(self):
        # ARRANGE
        driver_info_sm = {"NAME": "Test", "AGE": 64, "COVERAGE":"SM", "COST":0.0}
        driver_info_l = {"NAME": "Test", "AGE": 64, "COVERAGE": "L", "COST": 0.0}
        driver_info_f = {"NAME": "Test", "AGE": 64, "COVERAGE": "F", "COST": 0.0}

        expected_sm = 494
        expected_l = 560
        expected_f = 1363

        #ACT
        driver_info_sm = get_annual_cost(driver_info_sm)
        actual_sm = driver_info_sm["COST"]
        driver_info_l = get_annual_cost(driver_info_l)
        actual_l = driver_info_l["COST"]
        driver_info_f = get_annual_cost(driver_info_f)
        actual_f = driver_info_f["COST"]

        #ASSERT
        self.assertEqual(actual_sm, expected_sm)
        self.assertEqual(actual_l, expected_l)
        self.assertEqual(actual_f, expected_f)

    def test_get_annual_cost_age_65(self):
        # ARRANGE
        driver_info_sm = {"NAME": "Test", "AGE": 65, "COVERAGE":"SM", "COST":0.0}
        driver_info_l = {"NAME": "Test", "AGE": 65, "COVERAGE": "L", "COST": 0.0}
        driver_info_f = {"NAME": "Test", "AGE": 65, "COVERAGE": "F", "COST": 0.0}

        expected_sm = 515
        expected_l = 585
        expected_f = 1402

        #ACT
        driver_info_sm = get_annual_cost(driver_info_sm)
        actual_sm = driver_info_sm["COST"]
        driver_info_l = get_annual_cost(driver_info_l)
        actual_l = driver_info_l["COST"]
        driver_info_f = get_annual_cost(driver_info_f)
        actual_f = driver_info_f["COST"]

        #ASSERT
        self.assertEqual(actual_sm, expected_sm)
        self.assertEqual(actual_l, expected_l)
        self.assertEqual(actual_f, expected_f)

    def test_get_annual_cost_age_66(self):
        # ARRANGE
        driver_info_sm = {"NAME": "Test", "AGE": 66, "COVERAGE":"SM", "COST":0.0}
        driver_info_l = {"NAME": "Test", "AGE": 66, "COVERAGE": "L", "COST": 0.0}
        driver_info_f = {"NAME": "Test", "AGE": 66, "COVERAGE": "F", "COST": 0.0}

        expected_sm = 515
        expected_l = 585
        expected_f = 1402

        #ACT
        driver_info_sm = get_annual_cost(driver_info_sm)
        actual_sm = driver_info_sm["COST"]
        driver_info_l = get_annual_cost(driver_info_l)
        actual_l = driver_info_l["COST"]
        driver_info_f = get_annual_cost(driver_info_f)
        actual_f = driver_info_f["COST"]

        #ASSERT
        self.assertEqual(actual_sm, expected_sm)
        self.assertEqual(actual_l, expected_l)
        self.assertEqual(actual_f, expected_f)

if __name__ == '__main__':
    unittest.main()
