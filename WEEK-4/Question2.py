n = int(input("How many numbers do you want to enter? "))
numbers = []

for _ in range(n):
    num = int(input("Enter integer: "))
    numbers.append(num)

# Assuming the first element is the max and min initially
if numbers:
    max_val = numbers[0]
    min_val = numbers[0]

    for num in numbers:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    print(f"List: {numbers}")
    print(f"Maximum: {max_val}")
    print(f"Minimum: {min_val}")
else:
    print("List is empty.")