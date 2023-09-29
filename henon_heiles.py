import argparse
import numpy as np
import matplotlib.pyplot as plt
from integration_methods import runge_kutta2, runge_kutta4, leap_frog, euler
from scipy.integrate import solve_ivp

# Define the Henon-Heiles system differential equations
def var(t, y):
    X = y[0]
    Y = y[1]
    px = y[2]
    py = y[3]

    dxdt = px
    dydt = py
    dpxdt = -X * (1 + 2 * Y)
    dpydt = Y * (Y - 1) - X**2

    return [dxdt, dydt, dpxdt, dpydt]

def henon_heiles(integration_method,f, y0, t_values, h):
    num_steps = len(t_values)
    y_values = np.zeros((num_steps, len(y0)))
    y_values[0] = y0
    
    for i in range(1, num_steps):
        y_values[i] = integration_method(f, t_values[i-1], y_values[i-1], h)
    
    return y_values

# Define initial conditions
initial_conditions = [0.0, -0.1475, 0.3101, 0.0]
# Define time values
t_values = np.linspace(0, 200, 20001)  # Adjust the time span and step size as needed
# Choose a suitable step size
h = t_values[1] - t_values[0]

def plot_hyperbolic(X, Y, px, py):
    # Plot hyperbolic points
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(X, Y, '.')
    plt.title('Hyperbolic Points: Separatrices')

    Y5, PY5 = [], []
    for i in range(len(X)):
        if -0.05 < X[i] < 0.05:
            Y5.append(Y[i])
            PY5.append(py[i])

    plt.subplot(1, 2, 2)
    plt.plot(Y5, PY5, '.')
    plt.title('Poincaré Map (Hyperbolic Points: Separatrices)')

    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Henon-Heiles System Integration")
    parser.add_argument("--rk2", action="store_true", help="Integrate equations of motion using Runge-Kutta 2")
    parser.add_argument("--rk4", action="store_true", help="Integrate equations of motion using Runge-Kutta 4")
    parser.add_argument("--leapfrog", action="store_true", help="Integrate equations of motion using leapfrog")
    parser.add_argument("--euler", action="store_true", help="Integrate equations of motion using Euler")

    args = parser.parse_args()

    if args.rk2:
        result = henon_heiles(runge_kutta2,var,initial_conditions, t_values, h)
        plot_hyperbolic(X=result[:,0], Y=result[:,1], px=result[:,2], py=result[:,3])

    if args.rk4:
        result = henon_heiles(runge_kutta4,var,initial_conditions, t_values, h)
        plot_hyperbolic(X=result[:,0], Y=result[:,1], px=result[:,2], py=result[:,3])
    
    if args.leapfrog:
        result = henon_heiles(leap_frog,var,initial_conditions, t_values, h)
        plot_hyperbolic(X=result[:,0], Y=result[:,1], px=result[:,2], py=result[:,3])
    
    if args.euler:
        result = henon_heiles(euler,var,initial_conditions, t_values, h)
        plot_hyperbolic(X=result[:,0], Y=result[:,1], px=result[:,2], py=result[:,3])



if __name__ == "__main__":
    main()
