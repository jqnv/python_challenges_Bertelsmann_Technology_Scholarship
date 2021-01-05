# Create a program that reads integers from the user until a blank line is entered. Once all of the integers
# have been read your program should display all of the negative numbers, followed by all of the zeros,
# followed by all of the positive numbers. Within each group the numbers should be displayed
# in the same order that they were entered by the user. For example, if the user enters
# the values 3, -4, 1, 0, -1, 0, and -2 then your program should output the values -4, -1, -2, 0, 0, 3, and 1.
# Your program should display each value on its own line.


def neg_zero_positives():
    is_blank = True
    neg, zero, pos = list(), list(), list()
    while is_blank:
        element = input("Please enter a number: ")
        if element == "":
            break
        num_element = int(element)
        if num_element < 0: neg.append(num_element)
        if num_element == 0: zero.append(num_element)
        if num_element > 0: pos.append(num_element)
    numbers = neg + zero + pos
    for i in numbers:
        print(i)


if __name__ == '__main__':
    neg_zero_positives()
