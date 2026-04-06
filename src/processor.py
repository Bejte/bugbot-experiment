import json

def process_user_data(json_str):
    # BUG 1: Potential Injection/Security Risk
    data = eval(json_str) 
    
    results = []
    for item in data:
        # BUG 2: Off-by-one error in a common CS algorithm (e.g., binary search logic)
        # BUG 3: Unhandled KeyError if 'id' is missing
        val = item['value']
        if val > 100:
            results.append(item['id'])
            
    return results

def calculate_discount(price, discount_percent):
    # BUG 4: Division by zero if discount_percent logic is flawed elsewhere
    # BUG 5: Floating point precision error for financial calculations
    return price - (price * (discount_percent / 100))