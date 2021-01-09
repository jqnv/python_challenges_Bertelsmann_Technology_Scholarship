# A standard deck of playing cards contains 52 cards. Each card has one of four suits along with a value. The suits are
# normally spades, hearts, diamonds and clubs while the values are 2 through 10, Jack, Queen, King and Ace.
# Each playing card can be represented using two characters. The first character is the value of the card, with the
# values 2 through 9 being represented directly. The characters “T”, “J”, “Q”, “K” and “A” are used to represent the
# values 10, Jack, Queen, King and Ace respectively. The second character is used to represent the suit of the card.
# It is normally a lowercase letter: “s” for spades, “h” for hearts, “d” for diamonds and “c” for clubs.
# The following table provides several examples of cards and their two-character representations...


def createDeck():
    # Create lists with first and second characters of cards
    first_char_list = list(str(x) for x in range(2, 10)) + ["T", "J", "Q", "K", "A"]
    second_char = ["s", "h", "d", "c"]

    # Create an empty list
    list_cards = []

    # Create the list of ordered cards
    for i in range(len(second_char)):
        for j in range(len(first_char_list)):
            list_cards.append(first_char_list[j] + second_char[i])

    # Print ordered cards
    print(list_cards)

    # Calling function to shuffle cards
    shuffle(list_cards)


def shuffle(list_cards):
    # Converting the list into a set in order to shuffle the list
    print(set(list_cards))


if __name__ == '__main__':
    createDeck()
