def greet(first_name, last_name):
    print(f"Hallo {first_name} {last_name}")
    print("Welcome aboard")

greet("Saiji", "Maheswaran")
greet("Sanji", "Biri")


def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Saiji")
print(message)
""" file = open("content.txt", "w")
file.write(message) """