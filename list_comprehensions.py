items = [
    ("Product 1", 10),
    ("Product 2", 22),
    ("Product 3", 54),
    ("Product 4", 32),
    ("Product 5", 145)
]
# Normal way
prices = list(map(lambda item: item[1], items))
# More elegant way way
prices = [item[1] for item in items]



# Normal way
filtered = list(filter(lambda item: item[1] >= 30, items))

# More elegant way way
filtered = [item for item in items if item[1] >= 30]

print(prices)
print(filtered)