# Function for reuse, for testing, readability
# Function means purpose

def do_something():
    print('I am a student')

do_something()

def add_two_nums (a,b):
    total = a + b
    return total

print(add_two_nums(2,5))
print(add_two_nums(42,57))
print(add_two_nums(24,65))
print(add_two_nums(267,5))

def make_square(n):
    total = n ** 2
    return total

print(make_square(10))
print(make_square(7))
print(make_square(100))

def cal_weight(m,g):
    weight = m * g
    return f'{weight} N'

print(cal_weight(50,9.81))

for name in ['Josh', 'Meski', 'tigist']:
    print(name, name.upper())
    if len(name) >= 6:
        print(name.title(), 'You got a long name')