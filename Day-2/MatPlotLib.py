# Create a line plot to visualize the trend of a numerical variable over time
# Import matplotlib.pyplot as plt and df from Pandas.py
import matplotlib.pyplot as plt
from Pandas import df

# Create a line plot to visualize the trend of a numerical variable over time.
# Plotting the variables
plt.plot(df['SepalLengthCm'], marker='o', linestyle='-', color='r')
# Labeling the axes
plt.xlabel('Index')
plt.ylabel('SepalLengthCm')
# Giving a title to the plot
plt.title('Trend Of Sepal Length Over Time')
plt.grid(True)
# Displaying the plot
plt.show()

# Generate a histogram to understand the distribution of a numerical variable in the dataset
plt.hist(df['SepalWidthCm'], edgecolor='black', color='skyblue')
# Label the x and y axes
plt.xlabel('SepalWidthCm')
plt.ylabel('Frequency')
# Give a title to the plot
plt.title('Distribution of Sepal Width of Iris Flowers')
plt.grid(True)
# Display the plot
plt.show()

# Create a bar chart to compare the performance of different categories.
# Let's compare the average PetalLengthCm for each species
avg_petal_length = df.groupby('Species')['PetalLengthCm'].mean()
species_names = avg_petal_length.index
plt.bar(species_names, avg_petal_length, color=['r', 'orange', 'g'])
plt.xlabel('Species ->')
plt.ylabel('Average Petal Length (Cm)')
plt.title('Performance Of Avg. Petal Length Of Different Species')
plt.grid(True)
plt.show()

# Plot a scatter plot to explore the relationship between two numerical variables.
# Customize your plots with labels, titles, colors, and styles.
# Plot the sepal length and width variables
plt.scatter(df['SepalLengthCm'], df['SepalWidthCm'], c=df['SepalLengthCm'], cmap='rainbow',
            s=df['SepalWidthCm'] * 15, alpha=0.5, marker='*')
# Label the x and y axes
plt.xlabel('SepalLengthCm', fontname='Bookman Old Style', size=14, color='blue')
plt.ylabel('SepalWidthCm', fontname='Bookman Old Style', size=14, color='green')
# Give a title to the plot
plt.title('Scatter Plot of Sepal Length and Width of Iris Flowers', c='red')
# To show the color scale
plt.colorbar()
# Display the plot
plt.grid(True)
plt.show()
