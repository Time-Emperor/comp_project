n = int(input("How many numbers do you want to enter? "))
numbers = []

for _ in range(n):
    num = int(input("Enter a random integer: "))
    numbers.append(num)


asc_list = numbers.copy()
for i in range(len(asc_list)):
    for j in range(0, len(asc_list) - i - 1):
        if asc_list[j] > asc_list[j + 1]:
            asc_list[j], asc_list[j + 1] = asc_list[j + 1], asc_list[j]


desc_list = numbers.copy()
for i in range(len(desc_list)):
    for j in range(0, len(desc_list) - i - 1):
        if desc_list[j] < desc_list[j + 1]:
            desc_list[j], desc_list[j + 1] = desc_list[j + 1], desc_list[j]

print(f"Original List: {numbers}")
print(f"Ascending Order: {asc_list}")
print(f"Descending Order: {desc_list}")