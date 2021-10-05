#introduces the program to the user
print ("Welcome to the Tip Calculator\n")

#Input prompt / cost validation
while True:
  try:
    #user input
    cost = float(input("What is the cost of the meal? ")) 
  except ValueError:    
    print("Please try again and input a valid number\n") 
    continue
  else:  
     #check for 0 and negative
     if (cost <= 0):
       print("Please try again and input a valid number\n") 
       continue 
  break   

#calculation 15% Function / finds tip amount + adds to base
def tip():
  tip = cost * .15
  total_Cost = tip + cost
  return total_Cost

#output
print ("Your total with 15% tip is: $ " + str(tip()))
