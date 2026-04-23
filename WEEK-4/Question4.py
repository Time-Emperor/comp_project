existing_list = [1, 1, 2, 3, 3, 4, 4, 5, 6, 5, 6]
unique_list = []

for item in existing_list:
    if item not in unique_list:
        unique_list.append(item)

print(f"Unique elements: {unique_list}")