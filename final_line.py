# Unix-based operating systems also typically include a tool named tail. It displays the last 10 lines of a file
# whose name is provided as a command line parameter. Write a Python program that provides the same behavior.
# Display an appropriate error message if the file requested by the user does not exist or if the command line
# parameter is omitted...
# You can use the attached "elements.txt" file if you need a file to work with.

## To run the file at the command line Prompt> python tail_file.py elements.txt
from sys import argv
from collections import deque


def get_final_line():
    # Get the file name from the command line
    file_2 = argv[1]

    # Open the file using and alias
    with open(file_2) as my_file:
        # Print the content of last 10 lines using deque
        for line in deque(my_file, 1):
            print(line)

if __name__ == '__main__':
    get_final_line()