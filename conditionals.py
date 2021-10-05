#Input prompts
hour_Input = float(input("Input hours worked: "))
pay_Rate = float(input("Input hourly pay rate: "))

#calculates total pay
if hour_Input <= 40:
  total = hour_Input * pay_Rate
else:
  #for over 40 hours
  Overtime = (pay_Rate * 1.5) * (hour_Input - 40)
  total = Overtime + (40 * pay_Rate)

#output
print("Your total pay is: " + str(total))
