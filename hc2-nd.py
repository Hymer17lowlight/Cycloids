# Hypocycloid 2-nd ord
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pylab
from matplotlib.cm import *
from mpl_toolkits.mplot3d import Axes3D


def NSD(a, b): # greatest common factor
    while a != 0 and b != 0:
        if b > a:
            a, b = b, a
        a = a % b
    return float(b)


def NSK(a, b): # Least Common Multiple
    return float(a*b/NSD(a, b))


def plot2d(R, r1, r2, w1, w2, h, a, b, e): # plot of hypocycloid of second order
    t = np.arange(a, b, e)
    k1 = R/r1
    k2 = r1/r2
    x = (R-r1)*np.cos(w1*t)+(r1-r2)*np.cos(((1-k1)*w1+w2)*t)+h*np.cos(((1-k1)*w1+(1-k2)*w2)*t)
    y = (R-r1)*np.sin(w1*t)+(r1-r2)*np.sin(((1-k1)*w1+w2)*t)+h*np.sin(((1-k1)*w1+(1-k2)*w2)*t)
    T = 'T = {}pi'.format(b/3.1415)
    n = 'n = {}'.format(b/6.283)
    print(T)
    print(n)
    plt.plot(x, y)
    plt.show()


def plot3dtriv(R, r1, r2, w1, w2, h, a, b, e):        # plotting the cylindrical surface with a hypocycloid of second order at the base
    t = np.arange(a, b, e)
    k1 = R / r1
    k2 = r1 / r2
    x = np.arange(-h, h, e)
    x, t = np.meshgrid(x, t)
    ygrid = (R - r1)*np.cos(w1*t) + (r1 - r2)*np.cos(((1-k1)*w1+w2)*t) + r2*np.cos(((1-k1)*w1 + (1-k2)*w2)*t)
    zgrid = (R - r1)*np.sin(w1*t) + (r1 - r2)*np.sin(((1-k1)*w1+w2)*t) + r2*np.sin(((1-k1)*w1 + (1-k2)*w2)*t)
    y, z = ygrid, zgrid

    fig = pylab.figure(1)
    axes = Axes3D(fig)

    fig = axes.plot_surface(y, z, x, cmap='coolwarm')

    pylab.show(fig)


def plot3duntr(R, r1, r2, w1, w2, h, a, b, e):       # a bit more interesting
    t = np.arange(a, b, e)
    k1 = R / r1
    k2 = r1 / r2
    x = np.arange(-h, h, e)  
    x, t = np.meshgrid(x, t)
    ygrid = (R - r1)*np.cos(w1*t) + (r1 - r2)*np.cos(((1-k1)*w1+w2)*t) + r2*(x/h)*np.cos(((1-k1)*w1 + (1-k2)*w2)*t)
    zgrid = (R - r1)*np.sin(w1*t) + (r1 - r2)*np.sin(((1-k1)*w1+w2)*t) + r2*(x/h)*np.sin(((1-k1)*w1 + (1-k2)*w2)*t)
    y, z = ygrid, zgrid

    fig = pylab.figure(1)
    axes = Axes3D(fig)

    fig = axes.plot_surface(y, z, x, cmap='coolwarm')

    pylab.show(fig)


# function for testing
def maindef():
    a = 0
    e = 0.01
    while True:
        try:
            j = float(input('Please, choose: \n 2d - 2 \n 3d trivial - 3 \n 3d half-trivial - 3.1 \n Stop it! - 0 \n '))
            print('R, r1 and r2 must be integer')
            if j == 3:
                R = float(input('R = '))
                r1 = float(input('r1 = '))
                r2 = float(input('r2 = '))
                b = 6.283 * NSK(R, r1) * NSK(r1, r2) / (R * r1)
                w1 = float(input('w1 = '))
                w2 = float(input('w2 = '))
                h = float(input('h = '))
                plot3dtriv(R, r1, r2, w1, w2, h, a, b, e)
            elif j == 3.1:
                R = float(input('R = '))
                r1 = float(input('r1 = '))
                r2 = float(input('r2 = '))
                b = 6.283 * NSK(R, r1) * NSK(r1, r2) / (R * r1)
                w1 = float(input('w1 = '))
                w2 = float(input('w2 = '))
                h = float(input('h = '))
                plot3duntr(R, r1, r2, w1, w2, h, a, b, e)
            elif j == 2:
                R = float(input('R = '))
                r1 = float(input('r1 = '))
                r2 = float(input('r2 = '))
                b = 6.283 * NSK(R, r1) * NSK(r1, r2) / (R * r1)
                w1 = float(input('w1 = '))
                w2 = float(input('w2 = '))
                h = float(input('h = '))
                plot2d(R, r1, r2, w1, w2, h, a, b, e)
            elif j == 0:
                break
            else:
                print('err, try again')
        except ValueError:
            print('err, try again')


if __name__ == '__main__':
    maindef()