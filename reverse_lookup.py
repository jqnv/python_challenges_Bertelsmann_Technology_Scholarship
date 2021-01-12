# Write a function named reverseLookup that finds all of the keys in a dictionary
# that map to a specific value. The function will take the dictionary and the value
# to search for as its only parameters. It will return a (possibly empty) list of keys
# from the dictionary that map to the provided value.
# Include a main program that demonstrates the reverseLookup function as part of your
# solution to this exercise. Your program should create a dictionary and then show that
# the reverseLookup function works correctly when it returns multiple keys, a single key,
# and no keys. Ensure that your main program only runs when the file containing your
# solution to this exercise has not been imported into another program.


def reverseLookup(my_dict, value):
    # Create an empty list
    my_list = []

    # Get a list with all indexes for values equal to variable value
    for k, v in my_dict.items():
        if v == value:
            my_list.append(k)

    # Return the list
    return my_list


def main():
    # Create the sample dictionary
    my_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100,
               11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 4, 17: 4}

    # Values to test program
    val1 = 4  # Value found multiple times within the dictionary
    val2 = 9  # Value found once within the dictionary
    val3 = 10  # Value found zero times within the dictionary

    print(f"Multiple keys {reverseLookup(my_dict, val1)}")
    print(f"Single key {reverseLookup(my_dict, val2)}")
    print(f"No keys {reverseLookup(my_dict, val3)}")


if __name__ == '__main__':
    main()
