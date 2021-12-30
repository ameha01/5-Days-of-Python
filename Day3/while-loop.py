count = 0
""" while count < 6:
    print(count)
    count = count + 1

    count =  5
    while count < - 1:
        print(count)
        count = count - 1
 """
def make_square(n):
    square = n ** 2 # you can also write 'n * n'
    return square

print(make_square(2))
print(make_square(3))
print(make_square(10))

def cal_weight(mass, gravity):
    weight = mass * gravity
    return f' {weight} N'

    
print(cal_weight(75, 9.81))
print(cal_weight(75, 1.65))