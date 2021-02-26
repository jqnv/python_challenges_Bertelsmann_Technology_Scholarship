# Your function should print the highest, lowest, and average test scores for each subject
# in each class.

from os import scandir


# Function de get data from a json file and print it
def get_scores():

    # Get the list of file names within the directory
    files = scandir("scores")
    for file in files:

        # Open and read each line of each file to print it
        with open(file, encoding='utf-8-sig') as json_file:
            print(file.name)
            for line in json_file:
                print(f"\t{line}", end="")


if __name__ == '__main__':
    get_scores()
