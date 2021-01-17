# Write a function that creates a random Bingo card and stores it in a dictionary. The keys will be the letters
# B, I, N, G and O. The values will be the lists of five numbers that appear under each letter. Write a second
# function that displays the Bingo card with the columns labeled appropriately.
from random import randint


def random_bingo():
    bingo_card = {"B": [15, []], "I": [30, []], "N": [45, []], "G": [60, []], "O": [75, []]}
    temp_value = 0
    for k, v in bingo_card.items():
        while len(v[1]) < 6:
            temp_value = randint(v[0] - 14, v[0])
            if temp_value not in v[1]:
                v[1].append(temp_value)

    print_card(bingo_card)


def print_card(dict_card):
    for k, v in dict_card.items():
        print(f"{k}\t", end="")
    print()
    for i in range(5):
        for k, v in dict_card.items():
            print(f"{v[1][i]}\t", end="")
        print()


if __name__ == '__main__':
    random_bingo()
