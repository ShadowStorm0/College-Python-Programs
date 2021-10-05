#Day of Week List
Week = ['I can only accept a number between 1 and 7. Please try again.', 'Sunday', 'Monday', 'Tuesday', 'Wedensday', 'Thursday', 'Friday' ,'Saturday']

#Introduce User to Program
print('Day of the Week Exercise')
print('Enter a number for the day of the week you want displayed.')

#Input prompt / Input Validation
while True:
  try:
    #User Input
    userInput = int(input("(Days are numbered sequentially from 1 - 7, starting with Sunday.): ")) 
    #Check if Number
  except ValueError:    
    print("I can only accept a number between 1 and 7. Please try again.\n") 
    continue
  else:  
     #Check if in Range
     if (userInput < 0 or userInput > 7):
        print("I can only accept a number between 1 and 7. Please try again.\n") 
        continue 
  break   

#Output
print(Week[userInput])
