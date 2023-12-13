# Create a Python list containing the names of five countries. Perform the following operations.
Country = ["India", "Australia", "Africa", "America", "England"]
print("Before append: ", Country)

# Add 2 more countries to the list.
Country.append("Pakistan")
Country.append("Russia")
print("After append: ", Country)

# Print the 3rd country in the list.
print("Third country: ", Country[2])

# Sort the list in alphabetical order.
Sorted_List = sorted(Country)
print("Sorted List: ", Sorted_List)

# Check if a country "India" is present in the list.
if "India" in Country:
    print("Country Exists in the list.")
