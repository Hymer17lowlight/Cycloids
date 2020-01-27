import numpy as np
import pylab
from matplotlib import pyplot as plt
from numpy import pi
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.cm import *

def plt_surf(h, r):
    u = np.arange(-2*pi, 2*pi, 0.01)
    v = np.arange(-2*pi, 2*pi, 0.01)

    u, v = np.meshgrid(u, v)
    fig = plt.figure(1)

    a1 = fig.add_subplot(2, 2, 1, projection='3d')
    a2 = fig.add_subplot(2, 2, 2, projection='3d')
    a3 = fig.add_subplot(2, 2, 3, projection='3d')
    a4 = fig.add_subplot(2, 2, 4, projection='3d')

    x = h*u
    y = r*v - r*np.sin(v-u)
    z = r - r*np.cos(v-u)

    fig = a1.plot_surface(x, y, z, cmap=coolwarm, antialiased=False)

    t = np.arange(-2*pi, 2*pi, 0.01)

    for i in range(-5, 5):
        tu = 2*pi*i/5
        x = h * tu + 0*t
        y = r * t - r * np.sin(t - tu)
        z = r - r * np.cos(t - tu)
        fig = a2.plot(x, y, z, 'red')
        fig = a3.plot(x, y, z, 'red')

    for j in range(-5, 5):
        tv = 2*pi*j/5
        x = h*t
        y = r*tv - r*np.sin(tv - t)
        z = r - r*np.cos(tv - t)
        fig = a2.plot(x, y, z, 'blue')
        fig = a4.plot(x, y, z, 'blue')

    pylab.show(fig)


plt_surf(1, 1)
