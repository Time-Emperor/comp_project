n = int(input("How many numbers do you want to enter? "))
numbers = []

for _ in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

odd_sum = sum(x for x in numbers if x % 2 != 0)
even_sum = sum(x for x in numbers if x % 2 == 0)

print(f"Sum of odd numbers: {odd_sum}")
print(f"Sum of even numbers: {even_sum}")