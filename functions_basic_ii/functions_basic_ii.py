# 1 - Countdown
def countdown(num):
    for x in range(num, -1, -1):
        print(x)

countdown(5)

# 2 - Print and Return 

def print_and_value(list):
    print(list[0])
    return(list[1])

print(print_and_value([1,2]))

# 3 - First Plus Length

def first_plus_length(list):
    return list[0] + len(list)
    
print(first_plus_length([1,2,3,4,5]))

# 4 - Values Greater than Second 

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    secondList = []
    for x in range(0, len(list)):
        if list[x] > list[1]:
            secondList.append(list[x])
    print(len(secondList))
    return(secondList)

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([2]))

# 5 - This Length, That Value 

def length_and_value(size, value):
    list = []
    for x in range(0,size):
        list.append(value)
    return list

print(length_and_value(4,7))
print(length_and_value(6,2))

