"""
Henon-Heiles System Integration

This script performs numerical integration of the Henon-Heiles system using various integration methods
and visualizes the trajectory.

Usage:
  henon_heiles.py (--rk2 | --rk4 | --leapfrog | --euler) (--outer | --torus | --hyperbolic)

Options:
  -h, --help    Show this help message and exit.
  --rk2         Integrate equations of motion using Runge-Kutta 2.
  --rk4         Integrate equations of motion using Runge-Kutta 4.
  --leapfrog    Integrate equations of motion using LeapFrog.
  --euler       Integrate equations of motion using Euler.
  --outer       Simulation of trajectory: outside separatrix.
  --torus       Simulation of trajectory: distorted torus.
  --hyperbolic  Simulation of trajectory: hyperbolic points (separatrices).

Examples:
  python henon_heiles.py --rk4 --torus
"""

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
t_values = np.linspace(0, 200, 200001) 

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
        print("Simulation of trajectory: outside separatrix")
        
    if args.torus:
        initial_conditions = [0, -0.1475, 0.3101, 0]
        color = 'tab:orange'
        title = 'Distorted torus'
        print("Simulation of trajectory: distorted torus")
        
    if args.hyperbolic:
        initial_conditions = [0, 0.1563, 0.18876, -0.25]
        color = 'tab:green'
        title = 'Hyperbolic points: separatrices'
        print("Simulation of trajectory: separatrices")
    
    # Choose the integration algorithm
    if args.rk2:
        print("Integrate equations of motion using Runge-Kutta 2")
        result = henon_heiles(runge_kutta2,var,initial_conditions, t_values, dt)

    if args.rk4:
        print("Integrate equations of motion using Runge-Kutta 4")
        result = henon_heiles(runge_kutta4,var,initial_conditions, t_values, dt)
    
    if args.leapfrog:
        print("Integrate equations of motion using Leap-Frog")
        result = henon_heiles(leap_frog,var,initial_conditions, t_values, dt)
    
    if args.euler:
        print("Integrate equations of motion using Euler")
        result = henon_heiles(euler,var,initial_conditions, t_values,dt)  
        print(result)
    
    pm.plot_henon_heiles(t_values,x=result[:,0], y=result[:,1], px=result[:,2], py=result[:,3],color=color,title=title)


if __name__ == "__main__":
    main()
