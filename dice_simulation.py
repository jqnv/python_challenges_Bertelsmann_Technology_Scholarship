# In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a function that simulates rolling
# a pair of six-sided dice. Your function will not take any parameters. It will return the total that was rolled on
# two dice as its only result.
# Write a main program that uses your function to simulate rolling two six-sided dice 1,000 times. As your program runs,
# it should count the number of times that each total occurs. Then it should display a table that summarizes this data.
# Express the frequency for each total as a percentage of the total number of rolls. Your program should also display
# the percentage expected by probability theory for each total. Sample output is shown below
from random import randint


def dice_simulation():
    # Create a blank dictionary
    my_dict = {}

    # Fill the dictionary with the possible total as keys
    for i in range(2, 13):
        my_dict.update({str(i): 0})

    # Initialize variables to count the occurrences of each total
    v_2, v_3, v_4, v_5, v_6, v_7, v_8, v_9, v_10, v_11, v_12 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    # Simulate 2 dices rolling
    for i in range(1000):
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)

        # Increase each variable according to the total obtained
        if dice1 + dice2 == 2: v_2 += 1
        if dice1 + dice2 == 3: v_3 += 1
        if dice1 + dice2 == 4: v_4 += 1
        if dice1 + dice2 == 5: v_5 += 1
        if dice1 + dice2 == 6: v_6 += 1
        if dice1 + dice2 == 7: v_7 += 1
        if dice1 + dice2 == 8: v_8 += 1
        if dice1 + dice2 == 9: v_9 += 1
        if dice1 + dice2 == 10: v_10 += 1
        if dice1 + dice2 == 11: v_11 += 1
        if dice1 + dice2 == 12: v_12 += 1

    # Filling the dictionary with a list as value
    my_dict.update({"2": [v_2 / 1000 * 100, 2.78]})
    my_dict.update({"3": [v_3 / 1000 * 100, 5.56]})
    my_dict.update({"4": [v_4 / 1000 * 100, 8.33]})
    my_dict.update({"5": [v_5 / 1000 * 100, 11.11]})
    my_dict.update({"6": [v_6 / 1000 * 100, 13.89]})
    my_dict.update({"7": [v_7 / 1000 * 100, 16.67]})
    my_dict.update({"8": [v_8 / 1000 * 100, 13.89]})
    my_dict.update({"9": [v_9 / 1000 * 100, 11.11]})
    my_dict.update({"10": [v_10 / 1000 * 100, 8.33]})
    my_dict.update({"11": [v_11 / 1000 * 100, 5.56]})
    my_dict.update({"12": [v_12 / 1000 * 100, 2.78]})

    # Print the table
    print(f"Total\tSimulated\tExpected")
    print(f"\t\tPercent\t\tPercent")
    for k, v in my_dict.items():
        print(f"{k}\t\t{format(v[0], '.2f')}\t\t{v[1]}")


if __name__ == '__main__':
    dice_simulation()
