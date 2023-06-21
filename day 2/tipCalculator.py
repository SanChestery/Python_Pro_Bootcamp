print("Welcome to the tip calculator")

# Variables
bill = float(input("What was the total bill: $"))
tipPerc = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

finalTip = bill * (tipPerc / 100)
finalBill = (finalTip + bill) / people

# Output 
print("In total, Each person should pay: $" + str(round(finalBill, 2)))
