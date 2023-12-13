# Create a dictionary that represents the population of five cities.
# Perform the following operations.
Dict = {"City1": 65000, "City2": 70000, "London": 55000, "City4": 100000, "City5": 150000}
print("Dictionary: ", Dict)

# Add 2 more cities and their populations to the dictionary.
Dict.update({"City6": 23000, "City7": 49000})
print("Dict After update: ", Dict)

# Find the city with the highest population.
print("Maximum Population: ", max(Dict.items(), key=lambda x: x[1]))

# Check if a city "London" is present in the dictionary.
if "London" in Dict:
    print("City Exist")

# Remove a city and its population from dictionary.
Dict.pop("City6")
print("New Dict: ", Dict)
