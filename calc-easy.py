command = ""
 
print("****************************")
print("Welcome to this Calc (easy v)")
print("****************************")

num1 = int(input("Input Num1 : "))
num2 = int(input("Input Num2 : "))


def addition(num1,num2):
    print(num1 + num2)

def subtraction(num1,num2):
    print(num1 - num2)

def multiplication(num1,num2):
    print(num1 * num2)

def division(num1, num2):
    print(num1 / num2)

command = input("Enter what you wanted to do (+, -, *, /): ")

match command.lower():
    case "addition" | "+":
        addition(num1,num2)
    case "subtraction" | "-":
        subtraction(num1,num2)
    case "multiplication" | "*":
        multiplication(num1,num2)
    case "division" | "/":
        division(num1,num2)
    
