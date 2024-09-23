print("Welcome to the Tip Calculator!")

# Get user input for bill
total = float(input ("What was the total bill? £"))

# Get user input of how much tip to pay
tip = int(input ("How much tip would you like to give 10%, 12% or 15%? "))

# Get user input for number of people
people = int(input ("How many people to split the bill? "))

# Calculate tip amount
tip_amount = (tip / 100)* total

# Calculate total bill
total_bill = total + tip_amount

# Calculate amount each person should pay
result = total_bill / people

# print and round result to 2 decimal places
print(f"Each person should pay £{round(result,2)}")