command = ""

num1 = 0
num2 = 0

while command.lower() != "quit":
    command = input("Enter a command: ")
    print("ECHO ", command)
    if command == "addition":
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter second number: "))
        print("The sum is: ", num1 + num2)
else: 
    print("u quitted, bye")
