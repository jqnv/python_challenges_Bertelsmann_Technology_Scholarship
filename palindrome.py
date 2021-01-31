# The notion of a palindrome was introduced previously in one of our previous coding challenges. In this exercise you
# will write a recursive function that determines whether or not a string is a palindrome. The empty string is a
# palindrome, as is any string containing only one character. Any longer string is a palindrome if its first and last
# characters match, and if the string formed by removing the first and last characters is also a palindrome.
# Write a main program that reads a string from the user and uses your recursive function to determine whether or not
# it is a palindrome. Then your program should display an appropriate message for the user.


def palindrome(word):
    # If word is length o or 1 print is palindrome
    if len(word) == 0 or len(word) == 1:
        print(f"The word is palindrome")

    # If first and last letter are equal remove them from, the list
    else:
        if word[0] == word[-1]:
            word.pop(0)
            word.pop()

            # Call recursive function
            palindrome(word)
        else:
            # If first and last letter are not equal show message is not palindrome
            print(f"The word is not palindrome")


if __name__ == '__main__':
    # Get input from the user an convert it into a list
    word = input("Please enter a word to check if it is a palindrome")
    word = list(word)
    palindrome(word)
