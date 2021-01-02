# Many recipe books still use cups, tablespoons and teaspoons to describe
# the volumes of ingredients used when cooking or baking. While such recipes
# are easy enough to follow if you have the appropriate measuring cups and spoons,
# they can be difficult to double, triple or quadruple when cooking Christmas
# dinner for the entire extended family. For example, a recipe that calls for 4
# tablespoons of an ingredient requires 16 tablespoons when quadrupled. However,
# 16 tablespoons would be better expressed (and easier to measure) as 1 cup.
# Write a function that expresses an imperial volume using the largest units
# possible. The function will take the number of units as its first parameter,
# and the unit of measure (cup, tablespoon or teaspoon) as its second parameter.
# Return a string representing the measure using the largest possible units
# as the function’s only result...
# For example, if the function is provided with parameters representing
# 59 teaspoons then it should return the string “1 cup, 3 tablespoons,
# 2 teaspoons”. Hint: One cup is equivalent to 16 tablespoons. One tablespoon
# is equivalent to 3 teaspoons.

def reduce_measure(u, u_m):
    if u_m=="a": cup, tablespoon, teaspoon=get_from_teaspoon(u)
    if u_m=="b": cup, tablespoon, teaspoon=get_from_tablespoon(u)
    if u_m=="c":
        cup=u
        tablespoon=0
        teaspoon=0
    return f"{cup} cups, {tablespoon} tablespoon, {teaspoon} teaspoon"

def get_from_teaspoon(u):
    cup=u//48
    tablespoon=u%48//3
    teaspoon=u-(48*cup+3*tablespoon)
    return cup,tablespoon,teaspoon

def get_from_tablespoon(u):
    cup = u // 16
    tablespoon=u-(16*cup)
    return cup,tablespoon,0

if __name__ == '__main__':
    units=int(input("Please enter the number of units to convert: "))
    unit_measure=input("Please enter unit measure of the units to convert: "\
                           "\n (a) Teaspoon\n (b) Tablespoon\n (c) Cup: \n")
    print(reduce_measure(units, unit_measure))