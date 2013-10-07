from random import triangular as randrange
import matplotlib.pyplot as plt

class Polynomial:
    def __init__(self, errmax, npoints, coeff):
        self.coefficients = []
        for i in range(coeff):
            self.coefficients.append(randrange(-0.5, 0.5))

        self.points = []
        e = errmax / 2.0
        for i in range(npoints):
            x = randrange(-10, 10)

            y = self.value(x)
            y += randrange(-e, e)

            self.points.append((x, y))

    def degree(self):
        return len(self.coefficients)

    def value(self, x):
        return sum([a * x**i
            for a, i in zip(self.coefficients, range(self.degree()))])

    def plot(self):
        x = range(-10, 10)
        plt.plot(x, [self.value(p) for p in x], '-b')
        plt.plot([p[0] for p in self.points],
            [p[1] for p in self.points], 'ro')
        plt.show()

if __name__ == '__main__':
    p = Polynomial(40, 50, 4)
    p.plot()
