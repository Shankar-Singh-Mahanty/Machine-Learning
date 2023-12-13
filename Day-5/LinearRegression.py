import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate synthetic data for dataset-1
np.random.seed(0)
X1 = np.random.rand(100, 1) * 50
Y1 = 4 * X1 + 13 + np.random.randn(100, 1)

# Generate synthetic data for dataset-2
X2 = np.random.rand(100, 2) * 50
Y2 = 10 * np.sin(X2[:, 0]) + 15 * np.sin(X2[:, 1]) + np.random.randn(100)

# Loading Boston Housing dataset
df = pd.read_csv("..//Boston.csv")
print(df.head())
X_boston = df.drop(columns=['medv']).values
Y_boston = df['medv'].values


# Linear Regression using matrix formulation (analytic solution)
def linear_regression_analytic(X, Y):
    # Implement the analytic solution for linear regression
    W = np.linalg.inv(X.T @ X) @ X.T @ Y
    return W


# Linear Regression using gradient descent
def linear_regression_gradient_descent(X, Y, learning_rate, iterations):
    # Initialize weights
    W = np.random.randn(X.shape[1], 1)

    for _ in range(iterations):
        # Update weights using gradient descent
        gradient = -(2 / len(Y)) * X.T @ (Y - X @ W)
        W -= learning_rate * gradient

    return W


# Calculate the sum of residual errors
def sum_residual_errors(Y, Y_pred):
    return np.sum((Y - Y_pred) ** 2)


