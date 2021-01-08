# In order to win the top prize in a particular lottery, one must match all 6 numbers on his or her ticket
# to the 6 numbers between 1 and 49 that are drawn by the lottery organizer. Write a program that generates a random
# selection of 6 numbers for a lottery ticket. Ensure that the 6 numbers selected do not contain any duplicates.
# Display the numbers in ascending order.

from random import randint


def lottery_numbers():
    num_list = []

    # Generate list of numbers between 1 and 49
    while len(num_list) < 6:
        num = randint(1, 49)

        # Check if already exist to avoid duplicates
        if num not in num_list:
            num_list.append(num)

    # Order the list ascending
    num_list.sort()

    # Store list as list of string
    str_num = "-".join(list(map(str, num_list)))

    # Display the output
    print(f"The lottery numbers on your ticket are {str_num} Good luck!")


if __name__ == '__main__':
    lottery_numbers()
