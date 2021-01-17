# Write a function that creates a random Bingo card and stores it in a dictionary. The keys will be the letters
# B, I, N, G and O. The values will be the lists of five numbers that appear under each letter. Write a second
# function that displays the Bingo card with the columns labeled appropriately.
from random import randint


def random_bingo():
    # Initialize a dictionary with the letter of the column as the key
    # The value is the maximum of values for that letter and a blank list
    # for the numbers in the range for each letter
    bingo_card = {"B": [15, []], "I": [30, []], "N": [45, []], "G": [60, []], "O": [75, []]}
    for k, v in bingo_card.items():

        # Fill each list with 6 numbers per key making sure the number is not duplicated
        while len(v[1]) < 6:
            temp_value = randint(v[0] - 14, v[0])
            if temp_value not in v[1]:
                v[1].append(temp_value)
    # Calling function to print the Bingo Card
    print_card(bingo_card)


def print_card(dict_card):
    # Print the header of letters
    for k, v in dict_card.items():
        print(f"{k}\t", end="")
    print()

    # Print the  values under each letter
    for i in range(5):
        for k, v in dict_card.items():
            print(f"{v[1][i]}\t", end="")
        print()


if __name__ == '__main__':
    random_bingo()
