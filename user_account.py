"""
Program Name: user_account.py
Author: Tony Ehlert
Date: 8/29/2023

Program Description: This program defines a class representing user bank accounts and contains driver code to test
creating objects from the class as well as the methods defined in the class
"""


class user_account:
    def __init__(self, account_owner, account_num, account_type):
        # supersets for validation
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-' '")

        # if statement against supersets for validation
        if not (name_characters.issuperset(account_owner)):
            raise ValueError

        # if statement to check for proper account type
        if account_type.upper() != "CHECKING" and account_type.upper() != "SAVINGS":
            raise ValueError

        # convert account_num to string to verify account_num passed is not a float
        account_num = str(account_num)

        # convert account_num back to int and verify it is greater than zero
        account_num = int(account_num)
        if account_num > 0:
            self._account_num = int(account_num)
        else:
            raise ValueError

        self._account_owner = account_owner
        self._account_num = int(account_num)
        self._account_type = account_type.capitalize()
        self._account_balance = 0.0

    @property
    def account_owner(self):
        return self._account_owner

    @account_owner.setter
    def set_account_owner(self, account_owner):
        # supersets for validation
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-' '")

        # if statement against supersets for validation
        if not (name_characters.issuperset(account_owner)):
            raise ValueError
        else:
            self._account_owner = account_owner

    @property
    def account_num(self):
        return self._account_num

    @account_num.setter
    def set_account_num(self, account_num):
        # convert account_num to string to verify account_num passed is not a float
        account_num = str(account_num)

        # convert account_num back to int and verify it is greater than zero
        account_num = int(account_num)
        if account_num > 0:
            self._account_num = int(account_num)
        else:
            raise ValueError

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def set_account_type(self, account_type):
        # if statement to check for proper account type
        if account_type.upper() != "CHECKING" and account_type.upper() != "SAVINGS":
            raise ValueError
        else:
            self._account_type = account_type.capitalize()

    @property
    def account_balance(self):
        return self._account_balance

    @account_balance.setter
    def set_account_balance(self, account_balance):
        self._account_balance = account_balance

    def deposit(self, deposit_amount):
        """
        This method accepts an amount and adds it to the account_balance

        ":param deposit_amount: amount to be added to account_balance
        :return: None
        """
        # if statement to check for number greater than zero
        if (deposit_amount > 0.00):
            self._account_balance += deposit_amount
        else:
            raise ValueError

    def withdrawal(self, withdrawl_amount):
        """
        This method accepts an amount and attempts to subtract it from the account_balance. If subtracting the
        amount would cause the account_balance to go negative, nothing is subtracted and a statement is printed
        to the console indicating that the transaction could not be completed.

        :param withdrawl_amount: amount to be withdrawn from account_balance
        :return: None
        """
        if (withdrawl_amount > 0):
            if self._account_balance < withdrawl_amount:
                print("Unable to complete transaction. Account balance is less than requested withdrawal amount")
            else:
                self._account_balance = self._account_balance - withdrawl_amount
        else:
            raise ValueError

    def display(self):
        """
        This method returns a formatted string containing the user_account's account_owner, account_num, account_type
        and account_balance

        :return: Formatted string containing user_account object information
        """
        display_string = "Account Owner: " + self._account_owner
        display_string += ("\n" + "Account Number: " + str(self._account_num))
        display_string += ("\n" + "Account Type: " + self._account_type)
        display_string += (f"\nAccount Balance: ${self._account_balance:.2f}")
        return display_string

    def __str__(self):
        str_string = "Account Owner: " + self._account_owner
        str_string += (", Account Number: " + str(self._account_num))
        str_string += (", Account Type: " + self._account_type)
        str_string += (", Account Balance: " + str(self._account_balance))
        return str_string

    def __repr__(self):
        repr_string = "User_Account(\"" + self._account_owner
        repr_string += ("\", " + str(self._account_num + ", "))
        repr_string += ("\"" + self._account_type + "\")")
        return repr_string


# DRIVER CODE
if __name__ == "__main__":
    # print statement to indicate account1 tests
    print("TESTS FOR account1 OBJECT")

    try:
        # create account1 object
        account1 = user_account("Tony Stark", 123456, "checking")
    except ValueError:
        print("Cannot create object. Argument(s) provided are invalid")

    # add a balance of $400 to account1
    account1.deposit(400)

    # withdraw $250 from account 1
    account1.withdrawal(250)

    # display information about account1
    try:
        print(account1.display())
    except NameError:
        print("No Object to Display")

    # print statement to indicate account1 tests
    print("\nTESTS FOR account2 OBJECT")

    # create account2 object
    try:
        # create account1 object
        account2 = user_account("Clint Barton", 987654, "SaViNgs")
    except ValueError:
        print("Cannot create object. Argument(s) provided are invalid")

    # add a balance of $50 to account2
    account2.deposit(50)

    # withdraw $100 from account2
    account2.withdrawal(100)

    # display information about account2
    try:
        print(account2.display())
    except NameError:
        print("No Object to Display")
