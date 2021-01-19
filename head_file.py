# Unix-based operating systems usually include a tool named head. It displays the first 10 lines of a file
# whose name is provided as a command line parameter. Write a Python program that provides the same behavior.
# Display an appropriate error message if the file requested by the user does not exist or if the command line
# parameter is omitted.
# You can use the attached "elements.txt" file if you need a file to work with.
from sys import argv


def head_file():
    try:
        file_1 = argv[1]
        with open(file_1, mode="r") as my_file:  # close the file automatically
            for i in range(10):
                line = next(my_file).strip()
                print(line)

    except FileNotFoundError as err:
        print("File does not exist")
    except IndexError as err:
        print("File name was not provided")


if __name__ == '__main__':
    head_file()
