print("=== Electronics Store Checkout System ===")

item1_name = input("Item 1 name:")
item1_price = float(input("Item 1 price:"))
item1_qty = int(input("Item 1 quantity:"))

item2_name = input("Item 2 name:")
item2_price = float(input("Item 2 price:"))
item2_qty = int(input("Item 2 quantity:"))

item3_name = input("Item 3 name:")
item3_price = float(input("Item 3 price:"))
item3_qty = int(input("Item 3 quantity:"))

customer_name = input("Customer name:")
is_member_input = input("Is the customer a member? (yes/no):")
total_previous_purchases = float(input("Total previous purchases:"))

is_member = (is_member_input.lower() == "yes")

item1_total = item1_price * item1_qty
item2_total = item2_price * item2_qty
item3_total = item3_price * item3_qty

subtotal = item1_total + item2_total + item3_total

total_items = item1_qty + item2_qty + item3_qty

eligible_member = is_member
eligible_bulk = (total_items > 5)
eligible_loyalty = (total_previous_purchases >= 1_000_000)

member_discount = eligible_member * 0.10 * subtotal
bulk_discount = eligible_bulk * 0.05 * subtotal
loyalty_discount = eligible_loyalty * 0.03 * subtotal

total_discounts = member_discount + bulk_discount + loyalty_discount

discounted_subtotal = subtotal - total_discounts

tax = 0.12 * discounted_subtotal

shipping = (subtotal<= 500000) * 25000
free_shipping = (shipping == 0)

final_total = discounted_subtotal + tax + shipping

total_saved = total_discounts + (1- free_shipping) * 25000

print("\n========= RECEIPT =========")
print("Customer:", customer_name)
print("Member:", is_member)

print("\nItems Purchased:")
print(f"{item1_name}: {item1_qty} × {item1_price} = {item1_total}")
print(f"{item2_name}: {item2_qty} × {item2_price} = {item2_total}")
print(f"{item3_name}: {item3_qty} × {item3_price} = {item3_total}")

print("\nSubtotal:", subtotal)

print("\n--- Discounts ---")
print("Member discount eligible:", eligible_member)
print("Member discount amount:", member_discount)

print("Bulk discount eligible:", eligible_bulk)
print("Bulk discount amount:", bulk_discount)

print("Loyalty discount eligible:", eligible_loyalty)
print("Loyalty discount amount:", loyalty_discount)

print("Total discounts:", total_discounts)

print("\nSubtotal after discounts:", discounted_subtotal)
print("Tax (12%):", tax)

