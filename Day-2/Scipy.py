# Use SciPy to perform numerical integration for a given mathematical function
import scipy.integrate as integrate
# Define the values of a and b
a = 2
b = 3
# Define the integrand as a lambda expression
f = lambda x, y: a * x ** 2 + b
# Define the ranges of integration as a list of tuples
ranges = [(0, 1), (0, 1)]
# Call nquad with the integrand and the ranges
I, err = integrate.nquad(f, ranges)
# Print the result and the error estimate
print(f"Numerical integration result: {I:.4f}")
print(f"Prime estimated error: {err:.4e}")
