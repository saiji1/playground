letters = ["a", "b", "c"]
numbers = [ 1, 2, 3, 4, 1, 5, 6, 7]

# Add
letters.append("d")
print(letters)
letters.insert(0, "0")
print(letters)

# Remove
numbers.pop()
print(numbers)
numbers.pop(3)
print(numbers)

# Removs first number with 1
numbers.remove(1)
print(numbers)