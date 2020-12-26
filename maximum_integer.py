# Option 2: This exercise examines the process of identifying the maximum value
# in a collection of integers. Each of the integers will be randomly selected
# from the numbers between 1 and 100. The collection of integers may contain
# duplicate values, and some of the integers between 1 and 100 may not be present...
from random import randint


def maximum_integer():
    max_value = randint(1, 100)
    print(f"{max_value}    <--- initial value")
    counter = 0
    for i in range(99):
        value = randint(1, 100)
        if value <= max_value:
            print(value)
        else:
            print(f"{value}    <--- update")
            max_value = value
            counter += 1
    print(f"The maximum value encountered is {max_value} after update {counter} times the max value")


maximum_integer()
