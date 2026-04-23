matrix = [
    [24, 3, 6],
    [8, 12, 18],
    [2, 66, 7]
]
divisible_by_2_and_3 = []
all_elements = []
for row in matrix:
    for val in row:
        all_elements.append(val)
        if val % 2 == 0 and val % 3 == 0:
            divisible_by_2_and_3.append(val)
print(f"Elements divisible by 2 and 3: {divisible_by_2_and_3}")
print(f"Maximum element: {max(all_elements)}")
print(f"Minimum element: {min(all_elements)}")