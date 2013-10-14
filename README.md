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


NOTES:
When approximating a linear function it is enough to scale
the gradient by a sufficiently small constant factor in order
to find the only minima of the cost function (i.e. the least
squared difference).

On the other hand, as the degree of the polynomial to be
approximated increases, the function becomes more and more
steep, thus making the gradient descent method overshot the
minima and, eventually, overflow.

It is possible to counteract this behavior using a variable
scaling factor and normalizing the gradient: exp(-alpha * t) *
* normalized gradient. Plotting a graph shows that the point
oscillates around the (local) minima and converges to it
after a number of iterations depending on alpha. Increasing
the precision used to calculate the derivatives is also of
help.

The graphs show that the only coefficient which varies
significantly is the one associated with the highest degree;
this makes sense because it is the one which makes the gradient
change the most even with the slightest variation. It is also
evident that most of the times the gradient descent method gets
stuck in local minimas because, even though the approximation error
converges to a steady value, the computed polynomial is evidently
different from the starting one.
