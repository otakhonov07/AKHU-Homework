print("=== Coffee Shop Order System ===")
print("Enter drink sizes: smaal, medium, or large")
print("Type 'done' when finished ordering")

total = 0
price = 0

while True:
    size = input("Enter drink size:")

    if size == 'done':
        break

    elif size == 'small':
        price = 3.50

    elif size == 'medium':
        price = 4.50

    elif size == 'large':
        price = 5.50

    else:
        print("Invalid size, try again.")
        continue

    total = total + price
    print(f"Price: ${price:.2f}")
    print(f"Current total: ${total:.2f}")

if total >= 20.00:
    discount = 3.00
    print(f"Loyalty Discount: {discount}")

else:
    discount = 0

totalafterdiscount = total - discount

print("\n=== Order Summary ===")
print(f"Subtotal: {total}")
print(f"Final Total: {totalafterdiscount}")
print("Thank you for your order!")






    
    