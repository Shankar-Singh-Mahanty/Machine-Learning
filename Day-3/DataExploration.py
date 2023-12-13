# Data Exploration:
import matplotlib.pyplot as plt
import seaborn as sns
from DataLoading import df
# Calculate basic summary statistics for the numeric columns (mean, median, min, max, standard deviation).
numeric_columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
print("Basic Statistics for the numeric columns:-\n", df[numeric_columns].describe())

# Visualize the distribution of numeric features using histograms or box plots.
# Creating histograms for numeric features
df[numeric_columns].hist(edgecolor='black', alpha=0.7)
plt.suptitle("Distribution Of Numeric Features", fontsize=16)
plt.tight_layout()
plt.show()

# Creating box plots for numeric features
sns.boxplot(data=df[numeric_columns])
plt.title("Box Plot Of Numeric Features")
plt.show()

# Explore the frequency distribution of categorical features using bar plots.
sns.countplot(data=df, x='Species')
plt.show()