# Plot the data points and regression line
def plot_regression_line(X, Y, W, title):
    plt.scatter(X, Y, color='blue', label='Data Points')
    plt.plot(X, X @ W, color='red', label='Regression Line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.legend()
    plt.show()


# Analytic solution for dataset-1
W1_analytic = linear_regression_analytic(X1, Y1)
Y1_pred_analytic = X1 @ W1_analytic
residual_error1_analytic = sum_residual_errors(Y1, Y1_pred_analytic)

# Gradient Descent for dataset-1
learning_rate = 0.01
iterations = 100
W1_gradient = linear_regression_gradient_descent(X1, Y1, learning_rate, iterations)
Y1_pred_gradient = X1 @ W1_gradient
residual_error1_gradient = sum_residual_errors(Y1, Y1_pred_gradient)

# Analytic solution for dataset-2
W2_analytic = linear_regression_analytic(X2, Y2)
Y2_pred_analytic = X2 @ W2_analytic
residual_error2_analytic = sum_residual_errors(Y2, Y2_pred_analytic)

# Gradient Descent for dataset-2
Y2 = Y2.reshape(-1, 1)  # Reshape Y2 to match X2's shape
W2_gradient = linear_regression_gradient_descent(X2, Y2, learning_rate, iterations)
Y2_pred_gradient = X2 @ W2_gradient
residual_error2_gradient = sum_residual_errors(Y2, Y2_pred_gradient)

# Display sum of residual errors
print("Sum of Residual Errors for Dataset-1 (Analytic):", residual_error1_analytic)
print("Sum of Residual Errors for Dataset-1 (Gradient Descent):", residual_error1_gradient)
print("Sum of Residual Errors for Dataset-2 (Analytic):", residual_error2_analytic)
print("Sum of Residual Errors for Dataset-2 (Gradient Descent):", residual_error2_gradient)

# Plot regression lines for dataset-1
plot_regression_line(X1, Y1, W1_analytic, "Linear Regression - Dataset-1 (Analytic)")
plot_regression_line(X1, Y1, W1_gradient, "Linear Regression - Dataset-1 (Gradient Descent)")

# Plot regression lines for dataset-2
plot_regression_line(X2[:, 0], Y2, W2_analytic, "Linear Regression - Dataset-2 (Analytic)")
plot_regression_line(X2[:, 0], Y2, W2_gradient, "Linear Regression - Dataset-2 (Gradient Descent)")


# Decaying learning rate function
def decay_learning_rate(initial_lr, epoch, decay_rate):
    return initial_lr / (1 + decay_rate * epoch)


# Full Batch Gradient Descent
def full_batch_gradient_descent(X, Y, learning_rate, iterations, decay_rate=0):
    W = np.random.randn(X.shape[1], 1)
    residual_errors = []

    for epoch in range(iterations):
        learning_rate_decay = decay_learning_rate(learning_rate, epoch, decay_rate)
        gradient = -(2 / len(Y)) * X.T @ (Y - X @ W)
        W -= learning_rate_decay * gradient

        Y_pred = X @ W
        residual_error = sum_residual_errors(Y, Y_pred)
        residual_errors.append(residual_error)

    return W, residual_errors


# Stochastic Gradient Descent
def stochastic_gradient_descent(X, Y, learning_rate, iterations, decay_rate=0):
    W = np.random.randn(X.shape[1], 1)
    residual_errors = []

    for epoch in range(iterations):
        learning_rate_decay = decay_learning_rate(learning_rate, epoch, decay_rate)

        for i in range(len(Y)):
            random_idx = np.random.randint(len(Y))
            x_i = X[random_idx, :].reshape(1, -1)
            y_i = Y[random_idx]

            gradient = -(2 / len(Y)) * x_i.T @ (y_i - x_i @ W)
            W -= learning_rate_decay * gradient

        Y_pred = X @ W
        residual_error = sum_residual_errors(Y, Y_pred)
        residual_errors.append(residual_error)

    return W, residual_errors


# Mini-Batch Stochastic Gradient Descent
def mini_batch_gradient_descent(X, Y, learning_rate, iterations, batch_size, decay_rate=0):
    W = np.random.randn(X.shape[1], 1)
    residual_errors = []

    for epoch in range(iterations):
        learning_rate_decay = decay_learning_rate(learning_rate, epoch, decay_rate)

        for i in range(0, len(Y), batch_size):
            x_batch = X[i:i + batch_size, :]
            y_batch = Y[i:i + batch_size]

            gradient = -(2 / len(y_batch)) * x_batch.T @ (y_batch - x_batch @ W)
            W -= learning_rate_decay * gradient

        Y_pred = X @ W
        residual_error = sum_residual_errors(Y, Y_pred)
        residual_errors.append(residual_error)

    return W, residual_errors


# Apply gradient descent methods to dataset-1 with different learning rates
learning_rates = [0.01, 0.05, 0.1]
iterations = 100
decay_rate = 0.01
batch_size = 10

for lr in learning_rates:
    # Full Batch Gradient Descent
    W_full_batch, residual_errors_full_batch = full_batch_gradient_descent(X1, Y1, lr, iterations, decay_rate)
    plot_regression_line(X1, Y1, W_full_batch, f"Full Batch GD (LR={lr}) - Dataset-1")

    # Stochastic Gradient Descent
    W_stochastic, residual_errors_stochastic = stochastic_gradient_descent(X1, Y1, lr, iterations, decay_rate)
    plot_regression_line(X1, Y1, W_stochastic, f"Stochastic GD (LR={lr}) - Dataset-1")

    # Mini-Batch Stochastic Gradient Descent
    W_mini_batch, residual_errors_mini_batch = mini_batch_gradient_descent(X1, Y1, lr, iterations, batch_size,
                                                                           decay_rate)
    plot_regression_line(X1, Y1, W_mini_batch, f"Mini-Batch GD (LR={lr}) - Dataset-1")

# Apply gradient descent methods to dataset-2 with different learning rates
for lr in learning_rates:
    # Full Batch Gradient Descent
    W_full_batch, residual_errors_full_batch = full_batch_gradient_descent(X2, Y2, lr, iterations, decay_rate)
    plot_regression_line(X2[:, 0], Y2, W_full_batch, f"Full Batch GD (LR={lr}) - Dataset-2")

    # Stochastic Gradient Descent
    W_stochastic, residual_errors_stochastic = stochastic_gradient_descent(X2, Y2, lr, iterations, decay_rate)
    plot_regression_line(X2[:, 0], Y2, W_stochastic, f"Stochastic GD (LR={lr}) - Dataset-2")

    # Mini-Batch Stochastic Gradient Descent
    W_mini_batch, residual_errors_mini_batch = mini_batch_gradient_descent(X2, Y2, lr, iterations, batch_size,
                                                                           decay_rate)
    plot_regression_line(X2[:, 0], Y2, W_mini_batch, f"Mini-Batch GD (LR={lr}) - Dataset-2")

# Apply gradient descent methods to Boston Housing dataset
for lr in learning_rates:
    # Full Batch Gradient Descent
    W_full_batch, residual_errors_full_batch = full_batch_gradient_descent(X_boston, Y_boston, lr, iterations, decay_rate)
    plot_regression_line(X_boston.reshape(-1, 1), Y_boston, W_full_batch, f"Full Batch GD (LR={lr}) - Boston Housing")

    # Stochastic Gradient Descent
    W_stochastic, residual_errors_stochastic = stochastic_gradient_descent(X_boston, Y_boston, lr, iterations, decay_rate)
    plot_regression_line(X_boston.reshape(-1, 1), Y_boston, W_stochastic, f"Stochastic GD (LR={lr}) - Boston Housing")

    # Mini-Batch Stochastic Gradient Descent
    W_mini_batch, residual_errors_mini_batch = mini_batch_gradient_descent(X_boston, Y_boston, lr, iterations, batch_size,
                                                                           decay_rate)
    plot_regression_line(X_boston.reshape(-1, 1), Y_boston, W_mini_batch, f"Mini-Batch GD (LR={lr}) - Boston Housing")
