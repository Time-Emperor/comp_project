existing_list = [1, 2, 3, 4, 5, 6]
reversed_list = []

for i in range(len(existing_list) - 1, -1, -1):
    reversed_list.append(existing_list[i])

print(f"Reversed list: {reversed_list}")