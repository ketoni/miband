import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata, zdata = [], [], []
lines, = plt.plot([], [])

def init():
    ax.set_xlim(0, 10*2*np.pi)
    ax.set_ylim(-1, 1)
    return lines,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    lines.set_data(xdata, ydata)
    return lines,

ani = FuncAnimation(
        fig,
        update,
        frames=np.linspace(0, 20*np.pi, 128),
        init_func=init,
        blit=True,
        interval=50)
plt.show()
