import matplotlib.pyplot as plt
import numpy as np
from numpy import transpose
from numpy.linalg import inv
import random

random.seed(2019)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def poly_best_fit(x, y, power=2, invert_x=False):
	"""

	:param x: The graph X points
	:param y: THe graph Y points
	:param power: Find best fit by adjusting the number of coefficients: b_1 + b_2x^1 + b_3x^2 + ... + b_power*x^power = y
	:param invert_x: If the graph has down slope you can graphically invert X axis (does not affect calculations)
	:return:
	"""
	# Scatter plot
	plt.scatter(x, y)
	if invert_x:
		plt.xlim(max(x), min(x))
	plt.show()

	# Create X matrix
	X = np.empty((len(x), power + 1))
	# Fill X matrix
	for i, row in enumerate(X):
		for j in range(power + 1):
			X[i, j] = x[i] ** j

	XT = transpose(X)

	# solve for b (y = b0 + b1*x + b2*x^2 + b3*x^3 + ... )
	# I intentionally did it in multiple lines os I can inspect each step.
	XdotXT = np.dot(XT, X)
	inv_XdotXT = inv(XdotXT)
	_abc = np.dot(inv_XdotXT, XT)
	b = np.dot(_abc, y)

	x_reg = np.linspace(x[0], x[-1], num=100)

	# we'll use the values contained in b to calculate y (y = b0 + b1*x + b2*x^2 + b3*x^3 + ... )
	y_reg = np.empty((1, 100))  # create empty y set
	for i in range(100):  # fill it up:
		y_reg[0, i] = 0
		for j in range(power + 1):  # y_reg is the sum of the power coefficient * x to that power
			y_reg[0, i] += b[j] * x_reg[i] ** j

	# Scatter plot + Graph line plot
	plt.scatter(x, y)
	plt.plot(x, y)
	if invert_x:
		plt.xlim(max(x), min(x))
	plt.show()

	# Scatter plot + Graph line plot + Polynomial Best Fit plot
	plt.scatter(x, y)
	plt.plot(x, y)
	plt.plot(x_reg, y_reg[0])
	if invert_x:
		plt.xlim(max(x), min(x))
	plt.show()


# Set 1
set1_x = np.array([2.51, 2.99, 3.54, 4.12, 4.71, 5.29, 5.87, 6.4, 6.89, 7.1, 7.49, 7.62])
set1_y = np.array([2.3, 3.14, 4, 4.84, 5.69, 6.54, 7.39, 8.25, 9.09, 9.52, 10.37, 10.79])
#x = np.array([2.51, 4.71, 6.4])
#y = np.array([2.3, 5.69, 8.25])

# Set 2
set2_x = [7.68, 7.54, 7.22, 7.05, 6.68, 6.26, 5.8, 5.29, 4.71, 4.09, 3.37, 2.54]
set2_y = [10.79, 10.37, 9.52, 9.09, 8.25, 7.39, 6.54, 5.69, 4.84, 4, 3.14, 2.3]

poly_best_fit(set1_x, set1_y)
poly_best_fit(set2_x, set2_y, invert_x=True)

