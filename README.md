Simple machine learning application which finds the optimal
parameters for a regression line using the gradient descent
method. Data is generated randomly at startup.

A csv file with the generated data is produced as well as
one containing data about every iteration (error, coefficients
and gradient).

Requires matplotlib in order to plot some graphs (original
data, error over time and parameters over time).

ml lr.py is a self contained file which correctly shows the
approximation of a regression line. approximation.py tries
to solve the same problem using arbitrary degree polynomials
and a general version of the gradient descent method.
