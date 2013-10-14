from polynomial import Polynomial
from derivatives import derivatives
import matplotlib.pyplot as plt
from math import sqrt, exp
from random import triangular as randrange

def add_vect(v, w):
    return [vi + wi for vi, wi in zip(v, w)]

def scale(v, x):
    return [vi * x for vi in v]

def normalize(vect):
    length = sqrt(sum([ vi**2 for vi in vect ]))
    return scale(vect, 1/length)

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

    plot_y = []

    for i in range(300):
        dnorm = normalize(derivatives(sqr_distance, point))

        scaling = exp(-alpha * i)
        point = add_vect(point, scale(dnorm, -scaling))

        dist = sqr_distance(*point)
        plot_y.append(dist)

        print "distance: ", dist
        print "scaling: ", scaling
        continue
        print "derivatives: ", dnorm
        print "point: ", point
        print 

    plt.plot(range(len(plot_y)), plot_y, 'b-')
    plt.yscale('log')
    plt.show()

if __name__ == '__main__':
    main(5)
