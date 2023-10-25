# 1
for i in range(151):
    print(i)

# 2
for x in range(5, 1001):
    if(x % 5 == 0):print(x)

# 3
for y in range(1, 101):
    if(y % 10 == 0):
        print("Coding Dojo")
    elif( y % 5 == 0): 
        print("Coding")    
    else: print(y)

# 4
sum = 0
for z in range(1,500001,2):    
    sum += z
print(sum)

# 5    
for p in range(2018, 0, -4):
    print(p)

# 6
lowNum = 2
highNum = 9
mult = 3
for g in range(lowNum, highNum + 1):
    if (g % mult == 0):
        print(g)
