#introduces the program to the user
print ("Welcome to the number counter. This program adds all numbers between two values.\n")

#user input for low number
while True:
  try:
    #user input
    low = int(input("Please input the low number: ")) 
  except ValueError:    
    print("Please try again and input valid values!\n") 
    continue
  break

#user input for high number
while True:
  try:
    #user input
    high = int(input("Please input the high number: ")) 
  except ValueError:    
    print("Please try again and input valid values!\n")
    continue
  break

#check if low number is greater then high number
if(low > high):
  print("Your second number must be higher than the first! Please try again.\n")
  quit()
  
#prints all numbers between and including low and high
else:
  for num in range (low, high +1):
    print(num)
    
#calculation
total = 0
for i in range(low, high + 1):
  total = total + i
  i = i + 1

#output
print("The total of all numbers is:  " + str(total))
    
