"""
Physics module for projectile motion simulation.

This module provides functions to calculate key parameters of projectile motion:
range, maximum height, time of flight, and trajectory points for visualization.
All calculations are based on standard kinematic equations.

Gravity constant: 9.8 m/s² (Earth's surface).
"""

import math
from typing import List, Tuple, Optional

# Gravitational acceleration constant (m/s²)
GRAVITY: float = 9.8


def calculate_range(
    velocity: float,
    angle_deg: float,
    gravity: Optional[float] = None,
) -> float:
    """
    Calculate the horizontal range of a projectile.

    The range is the total horizontal distance traveled by the projectile
    before it returns to the launch height.

    Args:
        velocity: Initial launch velocity in meters per second (m/s).
        angle_deg: Launch angle in degrees (0° = horizontal, 90° = vertical).
        gravity: Optional custom gravity (defaults to GRAVITY constant).

    Returns:
        The horizontal range in meters.

    Formula:
        R = (v₀² × sin(2θ)) / g

    Example:
        >>> calculate_range(10, 45)
        10.20408163265306
    """
    if gravity is None:
        gravity = GRAVITY
    theta: float = math.radians(angle_deg)
    return (velocity ** 2 * math.sin(2 * theta)) / gravity


def calculate_max_height(
    velocity: float,
    angle_deg: float,
    gravity: Optional[float] = None,
) -> float:
    """
    Calculate the maximum height reached by a projectile.

    This is the peak vertical displacement above the launch point.

    Args:
        velocity: Initial launch velocity in meters per second (m/s).
        angle_deg: Launch angle in degrees.
        gravity: Optional custom gravity (defaults to GRAVITY constant).

    Returns:
        The maximum height in meters.

    Formula:
        H = (v₀² × sin²(θ)) / (2g)

    Example:
        >>> calculate_max_height(10, 45)
        2.551020408163265
    """
    if gravity is None:
        gravity = GRAVITY
    theta: float = math.radians(angle_deg)
    return (velocity ** 2 * (math.sin(theta) ** 2)) / (2 * gravity)


def calculate_time_of_flight(
    velocity: float,
    angle_deg: float,
    gravity: Optional[float] = None,
) -> float:
    """
    Calculate the total time of flight of a projectile.

    The time of flight is the duration from launch until the projectile
    returns to the launch height.

    Args:
        velocity: Initial launch velocity in meters per second (m/s).
        angle_deg: Launch angle in degrees.
        gravity: Optional custom gravity (defaults to GRAVITY constant).

    Returns:
        The total time of flight in seconds.

    Formula:
        T = (2 × v₀ × sin(θ)) / g

    Example:
        >>> calculate_time_of_flight(10, 45)
        1.4433756729740643
    """
    if gravity is None:
        gravity = GRAVITY
    theta: float = math.radians(angle_deg)
    return 2 * velocity * math.sin(theta) / gravity


def generate_trajectory(
    velocity: float,
    angle_deg: float,
    steps: int = 100,
    gravity: Optional[float] = None,
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
        gravity: Optional custom gravity (defaults to GRAVITY constant).

    Returns:
        A tuple of two lists: (x_coords, y_coords), where each list contains
        the horizontal and vertical coordinates in meters.

    Note:
        The trajectory is generated using the kinematic equations:
            x(t) = v₀ × cos(θ) × t
            y(t) = v₀ × sin(θ) × t - ½ × g × t²
        The time points are evenly spaced from 0 to T (total flight time).
    """
    if gravity is None:
        gravity = GRAVITY
    theta: float = math.radians(angle_deg)
    T: float = calculate_time_of_flight(velocity, angle_deg, gravity)

    if T <= 0 or steps <= 0:
        return [], []

    # Create a list of time points from 0 to T
    num_points: int = int(T * steps) + 1
    time_points: List[float] = [t * T / (num_points - 1) for t in range(num_points)]

    # Compute horizontal and vertical coordinates for each time point
    vx: float = velocity * math.cos(theta)
    vy: float = velocity * math.sin(theta)

    x_coords: List[float] = [vx * t for t in time_points]
    y_coords: List[float] = [vy * t - 0.5 * gravity * t ** 2 for t in time_points]

    # Ensure y coordinates don't go below zero (impact point)
    y_coords = [max(0.0, y) for y in y_coords]

    return x_coords, y_coords
