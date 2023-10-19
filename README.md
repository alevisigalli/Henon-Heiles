# Henon-Heiles System Integration

This repository contains a Python script for simulating and analyzing trajectories in the Henon-Heiles system using various numerical integration methods.

## Table of Contents
- [Author](#author)
- [Background](#background)
- [Usage](#usage)
- [Installation](#installation)
- [Integration Methods](#integration-methods)
- [Examples](#examples)

## Authors
Alessia Visigalli, PhD student

## Background
The Henon-Heiles system, also known as the Henon-Heiles Hamiltonian, is a simple but important example of a dynamical system that exhibits chaotic behavior. It was introduced by Michel Henon and Carl Heiles in 1964 as a simplified model for certain astronomical systems, such as stars moving in a galaxy. The system is characterized by its conservative, Hamiltonian dynamics, meaning that the total energy is conserved.

The Henon-Heiles Hamiltonian describes the motion of a particle in a two-dimensional potential field, which can be expressed as follows:

$H=\frac{1}{2}(p_x^2+p_y^2)+\frac{1}{2}(x^2+y^2)+x^2y-\frac{1}{3}y^3$

Where:

- H is the Hamiltonian, which represents the total energy of the system.
- x and y are the particle's coordinates in the x and y directions.
- px and py are the corresponding momentum components.
- The terms in the Hamiltonian represent kinetic energy $\frac{1}{2}(p_x^2+p_y^2)+\frac{1}{2}(x^2+y^2)$ and potential energy $x^2y-\frac{1}{3}y^3$

The Henon-Heiles system is a classic example of a Hamiltonian system that has been extensively studied in the context of chaos theory and nonlinear dynamics. It serves as a model system for understanding the behavior of more complex physical systems with chaotic dynamics. Researchers use it to explore fundamental concepts in dynamical systems, such as phase space, stability, and bifurcations, as well as the transition from regular to chaotic motion.

The equations of motion for this system are defined as follows:

$$
\begin{aligned}
\frac{dx}{dt}=p \\
\frac{dp}{dt}=-x-2xy \\
\frac{dy}{dt}=q \\
\frac{dq}{dt}=-y-(x^2-y^2)
\end{aligned}
$$

where `(x, p)` and `(y, q)` are the coordinates and momenta of the two particles, respectively.

## Usage

To use this code, you can run the `henon_heiles.py` script, which allows you to choose different integration methods and initial conditions. The available integration methods include Runge-Kutta 2, Runge-Kutta 4, LeapFrog, and Euler. You can select the initial conditions based on different trajectories of the Henon-Heiles system, such as "Outside separatrix," "Distorted torus," or "Hyperbolic points (separatrices)."

Here's an example of how to use the code:

```bash
python henon_heiles.py --rk2 --outer
```
This command will run the simulation using Runge-Kutta 2 integration method with initial conditions for the outside separatrix.

##Intallation
To get started, follow these steps:
1) Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/henon-heiles.git
   cd henon-heiles
   ```
2) Make sure you have Python and the required dependencies installed. You can install the dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
3) Run the code as described in the Usage section.

## Integration methods
This code provides several integration methods to solve the equations of motion:

- Runge-Kutta 2 (RK2): A second-order numerical method.
- Runge-Kutta 4 (RK4): A fourth-order numerical method.
- LeapFrog: A symplectic integration method for Hamiltonian systems.
- Euler: A simple first-order numerical method.

You can choose your preferred method when running the code.

## Examples
Here are some example scenarios and trajectories:
### Outside Separatrix
```bash
python henon_heiles.py --rk2 --outer
```
![png](Figures/Outer.png)

### Distorted Torus
```bash
python henon_heiles.py --rk4 --torus
```
![png](Figures/Torus.png)

### Hyperbolic Points (Separatrices)
```bash
python henon_heiles.py --leapfrog --hyperbolic
```
![png](Figures/Hyperbolic.png)

### All the previous solutions
```bash
python henon_heiles.py --leapfrog --all
```
![png](Figures/all.png)
