subtotal = 0.0

while True:
    name = input("Enter item name: ")
    price = float(input(f"Enter price for {name}: "))
    quantity = int(input(f"Enter quantity for {name}: "))

    total_cost = price * quantity
    subtotal += total_cost

    more = input("Do you want to add another item? (type 'no' to stop): ").strip().lower()
    if more == 'no':
        break

vat = subtotal * 0.13
final_total = subtotal + vat

print(f"\nSubtotal: {subtotal:.2f}")
print(f"VAT (13%): {vat:.2f}")
print(f"Final Total: {final_total:.2f}")