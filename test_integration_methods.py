import numpy as np
import unittest
import integration_methods as im

class TestIntegrationMethods(unittest.TestCase):

    def test_runge_kutta2(self):
        # Define a simple test ODE: dy/dt = -y
        def test_ode(t, y):
            return -y

        # Initial conditions
        y0 = 1.0
        t = 0.0
        dt = 0.01

        # Use Runge-Kutta 2 to solve the ODE
        y_next = im.runge_kutta2(test_ode, t, y0, dt)

        # The solution for this ODE is y(t) = e^(-t)
        expected_result = np.exp(-t)
        self.assertAlmostEqual(y_next, expected_result, places=1)

    def test_runge_kutta4(self):
        # Define a simple test ODE: dy/dt = -y
        def test_ode(t, y):
            return -y

        # Initial conditions
        y0 = 1.0
        t = 0.0
        dt = 0.01

        # Use Runge-Kutta 4 to solve the ODE
        y_next = im.runge_kutta4(test_ode, t, y0, dt)

        # The solution for this ODE is y(t) = e^(-t)
        expected_result = np.exp(-t)
        self.assertAlmostEqual(y_next, expected_result, places=1)

    def test_leap_frog(self):
        # Define a simple test ODE: dy/dt = -y
        def test_ode(t, y):
            return -y

        # Initial conditions
        y = 1.0
        t = 0.0
        dt = 0.001
        y_prev = np.exp(t-dt)

        # Use LeapFrog to solve the ODE
        y_next = im.leap_frog(test_ode, t, y, y_prev,dt)

        # The solution for this ODE is y(t) = e^(-t)
        expected_result = np.exp(-t)
    
        # Check if the result is close to the analytical solution
        self.assertAlmostEqual(y_next, expected_result,places=2)

    def test_euler(self):
        # Define a simple test ODE: dy/dt = -y
        def test_ode(t, y):
            return -y

        # Initial conditions
        y0 = 1.0
        t = 0.0
        dt = 0.01

        # Use Runge-Kutta 4 to solve the ODE
        y_next = im.euler(test_ode, t, y0, dt)

        # The solution for this ODE is y(t) = e^(-t)
        expected_result = np.exp(-t)
        self.assertAlmostEqual(y_next, expected_result, places=1)



if __name__ == '__main__':
    unittest.main()
