n = int(input("Enter N: "))
fib_list = [1, 1]

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print([1])
elif n == 2:
    print(fib_list)
else:
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    print(fib_list)