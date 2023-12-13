# Handle missing values: Identify and handle any missing values in the dataset (e.g., imputation, removal).
from DataLoading import df
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Display the number of missing values in each column
missingValues = df.isnull().sum()
print("Missing values per column:-")
print(missingValues)

# Display the number of missing values after imputation
# Fill the missing values with the mean of each column except column4
df_imputed = df.fillna(df.drop('Species', axis=1).mean())
missingValues_after_imputation = df_imputed.isnull().sum()
print("Missing Values after imputation:-")
print(missingValues_after_imputation)

# Encode categorical variables: Convert categorical variables into numerical form
# (e.g., one-hot encoding, label encoding).
# Categorical Column
categorical_column = 'Species'
# One-Hot Encoding (Creating Dummy Variables)
data_encoded_onehot = pd.get_dummies(df, columns=[categorical_column], prefix=[categorical_column])
# Display the first few rows of the encoded data
print("One-Hot Encoded Data:")
print(data_encoded_onehot.head())

# Label Encoding
data_encoded_label = df.copy()
label_encoder = LabelEncoder()
data_encoded_label[categorical_column] = label_encoder.fit_transform(data_encoded_label[categorical_column])
# Displays the first few rows of the encoded data
print("\nLabel Encoded Data:")
print(data_encoded_label.head())
# Reverse Label Encoding(for demonstration purposes)
reverse_encoded_labels = label_encoder.inverse_transform(data_encoded_label[categorical_column])
data_encoded_label[categorical_column] = reverse_encoded_labels
# Display the first few rows of the data with reversed level encoding
print("\nData with Reversed Label Encoding:")
print(data_encoded_label.head())

# Feature scaling: Normalize or standardize numeric features to bring them to a similar scale.
numeric_columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
# Standardization
scaler_standard = StandardScaler()
data_standardized = pd.DataFrame(scaler_standard.fit_transform(df[numeric_columns]), columns=numeric_columns)
# Display the first few rows of standardized data
print("Standardized Data:")
print(data_standardized.head())

# Normalization(MinMax Scaling)
scaler_minmax = MinMaxScaler()
data_normalized = pd.DataFrame(scaler_minmax.fit_transform(df[numeric_columns]), columns=numeric_columns)
# Display the first few rows of normalized data
print("\nNormalized Data:")
print(data_normalized.head())
