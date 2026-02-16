# This simulates raw data from a Retail API
raw_data = [
    {"id": 1, "name": "Laptop", "info": {"price": 1200, "stock": 5}},
    {"id": 2, "name": "Mouse", "info": {"price": 25, "stock": 50}},
    {"id": 3, "name": "Keyboard", "info": {"price": 75, "stock": 10}}
]

# Intermediate Method: List Comprehension 
# It's a faster, one-line way to write a 'for loop'
prices = [item["info"]["price"] for item in raw_data]

# Validation: Let's calculate the total value of stock
# price * stock for each item
total_stock_value = sum(item["info"]["price"] * item["info"]["stock"] for item in raw_data)

print(f"Extracted Prices: {prices}")
print(f"Total Warehouse Value: ${total_stock_value}")