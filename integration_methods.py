import numpy as np

def runge_kutta2(f, t, y, dt):
    """
    Runge-Kutta 2nd order integration method for solving first-order ODEs.

    Parameters:
        f  (function): The function that defines the ODE dy/dt = f(t, y).
        t  (float): Current time.
        y  (array-like): Current state vector.
        dt (float): Step size.

    Returns:
        array-like: New state vector after one time step.
    """

    # Implement the Runge-Kutta integration method
    k1 = np.array(f(t,y))
    k2 = np.array(f(t+dt,y+dt*k1))

    # Return the results
    return y + 0.5 * dt * (k1+k2)

def runge_kutta4(f, t, y, dt):
    """
    Runge-Kutta 4th order integration method for solving first-order ODEs.

    Parameters:
        f  (function): The function that defines the ODE dy/dt = f(t, y).
        t  (float): Current time.
        y  (array-like): Current state vector.
        dt (float): Step size.

    Returns:
        array-like: New state vector after one time step.
    """

    # Implement the Runge-Kutta integration method
    k1 = np.array(f(t,y))
    k2 = np.array(f(t+dt/2,y+dt/2*k1))
    k3 = np.array(f(t+dt/2,y+dt/2*k2))
    k4 = np.array(f(t+dt,y+dt*k3))

    # Return the results
    return y + dt/6 * (k1+2*k2+2*k3+k4)

def leap_frog(f, t, y, y_prev, dt):
    """
    Leap-Frog integration method for solving first-order ODEs.

    Parameters:
        f      (function): The function that defines the ODE dy/dt = f(t, y).
        t      (float): Current time.
        y      (array-like): Current state vector.
        y_prev (array-like): Previous state vector.
        dt     (float): Step size.

    Returns:
        array-like: New state vector after one time step.
    """
    # Implement the Leap-Frog integration method
    k = np.array(f(t, y))

    y_new = y_prev + 2*dt*k


    return y_new

def euler(f, t, y, dt):
    """
    Euler integration method for solving first-order ODEs.

    Parameters:
        f  (function): The function that defines the ODE dy/dt = f(t, y).
        t  (float): Current time.
        y  (array-like): Current state vector.
        dt (float): Step size.

    Returns:
        array-like: New state vector after one time step.
    """
    # Implement the Euler integration method
    k = np.array(f(t,y))
    y_next = y + dt*k

    # Return the results
    return y_next

