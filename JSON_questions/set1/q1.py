data={
  "items": [
    {
      "id": 1,
      "product": {
        "name": "Coffee Maker",
        "price": 49.99
      },
      "quantity": 1
    },
    {
      "id": 2,
      "product": {
        "name": "Coffee Beans",
        "price": 12.99
      },
      "quantity": 2
    }
  ]
}

'''
Questions: 
1. What properties are included in each item within the shopping cart?
2. How would you access the price of the first item's product (Coffee Maker) in this JSON data?
3. Write a function in a programming language of your choice that calculates the total price of all items in the shopping cart, considering both price and quantity.
'''

# 1st
'''
Properties would be: 
id
product -> name,price
quantity 
'''

# 2nd 
print(data["items"]["0"]["product"]["price"])

# 3rd
def calculate_price(data):
    total_price=0
    for item in data["items"]:
        product_price=item["product"]["price"]
        quantity=item["quantity"]
        total_price+=product_price*quantity
    return total_price
print(calculate_price(data=data))


