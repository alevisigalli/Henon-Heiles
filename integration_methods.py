import numpy as np

def runge_kutta2(f, t, y, h):
    # Implement the Runge-Kutta integration method
    k1 = np.array(f(t,y))
    k2 = np.array(f(t+h,y+h*k1))

    # Return the results
    return y + 0.5 * h * (k1+k2)

def runge_kutta4(f, t, y, h):
    # Implement the Runge-Kutta integration method
    k1 = np.array(f(t,y))
    k2 = np.array(f(t+h/2,y+h/2*k1))
    k3 = np.array(f(t+h/2,y+h/2*k2))
    k4 = np.array(f(t+h,y+h*k3))

    # Return the results
    return y + h/6 * (k1+2*k2+2*k3+k4)

def leap_frog(f, t, y, h):
    # Implement the Leap-Frog integration method
    ## Half-step update for positions
    y[:2] += 0.5 * h * y[2:4] 

    ## Full-step update for momenta
    k = np.array(f(t,y))
    y[2:4] += h*k[2:4]

    ## Half-step update for positions
    y[:2] += 0.5 * h * y[2:4]

    # Return the results
    return y

def euler(f, t, y, h):
    # Implement the Euler integration method
    k = np.array(f(t,y))
    y_next = y + h*k

    # Return the results
    return y_next

