from polynomial import Polynomial
from derivatives import derivatives
import matplotlib.pyplot as plt
from math import sqrt

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
    alpha = 0.0001

    pol = Polynomial(npar)
    pol.generate_points(50, 40)

    point = [0] * npar
    for i in range(30):
        print "point: ", point

        d = normalize(derivatives(sqr_distance, point))
        point = add_vect(point, scale(d, -alpha))

        print "distance: ", sqr_distance(*point)
        print "derivatives: ", d
        print 

if __name__ == '__main__':
    main(5)
