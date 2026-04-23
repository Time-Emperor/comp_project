m = int(input("Enter how many rows you want: "))
n= int(input("Enter how many columns you want: "))
matrix = []
for i in range(m):
    Matrix = []
    for j in range(n):
        if i == j:
            Matrix.append(1)
        elif i < j:
            Matrix.append(2)
        else:
            Matrix.append(3)
    matrix.append(Matrix)
print("\nGenerated Matrix:")
for Matrix in matrix:
    print(Matrix)