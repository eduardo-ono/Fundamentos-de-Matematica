import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [4, 3]


def plotFunction(x_coords, y_coords, fig, ax):
    plt.axhline(y=0.0, color='brown', linestyle='-', linewidth=1)
    ax.plot(x_coords, y_coords)
    plt.show()

# MARK: plotCircle()
def plotCircle(center, radius, fig, ax):
    angles = np.linspace(0, np.pi * 4, round(360 * radius))
    x_coords = np.sin(angles) * radius
    y_coords = np.cos(angles) * radius

    ax.set_aspect('equal')
    ax.plot(x_coords, y_coords)
    plt.show()
