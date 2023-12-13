# Split the dataset into training and testing sets (e.g., 80% for training, 20% for testing).
from DataLoading import df
from sklearn.model_selection import train_test_split

# Features and target variable
X = df.drop(columns=['Species'])  # Features
Y = df['Species']  # Target Variable
# Split the dataset into training and testing sets(80% training, 20%testing)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
# Display the shape of the training and testing sets
print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of Y_train:", Y_train.shape)
print("Shape of Y_test:", Y_test.shape)

# Ensure the data is in the appropriate format for the ML algorithms (e.g., arrays, matrices).
# Convert the data to arrays or matrices
X_train_array = X_train.values
X_test_array = X_test.values
Y_train_array = Y_train.values
Y_test_array = Y_test.values
# Display the type and shape of the array
print("Type of X_train_array:", type(X_train_array))
print("Shape of X_train_array:", X_train_array.shape)
print("Type of Y_train_array:", type(Y_train_array))
print("Shape of Y_train_array:", X_train_array.shape)
