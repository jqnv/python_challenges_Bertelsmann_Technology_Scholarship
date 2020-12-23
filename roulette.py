# Roulette Challenge
#Option 2: Difficulty Level: Pre-Intermediate:
# A roulette wheel has 38 spaces on it. Of these spaces,
# 18 are black, 18 are red, and two #are green. The green spaces are numbered 0 and 00.
# The red spaces are numbered 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36.
# The remaining integers between 1 and 36 are used to number the black spaces....
# (please see the attached image for more detail)

from random import choice

def roulette():
    rou_dict={}
    for i in range(37):
        if i%2!=0 and i<10 or i%2==0 and i>10:
            rou_dict.update({str(i):"red"})
        elif i%2==0 and i<10 or i%2!=0 and i>10:
            rou_dict.update({str(i):"black"})
    rou_dict.update({"00":"green","0":"green"})
    selected=choice(list(rou_dict))
    select_int=int(selected)
    print(f"The spin resulted in {selected}...")
    if select_int>1:
        print("Pay Red") if rou_dict.get(selected)=="red" else print("Pay Black")
        print("Pay Even") if select_int%2==0 else print("Pay Odd")
        print("Pay 1 to 18") if select_int<19 else print("Pay 19 to 36")
    else:
        print(f"Pay {selected}")
roulette()