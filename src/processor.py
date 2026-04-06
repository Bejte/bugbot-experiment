import json

def process_user_data(json_str):
    # BUG 1: The 'eval' risk
    data = eval(json_str) 
    
    results = []
    for item in data:
        # BUG 2: Unhandled KeyError if 'id' is missing
        val = item['value']
        if val > 100:
            results.append(item['id'])
            
    return results

def calculate_discount(price, discount_percent):
    # BUG 3: Potential DivisionByZero and precision errors
    return price - (price * (discount_percent / 100))