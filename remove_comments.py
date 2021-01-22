# Python uses the # character to mark the beginning of a comment. The comment ends at the end of the line containing
# the # character. In this exercise, you will create a program that removes all of the comments from a Python source file.
# Check each line in the file to determine if a # character is present. If it is then your program should remove all of
# the characters from the # character to the end of the line (we’ll ignore the situation where the comment character
# occurs inside of a string). Save the modified file using a new name that will be entered by the user. The user will
# also enter the name of the input file. Ensure that an appropriate error message is displayed if a problem is
# encountered while accessing the files.

# To run de program: >python [name py file] [name of text file] [name of output file]
# Example: [prompt]>python remove_comments.py with_comments.txt no_comments_file.txt
from sys import argv


def remove_comments():
    # Check if parameters provided
    if len(argv) < 3:
        print("Please provide the source name file and output file")
        return

        # Catch error message if error reading a file
    try:
        # Create output file
        with open(argv[2], 'w') as my_file:

            # Read file name provided
            with open(argv[1]) as infile:
                infile = list(infile)

            # Write file content in the new file
            for line in infile:

                # Remove comments
                line.strip()
                if line[0] == "#":
                    continue
                else:

                    # Write to output file
                    my_file.write(line)
            my_file.write("\n")

    except IOError:
        print(f"Failed to open file {argv[1]}")


if __name__ == '__main__':
    remove_comments()
