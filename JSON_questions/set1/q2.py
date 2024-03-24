data={
  "name": "John Doe",
  "age": 30,
  "city": "New York"
}
'''
Questions: 
1. What is the data type of the value associated with the key "age"?
2. How would you access the value of the key "city" in this JSON data?
3. Imagine you want to add a new key-value pair to this JSON. What key-value pair would you add to specify John Doe's favorite color?
'''

# 1st
# data-type would be integer

# 2nd 
print(data["city"])

# 3rd
data["fav-color"]="Blue"
print(data)

#another question

product=[
  {
    "id": 1,
    "name": "T-Shirt",
    "price": 25.99,
    "available": 1
  },
  {
    "id": 2,
    "name": "Jeans",
    "price": 49.99,
    "available": 0
  }
]

'''
questions: 
1. How many products are there in this JSON data?
2. What is the price of the product with ID 2 (Jeans)?
3. Is the first product (T-Shirt) available for purchase?
'''

# 1st
# There are 1 product present in json

# 2nd 
price=product[1]["price"]
print(price)

# 3rd 
print(product[0]["available"])
