import random
import matplotlib.pyplot as plt
from math import sqrt

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

    def trend_line(self):
        sum_x = sum([p[0] for p in self.points])
        sum_y = sum([p[1] for p in self.points])
        
        numerator = sum([p[0]*p[1] for p in self.points]) - (sum_x * sum_y) / len(self.points)
        denominator = sum([p[0]**2 for p in self.points]) - sum_x**2 / len(self.points)
         
        a = numerator / denominator
        b = sum_y / len(self.points) - a * sum_x / len(self.points)

        return a, b

    def save(self, path):
        with open(path, "w") as streamOut:
            streamOut.write("x;y\n")
            streamOut.writelines(["{};{}\n".format(*p)
                for p in self.points])
   
def distance(line, a, b):
    return sum([ (p[1] - (p[0] * a + b))**2 for p in line.points ])

def correlation_coefficient(points):
    denominator = sqrt(
        sum([p[0]**2 for p in points]) *
        sum([p[1]**2 for p in points]))

    return sum([p[0] * p[1] for p in points]) / denominator    

def main():
    delta = 0.0001  # difference quotient approximation
    alpha = 0.0001  # step size

    a = 0
    b = 0
    r = RandomLine(5, 100)

    trend = r.trend_line()
    print "Correlation coefficient is: {}".format(correlation_coefficient(r.points))
    print "Trend line using formula: y = {} * x + {}".format(trend[0], trend[1])

    tries = []
    while len(tries) < 5 or abs(tries[-1][1] - tries[-2][1]) > 0.01:
        dist = distance(r,a,b)

        g_a = (distance(r, a+delta, b) - distance(r, a, b)) / delta
        g_b = (distance(r, a, b+delta) - distance(r, a, b)) / delta

        a -= g_a * alpha
        b -= g_b * alpha

        tries.append((len(tries), dist, a, b, g_a, g_b))

    print "Calculated trend line is: y = {} * x + {}".format(a, b)

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

    plt.axhline(y=line.a, color='r', linestyle='dashed')
    plt.plot([t[0] for t in tries], [t[2] for t in tries], '-r')

    plt.axhline(y=line.b, color='g', linestyle='dashed')
    plt.plot([t[0] for t in tries], [t[3] for t in tries], '-g')
    plt.title("Line coefficients evolution")

    plt.show()

if __name__ == '__main__':
    main()
