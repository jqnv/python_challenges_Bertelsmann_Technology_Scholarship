# Option 1 Difficulty Level: Elementary: Write a function that takes
# three numbers as parameters, and returns the median value of those
# parameters as its result. Include a main program that reads three values from
# the user and displays their median
from statistics import median


def median_calc(num_list):
    num_list.sort()
    print(f"The median value of {num1}, {num2} and {num3} is {num_list[len(num_list) // 2]}")


num1 = int(input("Plese enter the first number to get the median: "))
num2 = int(input("Plese enter the second number to get the median: "))
num3 = int(input("Plese enter the third number to get the median: "))
median_calc([num1, num2, num3])
