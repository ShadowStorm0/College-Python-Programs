#user input for name
name = str(input("Please input your first and last name, separated by a space\n")) 
 
#spliting string from the space [Creating an array]
seperate = name.split(' ')

#output first and last name to user
print("First Name: " + seperate[0])
print("Last Name: " + seperate[1])
 
 
 
