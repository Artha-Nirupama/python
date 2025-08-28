print("***Calculater***")

try:
    num1=float(input("Enter your First Number: "))
except:
    print("Error!Please only enter Intiger or floating point number")
    
try:
    Operater=input("Enter the Operater(Ex:+,-,*,/,%,^): ")
except:
    print("Error!Please only enter one charecter(Ex:+,-,*,/,%,^)")

try:
    num2=float(input("Enter the Secound Number: "))
except:
    print("Error!Please only enter Intiger or floating point number")
    
match Operater:
    case "+":
        print(round(num1 + num2,3))
    case "-":
        print(round(num1 - num2,3))
    case "*":
        print(round(num1 * num2,3))
    case "/":
        print(round(num1 / num2,3))
    case "%":
        print(round(num1 % num2,3))
    case "^":
        print(round(pow(num1, num2,3)))
    case " ":
        print("Error!Please only enter one charecter(Ex:+,-,*,/,%,^)")