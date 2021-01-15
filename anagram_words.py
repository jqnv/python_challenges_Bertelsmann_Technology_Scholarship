# Two words are anagrams if they contain all of the same letters, but in a different order. For example, “evil”
# and “live” are anagrams because each contains one e, one i, one l, and one v. Create a program that reads two
# strings from the user, determines whether or not they are anagrams, and reports the result.


def is_anagram(str1, str2):
    # Strings stored in lists to be sorted
    word1 = sorted(list(str1))
    word2 = sorted(list(str2))

    # Sorted lists compared if are equal and print results of comparison
    if word1 == word2:
        print(f"{str1} and {str2} are anagrams as both contain all of the same letters")
    else:
        print(f"{str1} and {str2} are not anagrams")


if __name__ == '__main__':
    str1 = input("please enter first word: ")
    str2 = input("please enter second word: ")
    is_anagram(str1, str2)
