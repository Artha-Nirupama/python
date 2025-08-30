principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount (greater than 0): "))
    if principal <= 0:
        print("Error! Please enter a value greater than 0.")

while rate <= 0:
    rate = float(input("Enter the annual interest rate (greater than 0): "))
    if rate <= 0:
        print("Error! Please enter a value greater than 0.")
        
while time <= 0:
    time = int(input("Enter the time in years (greater than 0): "))
    if time <= 0:
        print("Error! Please enter a value greater than 0.")
    
amount = principal * (1 + rate / 100) ** time
interest = amount - principal

print(f"The amount after {time} years is: ${amount:.2f}")
print(f"The interest earned is: ${interest:.2f}")