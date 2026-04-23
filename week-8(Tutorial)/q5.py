numbers = []

try:
    with open("lab8.txt", "r") as file:
        for line in file:
            # Split by comma and convert each piece to an integer
            line_numbers = [int(n.strip()) for n in line.split(",") if n.strip()]
            numbers.extend(line_numbers)

    if numbers:
        print(f"Numbers: {numbers}")
        print(f"Sum: {sum(numbers)}")
        print(f"Maximum: {max(numbers)}")
        print(f"Minimum: {min(numbers)}")
    else:
        print("No numbers found in the file.")

except FileNotFoundError:
    print("The file 'lab8.txt' was not found.")
except ValueError:
    print("Ensure the file contains only numbers and commas.")