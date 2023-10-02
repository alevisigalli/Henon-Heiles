import unittest
from unittest.mock import patch
from . import henon_heiles  # Import your main script
from . import integration_methods  # Import your submodules
from . import var
from . import poincare_maps
import sys
import numpy as np
import io

def run_henon_heiles(args):
    # Redirect stdout to capture printed messages
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Add the current directory to the module search path
    sys.path.append("/home/avisigalli@iit.local/Desktop/Data/Henon-Heiles")

    # Run the script with arguments
    with patch.object(sys, 'argv', ['python','henon_heiles.py'] + args):
        import henon_heiles

    # Reset redirect
    sys.stdout = sys.__stdout__
    sys.path.remove("/home/avisigalli@iit.local/Desktop/Data/Henon-Heiles")

    # Capture printed messages
    output = captured_output.getvalue()
    return output

class TestHenonHeiles(unittest.TestCase):

    def test_energy_range(self):
        # Define initial conditions
        initial_conditions = [0.0, -0.1475, 0.3101, 0.0]
        # Define time values
        t_values = np.linspace(0, 200, 20001)
        # Choose a suitable step size
        h = t_values[1] - t_values[0]

        # Integrate using your chosen method (e.g., Runge-Kutta 4)
        result = henon_heiles(runge_kutta4, var, initial_conditions, t_values, h)
        x = result[:,0]
        y = result[:,1]
        px = result[:,2]
        py = result[:,3]

        # Calculate total energy
        H = (px**2) / 2 + (py**2) / 2 + (x**2) / 2 + (y**2) / 2 + x**2 * y - (1/3) * y**3

        # Check if the energy is within the desired range
        self.assertTrue((H >= 0).all() and (H <= 1/6).all())

    def test_invalid_arguments(self):
        args = []
        output = run_henon_heiles(args)
        self.assertIn("usage:", output)
        self.assertIn("Error: You need to use exactly one of these three arguments", output)
        self.assertIn("Error: You need to use exactly one of these four arguments", output)

    def test_outer_rk4(self):
        args = ["--outer", "--rk4"]
        output = run_henon_heiles(args)
        self.assertNotIn("usage:", output)
        self.assertIn("Simulation of trajectory: outside separatrix", output)
        self.assertIn("Integrate equations of motion using Runge-Kutta 4", output)

    def test_torus_leapfrog(self):
        args = ["--torus", "--leapfrog"]
        output = run_henon_heiles(args)
        self.assertNotIn("usage:", output)
        self.assertIn("Simulation of trajectory: distorted torus", output)
        self.assertIn("Integrate equations of motion using LeapFrog", output)

    def test_hyperbolic_euler(self):
        args = ["--hyperbolic", "--euler"]
        output = run_henon_heiles(args)
        self.assertNotIn("usage:", output)
        self.assertIn("Simulation of trajectory: hyperbolic points (separatrices)", output)
        self.assertIn("Integrate equations of motion using Euler", output)

if __name__ == '__main__':
    unittest.main()
