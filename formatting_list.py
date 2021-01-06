# When writing out a list of items in English, one normally separates the items with commas. In addition,
# the word “and” is normally included before the last item, unless the list only contains one item. Consider
# the following four lists:
# apples
# apples and oranges
# apples, oranges and bananas
# apples, oranges, bananas and lemons
# Write a function that takes a list of strings as its only parameter. Your function should return a string
# that contains all of the items in the list formatted in the manner described previously as its only result.
# While the examples shown previously only include lists containing four elements or less, your function should
# behave correctly for lists of any length. Include a main program that reads several items from the user, formats
# them by calling your function, and then displays the result returned by the function.


def formatting_list(my_list):
    length_list = len(my_list)
    if length_list == 1:
        formatted = my_list[0]
    if length_list > 1:
        my_list.insert(-1, " and ")
        formatted = (", ".join(my_list[:-2])) + my_list[-2] + my_list[-1]
    print(formatted)


def main():
    bol = True
    my_list = []
    while bol:
        element = input("Please enter an item or press enter to finish: ")
        if element != "":
            my_list.append(element)
        else:
            bol = False
    formatting_list(my_list)


if __name__ == '__main__':
    main()
