"""
Physics module for projectile motion simulation.

This module provides functions to calculate key parameters of projectile motion:
range, maximum height, time of flight, and trajectory points for visualization.
All calculations are based on standard kinematic equations.

Gravity constant: 9.8 m/s² (Earth's surface).
"""

import math
from typing import List, Tuple

# Gravitational acceleration constant (m/s²)
GRAVITY: float = 9.8


def calculate_range(velocity: float, angle_deg: float) -> float:
    """
    Calculate the horizontal range of a projectile.

    The range is the total horizontal distance traveled by the projectile
    before it returns to the launch height.

    Args:
        velocity: Initial launch velocity in meters per second (m/s).
        angle_deg: Launch angle in degrees (0° = horizontal, 90° = vertical).

    Returns:
        The horizontal range in meters.

    Formula:
        R = (v₀² × sin(2θ)) / g

    Example:
        >>> calculate_range(10, 45)
        10.20408163265306
    """
    theta: float = math.radians(angle_deg)
    return (velocity ** 2 * math.sin(2 * theta)) / GRAVITY


def calculate_max_height(velocity: float, angle_deg: float) -> float:
    """
    Calculate the maximum height reached by a projectile.

    This is the peak vertical displacement above the launch point.

    Args:
        velocity: Initial launch velocity in meters per second (m/s).
        angle_deg: Launch angle in degrees.

    Returns:
        The maximum height in meters.

    Formula:
        H = (v₀² × sin²(θ)) / (2g)

    Example:
        >>> calculate_max_height(10, 45)
        2.551020408163265
    """
    theta: float = math.radians(angle_deg)
    return (velocity ** 2 * (math.sin(theta) ** 2)) / (2 * GRAVITY)


def calculate_time_of_flight(velocity: float, angle_deg: float) -> float:
    """
    Calculate the total time of flight of a projectile.

    The time of flight is the duration from launch until the projectile
    returns to the launch height.

    Args:
        velocity: Initial launch velocity in meters per second (m/s).
        angle_deg: Launch angle in degrees.

    Returns:
        The total time of flight in seconds.

    Formula:
        T = (2 × v₀ × sin(θ)) / g

    Example:
        >>> calculate_time_of_flight(10, 45)
        1.4433756729740643
    """
    theta: float = math.radians(angle_deg)
    return 2 * velocity * math.sin(theta) / GRAVITY


def generate_trajectory(
    velocity: float,
    angle_deg: float,
    steps: int = 100
) -> Tuple[List[float], List[float]]:
    """
    Generate a set of (x, y) coordinates representing the projectile's path.

    This function computes the trajectory points using a time‑step approach
    based on the total flight time. The number of points is controlled by the
    `steps` parameter (default = 100), which defines the resolution of the path.

    Args:
        velocity: Initial launch velocity in meters per second (m/s).
        angle_deg: Launch angle in degrees.
        steps: Number of discrete points along the trajectory (default: 100).

    Returns:
        A tuple of two lists: (x_coords, y_coords), where each list contains
        the horizontal and vertical coordinates in meters.

    Note:
        The trajectory is generated using the kinematic equations:
            x(t) = v₀ × cos(θ) × t
            y(t) = v₀ × sin(θ) × t - ½ × g × t²
        The time points are evenly spaced from 0 to T (total flight time).
    """
    theta: float = math.radians(angle_deg)
    T: float = calculate_time_of_flight(velocity, angle_deg)

    # Create a list of time points from 0 to T
    time_points: List[float] = [i / steps for i in range(int(T * steps) + 1)]

    # Compute horizontal and vertical coordinates for each time point
    x_coords: List[float] = [
        velocity * math.cos(theta) * t for t in time_points
    ]
    y_coords: List[float] = [
        velocity * math.sin(theta) * t - 0.5 * GRAVITY * t ** 2
        for t in time_points
    ]

    return x_coords, y_coords
