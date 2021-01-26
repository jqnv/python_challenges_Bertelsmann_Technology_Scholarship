from string import ascii_lowercase
from sys import argv


def lipogram():
    alpha_dict = dict.fromkeys(list(ascii_lowercase), 0)
    try:

        # Read the file
        with open(argv[1], "r") as infile:
            word_counter = 0

            # Iterate each line of the file in lines
            for line in infile:
                words = line.split()
                word_counter += len(words)

                # Iterate each word in the line
                for word in words:
                    characters = set(word.lower())

                    # Iterate for each letter in the dictionary key
                    for letter in alpha_dict:
                        if letter in characters:
                            # Increase the counter if found in a word
                            alpha_dict[letter] += 1
        # Find the lower value of the dictionary
        key_min = min(alpha_dict.keys(), key=(lambda k: alpha_dict[k]))

        # Print proportions of usage on words per letter
        print(f"Proportion of words using each letter of the alphabet:")
        for key in alpha_dict:
            print(f"{key}   {round(alpha_dict[key] / word_counter * 100, 3)}%")
        # Print the smaller portion of words used for a letter
        print(
            f"The letter used in the smaller portion of the words is '{key_min}' used only {round(alpha_dict[key_min] / word_counter * 100, 3)}% of the words in this file.")
    except IOError:
        print(f"Failed to open {argv[1]} file ")


if __name__ == '__main__':
    lipogram()
