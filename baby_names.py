# The baby names data set consists of over 200 files (data sets are attached to this message). Each file contains a
# list of 100 names, along with the number of times each name was used. Entries in the files are ordered from most
# frequently used to least frequently used. There are two files for each year: one containing names used for girls
# and the other containing names used for boys. The data set includes data for every year from 1900 to 2012.
# Write a program that reads every file in the data set and identifies all of the names that were most popular in at
# least one year. Your program should output two lists: one containing the most popular names for boys and the other
# containing the most popular names for girls. Neither of your lists should include any repeated values.

from os import scandir


def baby_names():
    try:
        files = scandir('BabyNames')
        b_names = []
        g_names = []
        for file in files:
            with open(file, 'r') as f:
                name = f.readline().split()
                if f.name.count("Boys") > 0:
                    b_names.append(name[0])
                else:
                    g_names.append(name[0])
        print(f"The most popular names for for boys from 1900 to 2012 are: {list(set(b_names))}")
        print(f"The most popular names for for girls from 1900 to 2012 are: {list(set(g_names))}")
    except FileNotFoundError:
        print("Path specified cannot be found")
    except IOError:
        print("File not found")


if __name__ == '__main__':
    baby_names()
