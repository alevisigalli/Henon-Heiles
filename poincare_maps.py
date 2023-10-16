import numpy as np
import matplotlib.pyplot as plt

def plot_henon_heiles(t, x, y, px, py, color, title,axs):
    """
    Plot the trajectories and energy evolution of the Henon-Heiles system.

    Parameters:
    - t (array): Time values.
    - x (array): x-coordinate values.
    - y (array): y-coordinate values.
    - px (array): Momentum in the x-direction.
    - py (array): Momentum in the y-direction.
    - color (str): Color for scatter plots and energy curve.
    - title (str): Title for the second subplot.

    Returns:
    None
    """
    ax1,ax2,ax3=axs

    # Plot trajectories in the x-y plane
    ax1.scatter(x, y, s=1, c=color)
    ax1.set_xlabel('x', fontsize=12)
    ax1.set_ylabel('y', fontsize=12)

    # Create a Poincaré map by selecting points within a range of x values
    selected_y = []
    selected_py = []
    for i in range(len(x)):
        if -0.05 < x[i] < 0.05:
            selected_y.append(y[i])
            selected_py.append(py[i])

    ax2.scatter(selected_y, selected_py, s=1, c=color,alpha=0.7)
    ax2.set_xlabel('y', fontsize=12)
    ax2.set_ylabel('py', fontsize=12)
    ax2.set_title(f'{title}', fontsize=16)

    # Plot energy evolution over time
    hamiltonian = (px**2) / 2 + (py**2) / 2 + (x**2) / 2 + (y**2) / 2 + x**2 * y - (1/3) * y**3
    normalized_hamiltonian = hamiltonian / hamiltonian[0]

    ax3.plot(t, normalized_hamiltonian, color=color)
    ax3.set_xlabel('Time', fontsize=12)
    ax3.set_ylabel('Normalized Energy', fontsize=12)
    
    plt.tight_layout()
