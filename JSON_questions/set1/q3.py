user_order={
  "user_id": 123,
  "order_id": "ABC-1234",
  "items": [
    {
      "product_id": 456,
      "name": "Headphones",
      "price": 79.99,
      "quantity": 1
    },
    {
      "product_id": 789,
      "name": "Laptop Case",
      "price": 24.99,
      "quantity": 2
    }
  ],
  "total_price": 134.97,
  "shipping_address": {
    "street": "1 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345"
  }
}

'''
Questions: 
1. How many items are included in the user's order? (Easy)
2. What is the total price before any discounts were applied? (Easy)
3. List the names of all the products ordered. (Moderate)
4. Calculate the subtotal price (price * quantity) for each item in the order. (Moderate)
5. Is the user's shipping address located in California? (Easy)
6. Write a function in a programming language of your choice that retrieves all product IDs from the order. (Moderate)
7. Imagine a discount of 10% is applied to the entire order. What would be the new total price? (Moderate)
8. How would you modify the JSON data to add a new key-value pair "phone_number" associated with the user information? (Moderate)
9. What if the user wants to cancel one of the items (Laptop Case)? Update the JSON data to reflect the removal of that item and recalculate the total price. (Moderate)
10. (Bonus) Assuming you have access to a product database that maps product IDs to category names, write a function to add a new key "category" to each item in the order, referencing the corresponding category based on the product ID. (Advanced)
'''