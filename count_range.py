# Python’s standard library includes a method named count that determines how many times a specific value occurs
# in a list. In this exercise, you will create a new function named countRange which determines and returns
# the number of elements within a list that are greater than or equal to some minimum value and less than some
# maximum value
from random import randint, random


# Function to determine how many elements are greater or equal to the minimum provided
# and less than maximum provided
def countRange(min_val, max_val, num_list):
    count = len([i for i in num_list if min_val <= i < max_val])
    return count


# Function to generate 6 lists of integers and float numbers with their minimum and maximum values to test it
def main():
    for i in range(6):
        items = []
        print(f"Test {i + 1}")

        # Generate minimum and maximum value
        min_max = sorted(list([randint(1, 100), randint(1, 100)]))
        min_val, max_val = min_max[0], min_max[1]

        # Print minimum and maximum value
        print(f"Minimum value: {min_val} Maximum value: {max_val}")

        # Half of the cases will be list of integers and half list of float numbers
        if i % 2 == 0:
            items = [randint(1, 100) for i in range(5)]
        else:
            items = [random() * 100 for i in range(5)]

        # Print the list of the case
        print(f"List: {items}")

        # Print the results after test the case
        print(
            f"We have {countRange(min_val, max_val, items)} elements in the list greater or equal than {min_val} and less than {max_val}\n")


if __name__ == '__main__':
    main()
