#!/usr/bin/python

import random
import matplotlib.pyplot as plt

class RandomLine:
    def __init__(self, errmax, num):
        self.a = random.triangular(-5, 5)
        self.b = random.triangular(-5, 5)

        self.points = []
        e = errmax / 2.0
        for i in range(num):
            x = random.triangular(-10, 10)
            y = self.a * x + self.b + random.triangular(-e, e)

            self.points.append((x, y))

    def save(self, path):
        with open(path, "w") as streamOut:
            streamOut.write("x;y\n")
            streamOut.writelines(["{};{}\n".format(*p)
                for p in self.points])
   
def distance(line, a, b):
    return sum([ (p[1] - (p[0] * a + b))**2 for p in line.points ])

def main():
    delta = 0.0001
    alpha = 0.0001

    a = 0
    b = 0
    r = RandomLine(5, 100)

    tries = []
    while len(tries) < 5 or abs(tries[-1][1] - tries[-2][1]) > 0.01:
        dist = distance(r,a,b)

        g_a = (distance(r, a+delta, b) - distance(r, a, b)) / delta
        g_b = (distance(r, a, b+delta) - distance(r, a, b)) / delta

        a -= g_a * alpha
        b -= g_b * alpha

        print dist, g_a, g_b

        tries.append((len(tries), dist, a, b, g_a, g_b))

    r.save("data.csv")
    with open("tries.csv", "w") as streamOut:
        streamOut.write("i;e;a;b;g_a;g_b\n")
        streamOut.writelines([
            "{};{};{};{};{};{}\n".format(*t)
            for t in tries ])

    plot_graph(tries, r)

def plot_graph(tries, line): 
    s = (tries[-1][2], tries[-1][3])
    plt.figure(1)
    plt.plot([-10,10],[-10*line.a+line.b,10*line.a+line.b],'-g',linewidth=2.0)
    plt.plot([-10,10],[-10*s[0]+s[1],10*s[0]+s[1]],'--b',linewidth=2.0)
    plt.plot([p[0] for p in line.points], [p[1] for p in line.points], 'ro')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Random generated data with real and approximated line")

    plt.figure(2)
    plt.subplot(2, 1, 1)
    plt.plot([t[0] for t in tries], [t[1] for t in tries])
    plt.title("Approximation error")

    plt.subplot(2, 1, 2)
    plt.plot([t[0] for t in tries], [t[2] for t in tries], '-r')
    plt.plot([t[0] for t in tries], [t[3] for t in tries], '--g')
    plt.title("Line coefficients evolution")

    plt.show()

if __name__ == '__main__':
    main()
