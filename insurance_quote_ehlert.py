"""
Program: insurance_quote_ehlert.py
Author: Tony Ehlert
Date Created: 08/25/2023

The purpose of this program is to get user input that used to calculate an insurance
rate quote
"""

def get_driver_name():
    """
    This method prompt's the user for their Name
    :return: string containing driver's name
    """
    # create set for name characters to use for validating username input
    name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-' '")

    # prompt user for name
    driver_name = input("Please Enter Your Name: ")
    if not (name_characters.issuperset(driver_name)):
        raise ValueError
    else:
        return driver_name

def get_driver_age():
    """
    This method prompt's the user for their Age
    :return: int containing driver's age
    """
    # prompt user for age and validate that input was an integer
    driver_age = int(input("Please Enter Your Age: "))
    if driver_age >= 16:
        return driver_age
    else:
        #print("Invalid age! Age must be 16 or greater!")
         raise ValueError

def get_driver_coverage():
    """
    This method prompt's the user for their desired coverage
    :return: string containing driver's desired coverage
    """
    # prompt user for coverage level and validate that input was correct
    driver_coverage =  input("Please Enter Your Desired Coverage Level (State Minimum[SM], Liability[L], or Full Coverage[F]: ")
    driver_coverage = driver_coverage.upper()
    if driver_coverage.upper() != "SM" and driver_coverage.upper() != "L" and driver_coverage.upper() != "F":
        raise ValueError
    else:
        return driver_coverage

def get_annual_cost(driver_info):
    """
    This method accepts a dictionary containing a driver's information and uses that to determine their base
    annual cost
    :param driver_info: dictionary containing a driver's info
    :return: dictionary of driver's info with annual cost added to it
    """
    if driver_info["AGE"] < 25:
        if driver_info["COVERAGE"] == "SM":
            driver_info["COST"] = 2593
        elif driver_info["COVERAGE"] == "L":
            driver_info["COST"] = 2957
        else:
            driver_info["COST"] = 6930

    elif 25 <= driver_info["AGE"] < 35:
        if driver_info["COVERAGE"] == "SM":
            driver_info["COST"] = 608
        elif driver_info["COVERAGE"] == "L":
            driver_info["COST"] = 691
        else:
            driver_info["COST"] = 1745

    elif 35 <= driver_info["AGE"] < 45:
        if driver_info["COVERAGE"] == "SM":
            driver_info["COST"] = 552
        elif driver_info["COVERAGE"] == "L":
            driver_info["COST"] = 627
        else:
            driver_info["COST"] = 1564

    elif 45 <= driver_info["AGE"] < 55:
        if driver_info["COVERAGE"] == "SM":
            driver_info["COST"] = 525
        elif driver_info["COVERAGE"] == "L":
            driver_info["COST"] = 596
        else:
            driver_info["COST"] = 1469

    elif 55 <= driver_info["AGE"] < 65:
        if driver_info["COVERAGE"] == "SM":
            driver_info["COST"] = 494
        elif driver_info["COVERAGE"] == "L":
            driver_info["COST"] = 560
        else:
            driver_info["COST"] = 1363

    else:
        if driver_info["COVERAGE"] == "SM":
            driver_info["COST"] = 515
        elif driver_info["COVERAGE"] == "L":
            driver_info["COST"] = 585
        else:
            driver_info["COST"] = 1402

    return driver_info

if __name__ == "__main__":
    #create cost modifier values
    ACCIDENT_INC_RATE = 1.41
    UPFRONT_DISC_RATE = .9

    #create dictionary to store driver's info
    driver_info = {"NAME": "", "AGE": 0, "COVERAGE": "", "COST": 0.0}

    # call function to get name from user
    while True:
        try:
            driver_name = get_driver_name()
            driver_info["NAME"] = driver_name
            break
        except ValueError:
            print("Invalid Input!")

    # call function to get age from user
    while True:
        try:
            driver_age = get_driver_age()
            driver_info["AGE"] = driver_age
            break
        except ValueError:
            print("Invalid Input!")

    # call function to get desired coverage from user
    while True:
        try:
            driver_coverage = get_driver_coverage()
            driver_info["COVERAGE"] = driver_coverage
            break
        except ValueError:
            print("Invalid Input!")

    # call function to determine base annual cost
    get_annual_cost(driver_info)

    # ask user if they have had any accidents. If true increase base rate by 41% and update dictionary
    while True:
        had_accidents = input("Have you had any accidents?")
        had_accidents = had_accidents.upper()
        if had_accidents == "Y" or had_accidents == "YES":
            driver_info["COST"] = driver_info["COST"] * ACCIDENT_INC_RATE
            break
        elif had_accidents == "N" or had_accidents == "NO":
            break
        else:
            print("Invalid response!")

    # ask user if they would like to pay up front for a 10% discount and update dictionary if true (COST * .9)
    while True:
        paying_upfront = input("Would you like to pay the total upfront to save 10%?")
        paying_upfront = paying_upfront.upper()
        if paying_upfront == "Y" or paying_upfront == "YES":
            driver_info["COST"] = driver_info["COST"] * UPFRONT_DISC_RATE
            break
        elif paying_upfront == "N" or paying_upfront == "NO":
            break
        else:
            print("Invalid Response!")

    # output annual insurance cost to user
    print(f"Your insurance rate will be ${driver_info['COST']:.2f}")