import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1,3,figsize=(15, 6),sharex=False,sharey=False)

def plotting_module(t,x,y,px,py,color,title):
    axs[0].scatter(x,y,s=5,c=color)
    axs[0].set_xlabel('x', fontsize=12)
    axs[0].set_ylabel('y', fontsize=12)

    Y = []
    PY = []
    for i in range(len(x)):
        if -0.05 < x[i] < 0.05:
            Y.append(y[i])
            PY.append(py[i])

    axs[1].scatter(Y,PY,s=5,c=color)
    axs[1].set_xlabel('y', fontsize=12)
    axs[1].set_ylabel('py', fontsize=12)
    axs[1].set_title(f'{title}', fontsize=16)

    H = (px**2) / 2 + (py**2) / 2 + (x**2) / 2 + (y**2) / 2 + x**2 * y - (1/3) * y**3
    Hn = H / H[0]

    axs[2].plot(t, Hn, color=color)
    axs[2].set_xlabel('Time', fontsize=12)
    axs[2].set_ylabel('Energy', fontsize=12)
    plt.show()