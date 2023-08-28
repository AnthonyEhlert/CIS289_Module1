"""
Program Name: gathering_input_functions_ehlert.py
Author: Tony Ehlert
Date: 8/28/2023

Program Description: This program contains two functions.  The first functions prompts the user for how many integers
they would like to store.  The second functions prompts the user for the integers they want to store.  Finally,
the program then prints the list of integers, followed by the average of the integers in the list.
"""
def get_num_of_ints():
    """
    This funtion prompts the user for the number of integers they would like to store and returns
    that number
    :return: integer value representing the total number of integers the user would like to store
    """
    #prompt user for total number of integers they want to store and validate input.
    num_of_ints = int(input("Please enter the number of integers you would like to store: "))
    # check to ensure number entered is greater than zero
    if num_of_ints >= 1:
        return num_of_ints
    else:
        raise ValueError

def get_ints(list_of_ints, num_of_ints):
    """
    This function accepts to number of integers that the user would like to store, and then prompts the user
    to enter the integers they want to store
    :param list_of_ints: list of ints to be updated
    :param num_of_ints: total number of integer numbers to be stored in the list(aka len of list)
    :return: updated list of integers
    """
    # prompt user for the integers to store and validate input
    while len(list_of_ints) < (num_of_ints):
        if len(list_of_ints) < (num_of_ints - 1):
            int_to_add = int(input("Please enter the next integer you would like to store: "))
            list_of_ints.append(int_to_add)
        else:
            int_to_add = int(input("Please enter the last integer you would like to store: "))
            list_of_ints.append(int_to_add)
            return list_of_ints


if __name__ == "__main__":
    # call function to get total num of integers to be stored.  Loop until valid input is received
    while True:
        try:
            total_num_of_ints = get_num_of_ints()
            break
        except ValueError:
            print("Invalid Entry! Number entered must be a whole number greater than 0.")

    # create empty list to pass to function
    list_of_ints = []

    # call function to get integers to be stored in list.  Loop until valid inputs are received
    while True:
        try:
            list_of_ints = get_ints(list_of_ints, total_num_of_ints)
            break
        except ValueError:
            print("Invalid Entry! Number entered must be a whole number.")

    # print the list of integers contained in list
    print("Integers in list: " + str(list_of_ints))

    #calculate sum of integers stored in list
    sum_of_ints = 0
    for int in list_of_ints:
        sum_of_ints += int
    print(sum_of_ints)

    # print the average of the integers contained in list
    print("Average of stored integers: " + str(sum_of_ints/total_num_of_ints))