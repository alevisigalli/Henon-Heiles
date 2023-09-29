import numpy as np

def equations_motion(t, y):
    """
    Compute the derivatives of the Henon-Heiles system.

    Parameters:
        t (float): Current time.
        y (numpy.ndarray): Array containing the system variables [X, Y, px, py].

    Returns:
        numpy.ndarray: Array containing the derivatives [dX/dt, dY/dt, dpx/dt, dpy/dt].
    """
    X, Y, px, py = y

    # Define the differential equations
    dX_dt = px
    dY_dt = py
    dpx_dt = -X * (1 + 2 * Y)
    dpy_dt = Y * (Y - 1) - X**2

    return np.array([dX_dt, dY_dt, dpx_dt, dpy_dt])