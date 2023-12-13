# Create a tuple with five elements, each representing the price of a product.
# Perform the following operations.
Price = (1050, 2500, 758, 15000, 8000)

# Find the maximum and minimum price of the tuple.
print("Maximum price: ", max(Price))
print("Minimum price: ", min(Price))

# Calculate the total cost of all the products.
print("Total cost: ", sum(Price))

# Convert the tuple to a list and add a new product with its price.
Price_List = list(Price)
print("List= ", Price_List)
Price_List.append(23000)
print("After append: ", Price_List)

# Calculate the average price of the products.
print("Average: ", sum(Price_List)/len(Price_List))
