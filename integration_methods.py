import numpy as np

def henon_heiles(integration_method,f, y0, t_values, dt):
    '''
    The henon_heiles function is designed to perform numerical integration of a dynamical system using various integration methods. 
    In particular, it can be used to simulate the Henon-Heiles system, a simple Hamiltonian system used in celestial mechanics and quantum mechanics. 
    
    Parameters:
        integration_method (string): this parameters allow you to choose between four integration methods: euler, runge_kutta4, runge_kutta2, leap-frog.
        f  (function): The function that defines the ODE dy/dt = f(t, y).
        y0  (array): Initial conditions for the state vector (x, y, px and py).
        t  (array): Simulation time.
        dt (float): Step size.

    Returns:
        array: State vector after the whole simulation time.
    
    '''
    num_steps = len(t_values)
    y_values = np.zeros((num_steps, len(y0)))
    y_values[0] = y0
    
    if integration_method == leap_frog:
        y_values[1] = y_values[0] + dt*np.array(f(t_values[0], y_values[0]))
        for i in range(2, num_steps):
            y_values[i] = leap_frog(f, t_values[i-1], y_values[i-1], y_values[i-2], dt)
    else:
        for i in range(1, num_steps):
            y_values[i] = integration_method(f, t_values[i-1], y_values[i-1], dt)
    
    return y_values

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

def euler(f, t, y0, dt):
    """
    Euler integration method for solving first-order ODEs.

    Parameters:
        f  (function): The function that defines the ODE dy/dt = f(t, y).
        t  (float): Current time.
        y0 (array-like): Initial state vector.
        dt (float): Step size.

    Returns:
        array-like: New state vector after one time step.
    """
    # Implement the Euler integration method
    k = np.array(f(t, y0))
    y = y0 + dt * k

    # Return the results
    return y

