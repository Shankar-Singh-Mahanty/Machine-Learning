# Data Loading:
# Load a dataset (Iris dataset: https://www.kaggle.com/datasets/uciml/iris) into your preferred ML environment (Python).
import pandas as pd
df = pd.read_csv("D:\\5th Sem\\LAB\\ML\\Iris.csv")
# Display the first few rows of the dataset to inspect its structure and content.
print("First 5 rows of the Iris dataset:-\n", df.head())
# Check the dimensions of the dataset (number of rows and columns).
print("Dimension of the dataset: ", df.shape)
# Identify the data types of each column (numeric, categorical, text, etc.).
print("Data types of each column:\n", df.dtypes)
