"""
FizzBuzz
- methode mit input int
- wenn x / 3 = 0 then return Fizz
- wenn x / 5 = 0 then return Buzz
- wenn x / 5 && x / 3 = 0 return FizzBuzz
- wenn no cond met, return number itself
"""

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return print("FizzBuzz")
    elif input % 3 == 0:
        return print("Fizz")
    elif input % 5 == 0:
        return print("Buzz")
    else:
        return print(f"{input}")
   

fizz_buzz(3)