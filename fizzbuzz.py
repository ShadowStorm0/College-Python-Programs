list = []

for i in range (1, 101):
    
    if (i % 15 == 0):
        list.append(str(i)+ ": fizzbuzz")
    elif (i % 3 == 0):
        list.append(str(i)+ ": fizz")
    elif (i % 5 == 0):
        list.append(str(i)+ ": buzz")
    else:
        list.append(i)
    
print (list)
