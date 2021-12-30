import math# print(dir(math))

print(math.sqrt(4))
print(math.sqrt(9))
print(math.sqrt(43))
print(math.pi)
print(math.e)
print(math.floor(9.81)) # floor value you have convert it to lower value/ take it down.
print(math.ceil(9.81))
print(math.ceil(3.14)) # ceil will conver to the upper value / take it up.


print(round(5.5))
print(round(5.3))
print(round(3.1456, 2))

from math import sqrt # an other way of doing the above 'math.__'
print(sqrt(2))

from math import sqrt, floor, ceil, pi  # you can change the imported function name eg. you can say 'ceil as floor'
print(floor(9.81))
print(ceil(3.14))

from math import ceil as floor
print(floor(3.14))

from pprint import pprint

import random
print(dir(random))
print(random.random()) # shows random value between 0 to 0.999999
print(random.randint(0, 10)) # random int number between 0 & 10

n = random.randint(0, 10)
lottery = []
for i in range(7):
    n = random.randint(0, 10)
    lottery.append(n)

# print(lottery) # using list, set function we can avoid one number not to come repeatedly.

def get_lucky_num(n):
    import random
    lottory = []
    for i in range(7):
        n = random.randint(0, 200)
        lottory.append(n)
    return lottory

print(get_lucky_num(7))




