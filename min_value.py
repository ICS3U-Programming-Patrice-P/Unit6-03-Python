#!/usr/bin/env python3

# Created By: Patrice Pat-Odita
# Created on: Dec 23, 2022
# This program Generates 10 random numbers, loops it to find the one with
# the lowest value and displays it.

import random

# Generates 10 random numbers
def find_min_value(array_of_nums):
    # This is the variable that will hold the highest value
    min_num = array_of_nums[0]

    for counter in range(len(array_of_nums)):
        current_num = array_of_nums[counter]
        # sets max_num to the current number generated comparing it
        # to see if it is greater than the number.
        if min_num > current_num:
            min_num = current_num
    # Returns the maximum number
    return min_num


def main():

    # declaring variable
    counter = 0
    min_num_arr = []

    # display opening message to console
    print("")
    print(
        "\033[1;35;38mThis program generates a list of random "
        "numbers between 0 and 100, then determines the smallest number."
    )
    print("")

    # generates random numbers
    for counter in range(10):

        # putting the random number into the array
        min_num_arr.append(random.randint(0, 100))

        print(
            " {} is added to the list at "
            "position {}".format(min_num_arr[counter], counter)
        )

    # calls the function
    min_value = find_min_value(min_num_arr)

    # displays results
    print("\nThe min value is {}".format(min_value))


if __name__ == "__main__":
    main()
