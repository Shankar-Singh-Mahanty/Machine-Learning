# Create a NumPy array and perform basic operations like addition, subtraction, and multiplication.
import numpy as np
# Create a numpy array
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
# Basic operation
print("Addition Result: ", arr1 + arr2)
print("Subtraction Result: ", arr1 - arr2)
print("Multiplication Result: ", arr1 * arr2)

# Use NumPy functions to calculate statistical measures like mean, median, and standard deviation.
# Statistical Measures
print("Mean of arr1: ", np.mean(arr1))
print("Median of arr2: ", np.median(arr2))
print("Standard Deviation of arr1: ", np.std(arr1))

# Reshape and slice NumPy arrays to extract specific data elements.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
reshaped_arr = arr.reshape(4, 3)
print("Reshaped Array is:-\n", reshaped_arr)
sliced_arr = arr[slice(-4, None)]
print("Sliced Array is:-\n", sliced_arr)

# Perform element-wise operations and broadcasting with NumPy arrays.
arr3 = np.array([[1, 2, 3, 4], [5, 10, 12, 15]])
arr4 = np.array([[6, 7, 8, 9], [10, 1, 7, 5]])
c = 2
print("Element wise addition:-\n", arr3 + arr4)
print("Element wise multiplication with Broadcasting:-\n", c * arr3)

# Apply mathematical functions (e.g., exponential, logarithm) to NumPy arrays.
arr5 = np.array([1, 2, 3, 4, 5])
print("Exponetial of arr5: ", np.exp(arr5))
print("Logarithim of arr5: ", np.log(arr5))
print("Square root of arr5: ", np.sqrt(arr5))
