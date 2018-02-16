"""This is a basic implementation of a descent algorithm
    without backpropagation to evaluate the derivatives"""

x_old = 0
x_new = 6 # The algorithm starts at x=6
eps = 0.01  # step size
precision = 0.000001

def f_derivative(x):
    return 4 * x**3 - 9 * x**2

while abs(x_new - x_old) > precision:
    x_old = x_new
    x_new = x_old - eps * f_derivative(x_old)

print("Local minimum occurs at ", x_new)
print("Why not use gradient descent ????????")
