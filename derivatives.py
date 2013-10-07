from polinomio import Polinomio

def add(v, w):
    return [vi + wi for vi, wi in zip(v, w)] 

def derivatives(function, point, npar):
    """
    Calculates function's derivatives in the given point;
    the function can have as many parameters as you want.
    
    function must accept -npar- parameters and return a number.
    """
    delta = 0.001
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
    for i in range(npar + 1):
        w = [0]*i + [delta] + [0]*(npar - i)
        derivatives.append((function(*add(point, w)) - fp) / delta)

    return derivatives

if __name__ == '__main__':
    f = lambda x, y: x**2 + 2*y

    print "f(x, y) = x**2 + 2y"
    print "derivatives in (2, 2) should be (4, 2)"
    print 
    print "derivatives: ", derivatives(f, [2,2], 1)
