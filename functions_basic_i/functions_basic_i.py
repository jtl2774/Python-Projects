#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#prediction: 5 

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# prediction: 5 - exits the function upon the first return statement


# #4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# prediction: 5 


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# prediction - 5 (prints 5 to console) and blank (x does not have a value that is returned)


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# prediction - 3, 5, 8 - error with adding the functions together 


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# prediction: 25 - when adding them together as string, doesn't treat it as an addition problem


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# prediction: 100, 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#prediction: 7, 14, 21

# 2
# Moved down because there is a function being used that is not being called until later
def number_of_military_branches():
    return 5
print( number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# prediction: 5 - there is an error with the first function being called since there are no arguments being passed 

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# prediction: 8


# #11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# prediction - 500, 500, 300, 500


# #12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# prediction: 500, 500, 300, 500


# #13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# prediction: 500, 500, 300, 300

# #14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# prediction: 1, 3, 2 - the last foo() does not return anything because there is no return statement...


# #15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# 1, 3, 5, 10