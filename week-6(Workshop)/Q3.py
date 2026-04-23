'''
matrix_a = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]
sum_diagonal = 0
sum_above = 0
sum_below = 0
max_val = matrix_a[0][0]
min_val = matrix_a[0][0]
for i in range(len(matrix_a)):
    for j in range(len(matrix_a[i])):
        current = matrix_a[i][j]
        if i == j:
            sum_diagonal += current
        elif j > i:
            sum_above += current
        elif i > j:
            sum_below += current
        if current > max_val:
            max_val = current
        if current < min_val:
            min_val = current
print(f"Matrix A Results:")
print(f"Sum of diagonal elements: {sum_diagonal}")
print(f"Sum of elements above diagonal: {sum_above}")
print(f"Sum of elements below diagonal: {sum_below}")
print(f"Maximum element: {max_val}")
print(f"Minimum element: {min_val}")
'''

matrix_b = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

sum_diagonal = 0
sum_above = 0
sum_below = 0

max_val = matrix_b[0][0]
min_val = matrix_b[0][0]
for i in range(len(matrix_b)):
    for j in range(len(matrix_b[i])):
        current = matrix_b[i][j]
        if i == j:
            sum_diagonal += current
        elif j > i:
            sum_above += current
        elif i > j:
            sum_below += current

        if current > max_val:
            max_val = current
        if current < min_val:
            min_val = current

print(f"Matrix B Results:")
print(f"Sum of diagonal elements: {sum_diagonal}")  # 2 + 5 + 8
print(f"Sum of elements above diagonal: {sum_above}")  # 7 + 6 + 1
print(f"Sum of elements below diagonal: {sum_below}")  # 9 + 4 + 3
print(f"Maximum element: {max_val}")
print(f"Minimum element: {min_val}")