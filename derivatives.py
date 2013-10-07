def add_vect(v, w):
    return [vi + wi for vi, wi in zip(v, w)] 

def derivatives(function, point, npar):
    """
    Calculates function's derivatives in the given point;
    the function can have as many parameters as needed.
    
    function must accept -npar- parameters and return a number.
    """
    delta = 0.0001
    fp = function(*point)

    derivatives = []

    # calculate each derivative by slightly moving in that
    # direction (w) and calculating the difference quotient.
    #
    # w will assume the following parameters:
    # [delta, 0, ..., 0]
    # [0, delta, ..., 0]
    # ...
    # [0, 0, ..., delta]
    for i in range(npar):
        w = [0]*i + [delta] + [0]*(npar - i - 1)
        derivatives.append((function(*add_vect(point, w)) - fp) / delta)

    return derivatives

if __name__ == '__main__':
    f = lambda x, y, z: x**2 + 2*y + 2*x*z

    test = [2,2,2]

    print "f(x, y) = x^2 + 2y + 2xz"
    print "    df/dx = 2x + 2z"
    print "    df/dy = 2"
    print "    df/dz = 2x"
    print
    print "derivatives in (2, 2, 2) should be (8, 2, 4)"
    print "and actually is ", derivatives(f, test, len(test))
