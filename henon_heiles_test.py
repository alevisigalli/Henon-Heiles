import numpy as np
import io
import sys
import matplotlib
import unittest
from unittest.mock import patch

from henon_heiles import main
from henon_heiles import henon_heiles as hh
import integration_methods as im
from var import equations_motion

matplotlib.use('Agg')
    
def run_henon_heiles(args):
    """
    Run the Henon-Heiles integration and capture the output.

    This function sets up the necessary environment to run the main Henon-Heiles integration script with specified arguments.
    It captures the printed output for testing.

    Args:
        args (list): A list of command-line arguments to be passed to the main script.

    Returns:
            str: The captured output from running the main script with the specified arguments.
    """
    # Redirect stdout to capture printed messages
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Add the current directory to the module search path
    sys.path.append("~/Desktop/Henon-Heiles")

    # Run the script with arguments
    with patch.object(sys, 'argv', ['python3 henon_heiles.py'] + args):
        main()

    # Reset redirect
    sys.stdout = sys.__stdout__
    sys.path.remove("~/Desktop/Henon-Heiles")

    # Capture printed messages
    output = captured_output.getvalue()
    return output
    
class TestHenonHeiles(unittest.TestCase):
    """
    Test cases for the Henon-Heiles system integration.
    """

    def test_outer_rk4(self):
        """
        Test the integration using Runge-Kutta 4 for the "outside separatrix" trajectory.
        """
        args = ["--outer", "--rk4"]
        output = run_henon_heiles(args)
        self.assertNotIn("usage:", output)
        self.assertIn("Simulation of trajectory: outside separatrix",output)
        self.assertIn("Integrate equations of motion using Runge-Kutta 4", output)

    def test_torus_leapfrog(self):
        """
        Test the integration using LeapFrog for the "distorted torus" trajectory.
        """
        args = ["--torus", "--leapfrog"]
        output = run_henon_heiles(args)
        self.assertNotIn("usage:", output)
        self.assertIn("Simulation of trajectory: distorted torus", output)
        self.assertIn("Integrate equations of motion using Leap-Frog", output)

    def test_hyperbolic_euler(self):
        """
        Test the integration using Euler for the "hyperbolic points (separatrices)" trajectory.
        """
        args = ["--hyperbolic", "--euler"]
        output = run_henon_heiles(args)
        self.assertNotIn("usage:", output)
        self.assertIn("Simulation of trajectory: separatrices", output)
        self.assertIn("Integrate equations of motion using Euler", output)

class TestIntegrationMethods(unittest.TestCase):
    def setUp(self):
        self.y0 = 1.0
        self.t = 0.0
        self.dt = 0.001
        
    def test_integration_methods(self):
        """
        Test various integration methods with constant, linear and quadratic function.
        """
        integration_methods = [im.runge_kutta2, im.runge_kutta4, im.euler]

        for method in integration_methods:
            # Test constant function
            y_next = method(self.constant_function, self.t, self.y0, self.dt)
            self.assertAlmostEqual(y_next, self.y0, places=5)

            # Test linear function
            y_next = method(self.linear_function, self.t, self.y0, self.dt)
            expected_result = self.y0 + 0.5 * self.dt * self.linear_function(self.t, self.y0)
            self.assertAlmostEqual(y_next, expected_result, places=5)

            # Test quadratic function
            y_next = method(self.quadratic_function, self.t, self.y0, self.dt)
            expected_result = self.y0 + 0.5 * self.dt * self.quadratic_function(self.t, self.y0)
            self.assertAlmostEqual(y_next, expected_result, places=5)
    
    def test_leap_frog(self):
        """
        Test leap frog with constant and linear function.
        """
        # Test constant function
        self.y_prev = self.y0
        y_next = im.leap_frog(self.constant_function, self.t, self.y0, self.y_prev, self.dt)
        self.assertAlmostEqual(y_next, self.y0, places=5)

        # Test linear function
        self.y_prev = self.y0 ** 2
        y_next = im.leap_frog(self.linear_function, self.t, self.y0, self.y_prev, self.dt)
        expected_result = self.y0 + 0.5 * self.dt * self.linear_function(self.t, self.y0)
        self.assertAlmostEqual(y_next, expected_result, places=5)

    def constant_function(self, t, y):
        """
        Define a constant function for testing.

        Parameters:
            t (float): Current time.
            y (float): Current state.

        Returns:
            float: Constant value of 0.0.
        """
        return 0.0

    def linear_function(self, t, y):
        """
        Define a linear function for testing.

        Parameters:
            t (float): Current time.
            y (float): Current state.

        Returns:
            float: 2.0 * t.
        """
        return 2.0 * t

    def quadratic_function(self, t, y):
        """
        Define a quadratic function for testing.

        Parameters:
            t (float): Current time.
            y (float): Current state.

        Returns:
            float: t^2.
        """
        return t ** 2
    
