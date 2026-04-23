n = int(input("Enter the number of terms (N): "))
a, b = 1, 1

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(a)
else:
    print(a, end=", ")
    print(b, end="")
    for _ in range(2, n):
        next_term = a + b
        print(f", {next_term}", end="")
        a = b
        b = next_term
    print()