# Unix-based operating systems typically include a tool named cat, which is short for concatenate. Its purpose is to
# concatenate and display one or more files whose names are provided as command line parameters. The files are
# displayed in the same order that they appear on the command line.
# Create a Python program that performs this task. It should generate an appropriate error message for any file that
# cannot be displayed, and then proceed to the next file. Display an appropriate error message if your program is
# started without any command line parameters.

# To run the file at the command line Prompt> python cat_file.py text1.txt text2.txt
from sys import argv
from collections import deque


def cat_file():
    # Check if filenames provided
    if len(argv)<2:
        print("No file names provided")
        return

    # Create file to concatenate existing files
    with open('text3.txt', 'w') as my_file:

        # Iterate the file names provided
        for fname in argv[1:]:

            # Catch error message if error reading a file
            try:

                # Open file name provided
                with open(fname) as infile:
                    infile = list(infile)

                    # Write file content in the new file
                    for line in infile:
                        my_file.write(line)
                    my_file.write("\n")

            except IOError:
                print(f"Failed to open file {fname}")
                continue



if __name__ == '__main__':
    cat_file()
