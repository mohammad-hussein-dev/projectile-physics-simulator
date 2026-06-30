"""
projectile_simulator — A Python package for projectile motion simulation.

====================================================================

This package provides a set of functions and tools to simulate and
visualize 2D projectile motion using standard kinematic equations.
It is designed for educational purposes, physics demonstrations,
and as a portfolio project for aspiring software engineers.

The package includes:
    - Physics calculations: range, max height, time of flight.
    - Trajectory generation: discrete (x, y) points for plotting.
    - Visualization: Matplotlib-based plot with bilingual support.

Usage:
    from projectile_simulator import calculate_range, plot_trajectory

    # Calculate the range for a projectile launched at 10 m/s, 45°
    range_value = calculate_range(10, 45)

    # Generate trajectory points and plot them
    x, y = generate_trajectory(10, 45)
    plot_trajectory(x, y)

Version:
    0.1.0
"""

# Import public API functions from submodules
from projectile_simulator.physics import (
    calculate_range,          # Calculate horizontal range
    calculate_max_height,      # Calculate peak height
    calculate_time_of_flight,  # Calculate total flight time
    generate_trajectory,       # Generate (x, y) trajectory points
)
from projectile_simulator.visualizer import plot_trajectory  # Plot the trajectory

# Define the public API of the package
__all__ = [
    "calculate_range",           # Public: range calculation
    "calculate_max_height",      # Public: height calculation
    "calculate_time_of_flight",  # Public: time of flight
    "generate_trajectory",       # Public: trajectory generation
    "plot_trajectory",           # Public: trajectory plotting
]

# Package metadata
__version__ = "0.1.0"  # Semantic version: major.minor.patch
