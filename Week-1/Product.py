subtotal = 0.0

while True:
    name = input("Enter the product name: ")
    price = float(input(f"Enter the price for {name}: "))

    if price < 0:
        print("Negative price skipped.")
    else:
        subtotal += price

    more = input("Do you want to add another item? (Yes/No): ").strip().lower()
    if more == "no":
        break

tax = subtotal * 0.13
total = subtotal + tax

delivery = input("Do you want the products delivered? (Yes/No): ").strip().lower()
if delivery == "yes":
    total += 100

print(f"\nSubtotal: {subtotal:.2f}")
print(f"Tax (13%): {tax:.2f}")
print(f"Final Total: {total:.2f}")