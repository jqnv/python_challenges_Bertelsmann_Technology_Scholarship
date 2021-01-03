# Write a program that reads integers from the user and stores them in a
# list. Your program should continue reading values until the user enters 0.
# Then it should display all of the values entered by the user
# (except for the 0) in order from smallest to largest, with one value
# appearing on each line. Use either the sort method or the sorted function
# to sort the list.

def sorted_order(num):
    num.sort()
    for i in num:
        print(i)


if __name__ == '__main__':
    num = []
    while True:
        num.append(int(input("Please enter an integer number into the list: ")))
        if num[-1] == 0:
            num.pop()
            break
    sorted_order(num)
