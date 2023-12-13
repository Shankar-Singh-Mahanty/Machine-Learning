# Step 1: Import the necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (confusion_matrix, accuracy_score, precision_score, recall_score,
                             f1_score, roc_curve, roc_auc_score)
import matplotlib.pyplot as plt

# Step 2: Load the dataset
df = pd.read_csv('BSNL.CSV')

# Step 3: Preprocess the data
# Handle missing data (if any)
# Encode categorical variables (Gender, HandsetType)
le = LabelEncoder()
df['HandsetType'] = le.fit_transform(df['HandsetType'])
df['Gender'] = le.fit_transform(df['Gender'])

# Print the mapping of labels to unique values for 'Gender'
label_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
print("To know the label encoding:\n", label_mapping)

# Define features and target variable
X = df.drop(["CustomerID", "Churn"], axis=1)  # Features
y = df['Churn']

# Step 4: Split the data into a training set and a test set
test_row_indices = [0, 5, 9]
# Create the test dataset based on the specified row indices
X_test = X.iloc[test_row_indices]
y_test = y.iloc[test_row_indices]
# Create the training dataset by excluding the rows used for testing
X_train = X.drop(test_row_indices)
y_train = y.drop(test_row_indices)

# Step 5: Define the concept for S-algorithm on training dataset
# Here, we'll create a rule to predict churn based on 'Gender' being 'Male'
concept = (X['Gender'] == 1)

# Apply the concept to predict churn
df['Churn_Predicted'] = 0  # Initialize predicted churn as 0
df.loc[concept, 'Churn_Predicted'] = 1  # Apply the rule to set churn as 1 for the selected concept

# Step 6: Evaluate the model: Compare predicted churn values to actual churn values in the test dataset
y_pred = df.loc[test_row_indices, 'Churn_Predicted']

# Step 7: Calculate the confusion matrix
confusion = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", confusion)

# Step 8: Calculate the evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Step 9: Plot the ROC curve
y_pred_proba = df.loc[test_row_indices, 'Churn_Predicted']  # Probability of positive class
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
roc_auc = roc_auc_score(y_test, y_pred_proba)

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc='lower right')
plt.show()

# Step 10: Print a report summarizing the results
report = (f"Model Evaluation Metrics:\nAccuracy: {accuracy:.3f}\nPrecision: {precision}\nRecall: {recall}\nF1-score: "
          f"{f1:.3f}\nROC AUC: {roc_auc}")
print(report)
