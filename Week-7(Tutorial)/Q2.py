def sum_string_digits():
    num_string = input("Enter a string of numbers: ")

    total_sum = 0

    for char in num_string:
        if char.isdigit():
            total_sum += int(char)
        else:
            print(f"Skipping '{char}' because it is not a number.")

    print(f"The sum of the numbers is: {total_sum}")

sum_string_digits()