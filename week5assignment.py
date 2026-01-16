def add_new_orders(orders, new_orders):
    orders.extend(new_orders)

def process_orders(orders, num_to_process):
    num_to_process = min(num_to_process, len(orders))
    processed = orders[:num_to_process]
    del orders[:num_to_process]
    return processed

def cancel_order(orders, order_id):
    if order_id in orders:
        orders.remove(order_id)
        return True
    else:
        return False
    
def manage_orders(initial_orders, new_orders_to_add, orders_to_process, order_to_cancel):
    orders = initial_orders.copy()
    add_new_orders(orders, new_orders_to_add)
    cancel_order(orders, order_to_cancel)
    processed_orders = process_orders(orders, orders_to_process)

    return orders, processed_orders

initial = [101, 102, 103, 104]
new = [105, 106]
process_count = 3
cancel_id = 103

final_state, processed = manage_orders(initial, new, process_count, cancel_id)

print("Final queue:", final_state)
print("Processed orders:", processed)
print("Original initial list:", initial)