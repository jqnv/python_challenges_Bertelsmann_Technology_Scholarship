# Option 1 Difficulty Level: Elementary:
# A particular zoo determines the price of admission based
# on the age of the guest. Guests 2 years of age and less
# are admitted without charge. Children between 3 and 12 years of age
# cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
# for all other guests is $23.00. Create a program that begins by
# reading the ages of all of the guests in a group from the user,
# with one age entered on each line. The user will enter a blank line
# to indicate that there are no more guests in the group.
# Then your program should display the admission cost for the group
# with an appropriate message. The cost should be displayed
# using two decimal places

def admission_cost():
    cost = 0
    while True:  # Loop continuously
        age = input("Please enter the age of the guest:")  # Get the input
        if age == "": break
        age_num = int(age)
        if 0 < age_num <= 2: cost += 0
        if 3 <= age_num < 12: cost += 14
        if 13 <= age_num < 64: cost += 23
        if 65 <= age_num: cost += 18
    print(f"The admission cost of the group is ${cost:.2f}")

admission_cost()
