# In this exercise, you will create a program that reads words from the user until the user enters a blank line.
# After the user enters a blank line your program should display each word entered by the user exactly once.
# The words should be displayed in the same order that they were entered. For example, if the user enters:
# first
# second
# first
# third
# second
# then your program should display:
# first
# second
# third

def avoiding_duplicates():
    is_blank = True
    words = list()
    while is_blank:
        element = input("Please enter a word: ")
        if element == "":
            is_blank = False
        elif element not in words:
            words.append(element)
    for i in words:
        print(i)


if __name__ == '__main__':
    avoiding_duplicates()
