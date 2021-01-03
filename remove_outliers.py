# Challenge Day 19 : Remove Outliers: When analysing data collected
# as part of a science experiment it may be desirable to remove the most
# extreme values before performing other calculations. Write a function
# that takes a list of values and an non-negative integer, n, as its
# parameters.
# The function should create a new copy of the list with the n largest
# elements and the n smallest elements removed. Then it should return
# the new copy of the list as the function’s only result. The order of
# the elements in the returned list does not have to match the order of
# the elements in the original list.
# Write a main program that demonstrates your function. Your function
# should read a list of numbers from the user and remove the two largest
# and two smallest values from it. Display the list with the outliers
# removed, followed by the original list. Your program should generate an
# appropriate error message if the user enters less than 4 values.


def remove_outliers():
    num_list = list(input("Please enter a list of numbers with a comma between them to remove outliers : ").split(","))
    num_list = [int(i) for i in num_list]
    if len(num_list) < 4:
        print("The list should have at least 4 values")
        return
    else:
        cpy_list = num_list[:]
        cpy_list.sort()
        cpy_list = cpy_list[:len(cpy_list) - 2]
        cpy_list = cpy_list[2:]
    print(f"List with outliers removed: {cpy_list}, Original list: {num_list}")


if __name__ == '__main__':
    remove_outliers()
