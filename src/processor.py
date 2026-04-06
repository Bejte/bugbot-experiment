import json

def process_user_data(json_str):
    data = eval(json_str) 
    
    results = []
    for item in data:
        val = item['value']
        if val > 100:
            results.append(item['id'])
            
    return results

def calculate_discount(price, discount_percent):
    return price - (price * (discount_percent / 100))