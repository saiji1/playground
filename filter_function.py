items = [
    ("MacBook", 1999),
    ("RTX 3090", 799),
    ("Galaxy S23", 899),
]

filter_higher = list(filter(lambda item: item[1] >= 802, items))
print(filter_higher)



"""
# Create a new list to store items with price more than 400
filtered_items = []

# Iterate through the existing list of tuples
for item in items:
    # Check if the price is more than 400
    if item[1] > 802:
        # Add the item to the new list
        filtered_items.append(item)

# Output the new list
print(filtered_items)
"""