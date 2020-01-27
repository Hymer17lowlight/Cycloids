import numpy as np
import random
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(-17, 17), ylim=(-17, 17))
line, = ax.plot([], [], lw=1.5)

def NSD(a, b):
    while a != 0 and b != 0:
        if b > a:
            a, b = b, a
        a = a % b
    return float(b)


def NSK(a, b):
    return float(a*b/NSD(a, b))

def plot2d(t, R, r1, r2, w1, w2, h):
    k1 = R/r1
    k2 = r1/r2
    b = 6.283 * NSK(R, r1) * NSK(r1, r2) / (R * r1)
    x = (R-r1)*np.cos(w1*t)+(r1-r2)*np.cos(((1-k1)*w1+w2)*t)+h*np.cos(((1-k1)*w1+(1-k2)*w2)*t)
    y = (R-r1)*np.sin(w1*t)+(r1-r2)*np.sin(((1-k1)*w1+w2)*t)+h*np.sin(((1-k1)*w1+(1-k2)*w2)*t)
    T = 'T = {}pi'.format(b/3.1415)
    n = 'n = {}'.format(b/6.283)
    print(T)
    print(n)
    return [x, y]


def init():
    line.set_data([], [])
    return line,


def animate(i):
    R  = 9
    r1 = 3
    r2 = 2
    w1 = i//25+1
    w2 = i//16+1
    b = 6.284 * NSK(9, 3) * NSK(3, 2) / (9 * 3)
    t = np.arange(0, b, 0.01)
    print(i)
    res = plot2d(t, R, r1, r2, w1, w2, 2*r2*(i % 100)/100)
    line.set_data(res[0], res[1])
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=400, interval=20, blit=True)

#anim.save('try_to_save.mp4', fps=24, extra_args=['-vcodec', 'libx264'])

plt.show()