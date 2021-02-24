# In this exercise, write two functions. find_longest_word takes a filename as an argument and returns
# the longest word found in the file.
# The second function, find- _all_longest_words, takes a directory name and returns a dict in which the keys are
# filenames and the values are the longest words from each file.

# To run the file at the command line Prompt> python find_all_longest_words.py books
from sys import argv
from os import scandir


def find_all_longest_words():

    # Get the list of files in books folder
    files = scandir(argv[1])
    longest_words = dict()

    # Iterate over every file
    for file in files:
        long_word = ""
        path = argv[1] + "/" + file.name

        # Read every file
        with open(path, 'r', encoding="utf8") as f:

            # Iterate for each line in the current file
            for line in f:
                line = f.readline().split()

                # Iterate for each word in the line
                for word in line:

                    # Find the longest word
                    if len(word) > len(long_word):
                        long_word = word

        # Update dictionary with the file name and the longest word
        longest_words.update({file.name: long_word})

    # Return the dictionary
    return longest_words


if __name__ == '__main__':
    print(find_all_longest_words())
