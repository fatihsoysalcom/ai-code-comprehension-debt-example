import json

def process_items_ai_style(d_list, f_k='status', f_v='active', t_k='type', t_v='premium', d_r=0.1):
    """
    Simulates AI-generated code that is functional but carries 'comprehension debt'.
    This function processes a list of dictionaries (items), filtering and transforming them.
    The debt is introduced by:
    - Obscure parameter and variable names (e.g., d_list, f_k, t_v, i, c_v).
    - Dense, single-line logic without clear intermediate steps.
    - Lack of detailed comments explaining the 'why' behind the logic.
    """
    # This complex list comprehension filters items and applies a conditional transformation.
    # The short, non-descriptive variable names (i, f_k, t_k, d_r) make it hard to grasp
    # its purpose without significant mental effort.
    return [
        {'id': i.get('id'), 'final_price': round(i.get('price', 0) * (1 - d_r) if i.get(t_k) == t_v else i.get('price', 0), 2)}
        for i in d_list if i.get(f_k) == f_v
    ]

def is_active(item, status_key, active_value):
    """Checks if an item is active based on a given status key and value."""
    return item.get(status_key) == active_value

def calculate_final_price(item, type_key, premium_type, discount_rate):
    """Calculates the final price of an item, applying a discount if it's a premium type."""
    base_price = item.get('price', 0)
    if item.get(type_key) == premium_type:
        return round(base_price * (1 - discount_rate), 2)
    return round(base_price, 2)

def process_items_readable(items_list, status_key='status', active_status='active',
                           type_key='type', premium_type='premium', discount_rate=0.1):
    """
    A more readable version of the item processing, demonstrating how to reduce
    'comprehension debt' through clear naming, modularity, and comments.
    """
    processed_items = []
    for item in items_list:
        # Clear function calls and descriptive variable names enhance readability.
        if is_active(item, status_key, active_status):
            final_price = calculate_final_price(item, type_key, premium_type, discount_rate)
            processed_items.append({'id': item.get('id'), 'final_price': final_price})
    return processed_items

# Sample data to process
items_data = [
    {'id': 'A101', 'name': 'Laptop', 'price': 1200.00, 'status': 'active', 'type': 'standard'},
    {'id': 'B202', 'name': 'Monitor', 'price': 300.00, 'status': 'active', 'type': 'premium'},
    {'id': 'C303', 'name': 'Keyboard', 'price': 75.00, 'status': 'inactive', 'type': 'standard'},
    {'id': 'D404', 'name': 'Mouse', 'price': 50.00, 'status': 'active', 'type': 'standard'},
    {'id': 'E505', 'name': 'Webcam', 'price': 150.00, 'status': 'active', 'type': 'premium'},
]

print("\n--- Processing with AI-style code (high comprehension debt) ---")
# Calling the function with obscure parameters as they might appear in AI-generated code
result_ai_style = process_items_ai_style(items_data, 'status', 'active', 'type', 'premium', 0.1)
print(json.dumps(result_ai_style, indent=2))

print("\n--- Processing with readable code (low comprehension debt) ---")
# Calling the function with clear, descriptive parameters
result_readable = process_items_readable(items_data, 'status', 'active', 'type', 'premium', 0.1)
print(json.dumps(result_readable, indent=2))

print("\nNotice how both functions produce the same output, but the 'readable' version is much easier to understand and maintain.")
