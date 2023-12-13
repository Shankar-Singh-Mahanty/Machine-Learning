# Load a dataset(Iris) using pandas and display the first few rows to understand its structure.
import pandas as pd
df = pd.read_csv("D:\\5th Sem\\LAB\\ML\\Iris.csv")
print("First 5 rows of the Iris dataset:-\n", df.head())  # if no parameter is passed then prints 5rows by default.

result = df.drop(['Id', 'Species'], axis=1)
print("After removing the unnecessary columns:-\n", result)
print("Basic Statistics of the dataset:-\n", result.describe())

# Perform data filtering to extract rows based on specific conditions (e.g. SepalLengthCm>5.0)
# Applying the condition on the sepal length column
condition = df['SepalLengthCm'] > 5.0
# Storing the filtered rows in a new DataFrame
filtered_iris = df[condition]
# Display the new DataFrame
print("The rows having SepalLengthCm > 5.0 is:-\n", filtered_iris)

