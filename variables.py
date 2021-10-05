#Input prompts
hour_Input = float(input("Input hours worked: "))
pay_Rate = float(input("Input hourly pay rate: "))

#calculates total pay
total = hour_Input * pay_Rate

#output
print("Your total pay is: " + str(total))
