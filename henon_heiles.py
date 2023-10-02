import argparse
import sys
import numpy as np
from integration_methods import runge_kutta2, runge_kutta4, leap_frog, euler
from var import equations_motion as var
import poincare_maps as pm

def henon_heiles(integration_method,f, y0, t_values, dt):
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

# Define time values
t_values = np.linspace(0, 200, 20001)  # Adjust the time span and step size as needed
# Choose a suitable step size
dt = t_values[1] - t_values[0]

def main():
    parser = argparse.ArgumentParser(description="Henon-Heiles System Integration")
    
    # Create a mutually exclusive group for the integration method options
    method_group = parser.add_mutually_exclusive_group(required=True)
    method_group.add_argument("--rk2", action="store_true", help="Integrate equations of motion using Runge-Kutta 2")
    method_group.add_argument("--rk4", action="store_true", help="Integrate equations of motion using Runge-Kutta 4")
    method_group.add_argument("--leapfrog", action="store_true", help="Integrate equations of motion using LeapFrog")
    method_group.add_argument("--euler", action="store_true", help="Integrate equations of motion using Euler")


    # Create a mutually exclusive group for the initial condition options
    traj_group = parser.add_mutually_exclusive_group(required=True)
    traj_group.add_argument("--outer", action="store_true", help="Simulation of trajectory: outside separatrix")
    traj_group.add_argument("--torus", action="store_true", help="Simulation of trajectory: distorted torus")
    traj_group.add_argument("--hyperbolic", action="store_true", help="Simulation of trajectory: hyperbolic points (separatrices)")

    args = parser.parse_args()

    selected_traj_options = [args.outer, args.torus, args.hyperbolic]
    if sum(selected_traj_options) != 1:
        print("Error: You need to use exactly one of these three arguments: --outer, --torus, or --hyperbolic.")
        sys.exit(1)  # Exit with an error code
    
    selected_method_options = [args.rk2, args.rk4, args.leapfrog, args.euler]
    if sum(selected_method_options) != 1:
        print("Error: You need to use exactly one of these four arguments: --rk2, --rk4, --leapfrog, or --euler.")
        sys.exit(1)  # Exit with an error code

    # Define initial conditions
    if args.outer:
        initial_conditions = [0, 0, -0.0428, -0.3438]
        color = 'tab:blue'
        title='Outside separatrix'
    if args.torus:
        initial_conditions = [0, -0.1475, 0.3101, 0]
        color = 'tab:orange'
        title = 'Distorted torus'
    if args.hyperbolic:
        initial_conditions = [0, 0.1563, 0.18876, -0.25]
        color = 'tab:green'
        title = 'Hyperbolic points: separatrices'
    
    # Choose the integration algorithm
    if args.rk2:
        result = henon_heiles(runge_kutta2,var,initial_conditions, t_values, dt)
        pm.plot_henon_heiles(t_values,x=result[:,0], y=result[:,1], px=result[:,2],py=result[:,3],color=color,title=title)

    if args.rk4:
        result = henon_heiles(runge_kutta4,var,initial_conditions, t_values, dt)
        pm.plot_henon_heiles(t_values,x=result[:,0], y=result[:,1], px=result[:,2], py=result[:,3],color=color,title=title)
    
    if args.leapfrog:
        result = henon_heiles(leap_frog,var,initial_conditions, t_values, dt)
        pm.plot_henon_heiles(t_values,x=result[:,0], y=result[:,1], px=result[:,2], py=result[:,3],color=color,title=title)
    
    if args.euler:
        result = henon_heiles(euler,var,initial_conditions, t_values, dt)
        pm.plot_henon_heiles(t_values,x=result[:,0], y=result[:,1], px=result[:,2], py=result[:,3],color=color,title=title)


if __name__ == "__main__":
    main()
