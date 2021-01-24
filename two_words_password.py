# While generating a password by selecting random characters usually creates one that is relatively secure, it also
# generally gives a password that is difficult to memorize. As an alternative, some systems construct a password
# by taking two English words and concatenating them. While this password may not be as secure, it is normally
# much easier to memorize.
# Write a program that reads a file containing a list of words, randomly selects two of them, and concatenates them
# to produce a new password. When producing the password ensure that the total length is between 8 and 10 characters,
# and that each word used is at least three letters long. Capitalize each word in the password so that the user can
# easily see where one word ends and the next one begins. Finally, your program should display the password for the user.


# To run de program you can use the words.txt file
# Example: [prompt]>python two_words_password.py words.txt

from sys import argv
from random import randint


def two_word_password():
    try:
        # Read the file containing the list of words saving them in a list
        with open(argv[1]) as infile:
            infile = list(infile)

        # Repeat the process
        while True:

            # Choose two words randomly
            word1 = infile[randint(0, len(infile) - 1)].rstrip()
            word2 = infile[randint(0, len(infile) - 1)].rstrip()

            # Check if both words are at least three long and total lenght of password is between 8 and 10 characters
            if len(word1) >= 3 and len(word2) >= 3 and 8 <= len(word1) + len(word2) <= 10 and word1 != word2:
                password = word1.capitalize() + word2.capitalize()
                return password
            else:
                continue

    # Print a message if file open fails
    except IOError:
        print(f"Failed to open file {argv[1]}")


if __name__ == '__main__':
    # Print password
    print(two_word_password())
