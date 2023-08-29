import unittest

from CIS289_Module1.user_account import user_account

"""
Program Name: user_account_tests.py
Author: Tony Ehlert
Date: 8/29/2023

Program Description: This program contains unit tests to test the user_account class defined in the user_account.py file
"""


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_account = user_account("Owner Name", 123456, "checking")

    def tearDown(self) -> None:
        del self.test_account

    def test_create_user_account_checking(self):
        self.assertEqual(self.test_account._account_owner, "Owner Name")
        self.assertEqual(self.test_account._account_num, 123456)
        self.assertEqual(self.test_account._account_type, "Checking")
        self.assertEqual(self.test_account._account_balance, 0.0)

    def test_create_user_account_savings(self):
        self.test_account = user_account("Owner Name", 123456, "SAVINGS")
        self.assertEqual(self.test_account._account_owner, "Owner Name")
        self.assertEqual(self.test_account._account_num, 123456)
        self.assertEqual(self.test_account._account_type, "Savings")
        self.assertEqual(self.test_account._account_balance, 0.0)

    def test_create_user_account_bad_owner(self):
        with self.assertRaises(ValueError):
            user_account("Test 123", 123456, "Checking")
        with self.assertRaises(ValueError):
            self.test_account.set_account_owner = "Test 123"

    def test_create_user_account_bad_account_num(self):
        with self.assertRaises(ValueError):
            self.test_account.set_account_num = "One"
        with self.assertRaises(ValueError):
            self.test_account.set_account_num = 1.1
        with self.assertRaises(ValueError):
            self.test_account.set_account_num = -1
        with self.assertRaises(ValueError):
            user_account("Owner Name", 1.1, "Checking")
        with self.assertRaises(ValueError):
            user_account("Owner Name", -1, "Checking")

    def test_create_user_account_bad_type(self):
        with self.assertRaises(ValueError):
            user_account("Owner Name", 123456, "cheking")
        with self.assertRaises(ValueError):
            user_account("Owner Name", 123456, "savins")
        with self.assertRaises(ValueError):
            self.test_account.set_account_type = "savins"
        with self.assertRaises(ValueError):
            self.test_account.set_account_type = "Checkin"

    def test_deposit(self):
        self.test_account.deposit(50)
        self.assertEqual(self.test_account.account_balance, 50)

    def test_deposit_neg_amount(self):
        with self.assertRaises(ValueError):
            self.test_account.deposit(-50)

    def test_withdrawal(self):
        self.test_account.deposit(100)
        self.test_account.withdrawal(50)
        self.assertEqual(self.test_account.account_balance, 50)

    def test_withdrawal_neg_amount(self):
        with self.assertRaises(ValueError):
            self.test_account.withdrawal(-50)

    def test_withdrawal_balance_too_small(self):
        self.test_account.deposit(50.01)
        self.test_account.withdrawal(50.02)
        self.assertEqual(self.test_account.account_balance, 50.01)

    def test_display(self):
        self.assertEqual(self.test_account.display(), "Account Owner: Owner Name\nAccount Number: 123456\nAccount "
                                                      "Type: Checking\nAccount Balance: $0.00")


if __name__ == '__main__':
    unittest.main()
