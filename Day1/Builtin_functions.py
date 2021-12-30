# what is function?
# a set of code to use, re-use, to test, ..
# functions usually have names
# there are 2 types of fuctions
# 1) Builtin function and 2) custom fucntion
# exist(), print(), len(), input(), round(), help(), dir(), int, str, float, range
print('input 1', 'input 2', 'whaterver you', 2021, False)

statment = 'I love python.'
word = 'Python'
skills = ['Html', 'CSS', 'JS', 'Python']
print(len(skills))
print(len(word))
print(len(statment))

""" first_name = input('Enter your first name:')
year_born = int(input('Enter the year you were both:'))
current_year = 2021
print('You are', first_name)
age = current_year - year_born
print('You are ' + str(age) + ' ' + 'years old.') """

""" r = float(input('Enter the r of the circle'))
area = 3.14 * r ** 2
print('The area of the circle is' + str(round(area, 3)) + 'sq.meter.')
 """
print(max(100, 1, 2, 3, 4, 5, 6))
print(min(100, 1, -2, 3, 4, 5 , 6))
print(sum([100, 1, -2, 3, 4, 5, 6]))
print(help('keywords'))

first_name = 'John'
print(first_name.startswith('J'))
print(dir(first_name))

a = 10
print(type(a))
print(float(a))
print(int(str(10)))

g = '9.81'
print(float(g))
print(int(float(g)))
print(type(g))

# range mean is from some point up to some other point.
# range should have (start, end, step)

nums = list(range(5))
print(nums)
evens = list(range(0,101,2))
print(evens)
odds = list(range(1,101,2))
print(odds)

# 60 - 80 even numbers that include ranges includes 60 to 80
print(list(range(60,81, 2)))

# 51 to 69 odd numbers that includes the two ranges
print(list(range(51, 70, 2)))

for i in range(10):
    print(a)