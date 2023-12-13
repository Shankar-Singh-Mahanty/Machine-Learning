# Create a box plot to visualize the distribution of a numerical variable across different categories.
# Customize the appearance of seaborn plots using various parameters.
import seaborn as sns
import matplotlib.pyplot as plt
from Pandas import df
# Let's create a box plot for 'PetalLengthCm' for each species.
sns.boxplot(x='Species', y='PetalLengthCm', data=df, palette='Set3')
plt.xlabel('Species')
plt.ylabel('PetalLengthCm')
plt.title('Distribution Of PetalLengthCm Across Different Species')
plt.grid(True)
plt.show()


# Generate a heatmap to explore the correlation between numerical variables.
# Let's plot the correlation heatmap for the numerical columns in the dataset
numerical_column = df.select_dtypes(include=['float64', 'int64'])
sns.heatmap(numerical_column.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()