class TestSymplecticity(unittest.TestCase):
    def setUp(self):
        # Common initial conditions for testing
        self.y0 = [0.0, -0.1475, 0.3101, 0.0]
        self.t = 0.0
        self.t_values = np.linspace(0, 10, 10001)
        self.dt = self.t_values[1] - self.t_values[0]
        
        self.t_values_half = np.linspace(0, 10, 5001)
        self.dt_half = self.t_values_half[1] - self.t_values_half[0]
        
        self.t_values_double = np.linspace(0, 20, 20001)
        self.dt_double = self.t_values_double[1] - self.t_values_double[0]
        
    def test_energy_range(self):
        """
        Test if the energy of the Henon-Heiles system stays within a certain range during integration.
        """
        # Integrate using your chosen method (e.g., Runge-Kutta 4)
        result = hh(im.runge_kutta4, equations_motion, self.y0, self.t_values, self.dt)
        x = result[:,0]
        y = result[:,1]
        px = result[:,2]
        py = result[:,3]

        # Calculate total energy
        H = (px**2) / 2 + (py**2) / 2 + (x**2) / 2 + (y**2) / 2 + x**2 * y - (1/3) * y**3

        # Check if the energy is within the desired range
        self.assertTrue((H >= 0).all() and (H <= 1/6).all())
        
    def test_leap_frog_symplecticity(self):
        # Calculate the initial energy of the system
        initial_energy = (self.y0[2]**2) / 2 + (self.y0[3]**2) / 2 + (self.y0[0]**2) / 2 + (self.y0[1]**2) / 2 + self.y0[0]**2 * self.y0[1] - (1/3) * self.y0[1]**3

        # Perform Leap-Frog integration
        result = hh(im.leap_frog, equations_motion, self.y0, self.t_values, self.dt)
        x = result[:,0]
        y = result[:,1]
        px = result[:,2]
        py = result[:,3]

        # Calculate the energy at each step and compare to the initial energy
        energy = (px**2) / 2 + (py**2) / 2 + (x**2) / 2 + (y**2) / 2 + x**2 * y - (1/3) * y**3
        self.assertAlmostEqual(initial_energy, energy[-1], places=8)
        
    def test_double_time_duration(self):
        """
        Test the integration using double time duration.

        This test method checks the behavior of the Leap-Frog integration method by using a time duration that is twice the
        original duration. It verifies that the energy of the Henon-Heiles system remains consistent throughout the extended
        simulation.

        The test checks if the total energy of the system at the end of the simulation is consistent with the initial energy,
        ensuring that the integration method maintains energy conservation over the extended time duration.

        The Henon-Heiles system is integrated using the Leap-Frog method with the provided initial conditions and time duration
        parameters.

        This test is useful to verify that the integration method remains accurate and energy-preserving over longer
        simulation periods.

        Returns:
            None
        """
        
        # Calculate the initial energy of the system
        initial_energy = (self.y0[2]**2) / 2 + (self.y0[3]**2) / 2 + (self.y0[0]**2) / 2 + (self.y0[1]**2) / 2 + self.y0[0]**2 * self.y0[1] - (1/3) * self.y0[1]**3

        # Perform Leap-Frog integration
        result = hh(im.leap_frog, equations_motion, self.y0, self.t_values_double, self.dt_double)
        x = result[:,0]
        y = result[:,1]
        px = result[:,2]
        py = result[:,3]

        # Calculate the energy at each step and compare to the initial energy
        energy = (px**2) / 2 + (py**2) / 2 + (x**2) / 2 + (y**2) / 2 + x**2 * y - (1/3) * y**3
        self.assertAlmostEqual(initial_energy, energy[-1], places=7)
        
    def test_double_step_size(self):
        """
        Test the integration using double step size.

        This test method checks the behavior of the Leap-Frog integration method by using a step size that is half of the
        original step size. It verifies that the energy of the Henon-Heiles system remains consistent throughout the simulation.

        The test checks if the total energy of the system at the end of the simulation is consistent with the initial energy,
        ensuring that the integration method maintains energy conservation over the extended step size.

        The Henon-Heiles system is integrated using the Leap-Frog method with the provided initial conditions and step size
        parameters.

        This test is useful to verify that the integration method remains accurate and energy-preserving when the step size is
        adjusted.

        Returns:
            None
        """
        # Calculate the initial energy of the system
        initial_energy = (self.y0[2]**2) / 2 + (self.y0[3]**2) / 2 + (self.y0[0]**2) / 2 + (self.y0[1]**2) / 2 + self.y0[0]**2 * self.y0[1] - (1/3) * self.y0[1]**3

        # Perform Leap-Frog integration
        result = hh(im.leap_frog, equations_motion, self.y0, self.t_values_half, self.dt_half)
        x = result[:,0]
        y = result[:,1]
        px = result[:,2]
        py = result[:,3]

        # Calculate the energy at each step and compare to the initial energy
        energy = (px**2) / 2 + (py**2) / 2 + (x**2) / 2 + (y**2) / 2 + x**2 * y - (1/3) * y**3
        self.assertAlmostEqual(initial_energy, energy[-1], places=7)

if __name__ == '__main__':
    unittest.main()
