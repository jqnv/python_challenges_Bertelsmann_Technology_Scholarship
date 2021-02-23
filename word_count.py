# The challenge for this exercise is to write a wordcount function that mimics the wc Unix command.
# The function will take a filename as input and will print four lines of output:
# 1 Number of characters (including whitespace)
# 2 Number of words (separated by whitespace)
# 3 Number of lines
# 4 Number of unique words (case sensitive, so “NO” is different from “no”)

# To run the file at the command line Prompt> python word_count.py wcfile.txt

from sys import argv


def word_count():
    # Assigning parameter on command line to variable
    file_1 = argv[1]

    # Open file on read mode with alias my_file
    with open(file_1, mode="r") as my_file:
        # Initialize variables to get the total of elements required
        num_char = 0
        num_words = 0
        num_lines = 0
        uniq_words = set()

        # Loop to get variables updated for each line
        for line in my_file:
            num_lines += 1
            words = line.split()
            num_char += len(line)
            num_words += len(words)
            uniq_words.update(words)

        # Print results
        print(f"Number of characters: {num_char}")
        print(f"Number of words: {num_words}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of unique words: {len(uniq_words)}")


if __name__ == '__main__':
    word_count()
