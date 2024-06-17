numbers = [3,41,53,5234,234,5,1]
numbers.sort(reverse=True)
print(numbers)


items = [
    ("Product1", 103),
    ("Product2", 103333434342),
    ("Product3", 1423430),
    ("Product4", 1432420),
    ("Product5", 1432510),
    ("Product6", 132520),
]

items.sort(key=lambda item:item[1])
print(items)