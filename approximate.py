from polynomial import Polynomial
from derivatives import derivatives
import matplotlib.pyplot as plt
from math import sqrt, exp, log
from random import triangular as randrange
import numpy as np

def add_vect(v, w):
    return [vi + wi for vi, wi in zip(v, w)]

def scale(v, x):
    return [vi * x for vi in v]

def normalize(vect):
    length = sqrt(sum([ vi**2 for vi in vect ]))
    return scale(vect, 1/length)

def plot(data, pol):
    # error over time plot
    plt.subplot(221)
    plt.title('Error over time')
    plt.plot(range(len(data)), [d[0] for d in data], 'b-')
    plt.yscale('log')
    if len(data) > 100:
        plt.xscale('log')
    plt.grid(True, which='major', ls='-')
    plt.grid(True, which='minor', ls='-', color='0.65')

    # original data with computed polynomial
    plt.subplot(222)
    plt.title('Computed polynomial')
    plt.plot([p[0] for p in pol.points], 
        [p[1] for p in pol.points], 'bo')
    cpol = Polynomial(0)
    cpol.coefficients = data[-1][1]
    rng = np.arange(-10, 10, 0.5)
    plt.plot([x for x in rng], [cpol.value(x) for x in rng], 'r-')
    plt.plot([x for x in rng], [pol.value(x) for x in rng], 'b-')
    plt.grid(True, which='both', ls='--', color='0.65')

    # coefficients evolution
    plt.subplot(223)
    plt.title('Coefficients over time')
    xs = range(len(data))
    for i in range(len(data[0][1])):
        plt.plot(xs, [d[1][i] for d in data], '-')
    plt.grid(True, which='both', ls='--', color='0.65')
    plt.show()

def main(npar):
    # proxy function to hide the polynomial to the derivatives
    # module in order to reduce coupling between the two
    # 
    # note that this function must live in main's closure so that
    # it can access our polynomial. An alternative would be
    # storing that in a global variable, but that doesn't seem
    # appropriate.
    def sqr_distance(*args):
        pl = Polynomial(len(args))
        pl.coefficients = args

        # points on the polynomial with args coefficients
        y_teo = [pl.value(x[1])
            for x in pol.points]

        # random points generated previously
        y_meas = [p[1] for p in pol.points]

        # squared difference
        return sum([ (y[0] - y[1])**2
            for y in zip(y_teo, y_meas)])
    # -----
    alpha = 0.1

    pol = Polynomial(npar)
    pol.generate_points(50, 40)

    point = []
    for i in range(npar):
        point.append(randrange(-0.5, 0.5))

    plot_data = [] # (y, point)
    i = 0
    while len(plot_data) < 2 or abs(plot_data[-1][0] - plot_data[-2][0]) / 2 > 1:
        dnorm = normalize(derivatives(sqr_distance, point))

        scaling = exp(-alpha * i)
        point = add_vect(point, scale(dnorm, -scaling))

        dist = sqr_distance(*point)
        plot_data.append((dist, point))

        i += 1

    print i, 'iterations'
    plot(plot_data, pol)

if __name__ == '__main__':
    main(5)
