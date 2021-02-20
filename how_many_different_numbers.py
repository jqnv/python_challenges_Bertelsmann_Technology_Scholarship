# Function returns how many unique numbers within a list

def how_many_different_numbers(numb_list):

    # Convert list into a set to eliminate duplicates
    unique_numbers=set(numb_list)

    # Return the length of the set
    return len(unique_numbers)


if __name__ == '__main__':

    # Declare list of integers
    numb_list=[1, 2, 3, 1, 2, 3, 4, 1]

    # Print the return of the function sending numbers list as an argument
    print(how_many_different_numbers(numb_list))