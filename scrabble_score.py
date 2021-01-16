# Write a program that computes and displays the Scrabble™ score for a word. Create a dictionary that maps from
# letters to point values. Then use the dictionary to compute the score


def scrabble_score(word):
    # Declare of variable to store the score
    score = 0

    # Pairing values and letters in a dictionary
    points_letter = {
        1: ["A", "E", "I", "L", "N", "O", "R", "S", "T","U"], 2: ["D", "G"], 3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"], 5: ["K"], 8: ["J", "X"], 10: ["Q", "Z"]
    }

    # Accumulating the score in the variable according to value of each letter
    for letter in word.upper():
        for k, v in points_letter.items():
            if letter in v:
                score += k

    # Displaying the results
    print(f"The Scrabble™ score for '{word}' is {score}")


if __name__ == '__main__':
    word = input("Please enter a word to get the Scrabble™ score: ")
    scrabble_score(word)
