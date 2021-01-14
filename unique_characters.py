# Create a program that determines and displays the number of unique characters in a string entered by the user.
# For example, Hello, World! has 10 unique characters while zzz has only one unique character. Use a dictionary or
# set to solve this problem


def unique_characters(text):
    # Solution using dictionary
    dictionary_solution(text)

    # Solution using set
    set_solution(text)


def dictionary_solution(text):
    # Declare an empty dictionary
    my_dict = {}

    # Fill the dictionary with unique characters
    for i in text:
        my_dict.update({i: 0})

    # Print unique characters in an ascendant order list
    print(f"Solution using a dictionary: {sorted(list(my_dict.keys()))} {len(my_dict)} unique characters")


def set_solution(text):
    # Convert test to set to get unique characters
    solution1 = set(text)

    # Print unique characters in an ascendant order list
    print(f"Solution using a set: \t\t {sorted(list(solution1))} {len(solution1)} unique characters")


if __name__ == '__main__':
    unique_characters(input("Please enter the sentence to get unique characters: "))
