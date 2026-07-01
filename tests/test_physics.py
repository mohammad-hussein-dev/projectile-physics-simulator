"""
Unit tests for the physics module of the projectile simulator.

This module contains comprehensive tests for all physics calculations:
- Range calculation (standard and edge cases)
- Maximum height calculation
- Time of flight calculation
- Trajectory generation

All floating-point comparisons use pytest.approx to handle numerical precision issues.
"""

import pytest
from projectile_simulator.physics import (
    calculate_range,
    calculate_max_height,
    calculate_time_of_flight,
    generate_trajectory,
)


# ============================================================
# Tests for calculate_range
# ============================================================

def test_calculate_range_standard():
    """Test range calculation with a standard 45° angle."""
    result = calculate_range(10, 45)
    assert abs(result - 10.20408163265306) < 0.001


def test_calculate_range_zero_angle():
    """Test range with 0° angle (should be 0)."""
    result = calculate_range(10, 0)
    assert result == 0.0


def test_calculate_range_90_angle():
    """
    Test range with 90° angle.

    With a 90° launch angle, the projectile goes straight up and comes
    straight down, so the horizontal range should be 0.
    """
    result = calculate_range(10, 90)
    # Use approx for floating-point precision
    assert result == pytest.approx(0.0, abs=1e-10)


def test_calculate_range_negative_velocity():
    """
    Test range with negative velocity.

    Negative velocity means the projectile is launched in the opposite
    direction. However, since range depends on v², the value remains
    positive (the projectile travels backward, but the distance is still
    a positive number).
    """
    result = calculate_range(-10, 45)
    assert result > 0
    assert abs(result - 10.20408163265306) < 0.001


def test_calculate_range_zero_velocity():
    """Test range with zero velocity (should be 0)."""
    result = calculate_range(0, 45)
    assert result == 0.0


# ============================================================
# Tests for calculate_max_height
# ============================================================

def test_calculate_max_height_standard():
    """Test max height calculation with a standard 45° angle."""
    result = calculate_max_height(10, 45)
    assert abs(result - 2.551020408163265) < 0.001


def test_calculate_max_height_zero_angle():
    """Test max height with 0° angle (should be 0)."""
    result = calculate_max_height(10, 0)
    assert result == 0.0


def test_calculate_max_height_90_angle():
    """
    Test max height with 90° angle.

    With a 90° launch angle, all initial velocity is directed upward,
    so the projectile reaches its maximum possible height.
    """
    result = calculate_max_height(10, 90)
    assert abs(result - 5.10204081632653) < 0.001


def test_calculate_max_height_zero_velocity():
    """Test max height with zero velocity (should be 0)."""
    result = calculate_max_height(0, 45)
    assert result == 0.0


# ============================================================
# Tests for calculate_time_of_flight
# ============================================================

def test_calculate_time_of_flight_standard():
    """Test time of flight with a standard 45° angle."""
    result = calculate_time_of_flight(10, 45)
    assert abs(result - 1.4433756729740643) < 0.001


def test_calculate_time_of_flight_zero_angle():
    """Test time of flight with 0° angle (should be 0)."""
    result = calculate_time_of_flight(10, 0)
    assert result == 0.0


def test_calculate_time_of_flight_90_angle():
    """
    Test time of flight with 90° angle.

    With a 90° launch angle, the projectile goes straight up and falls
    straight down, resulting in the longest possible flight time for a
    given initial velocity.
    """
    result = calculate_time_of_flight(10, 90)
    assert abs(result - 2.0408163265306123) < 0.001


def test_calculate_time_of_flight_zero_velocity():
    """Test time of flight with zero velocity (should be 0)."""
    result = calculate_time_of_flight(0, 45)
    assert result == 0.0


# ============================================================
# Tests for generate_trajectory
# ============================================================

def test_generate_trajectory_standard():
    """
    Test trajectory generation with standard parameters.

    Verifies:
    - Correct number of points based on flight time and step count
    - Start point at origin (0, 0)
    - End point at ground level (y ≈ 0)
    - All y values are non-negative
    """
    x, y = generate_trajectory(10, 45)

    # Check that we got lists of the expected length
    # Flight time is ~1.44s, with steps=100 → ~145 points
    expected_len = int(calculate_time_of_flight(10, 45) * 100) + 1
    assert len(x) == expected_len
    assert len(y) == expected_len

    # Start point should be (0, 0)
    assert x[0] == 0.0
    assert y[0] == 0.0

    # End point should be at ground level (y ≈ 0)
    # Use a tolerance of 0.03 to account for numerical approximation
    assert abs(y[-1]) < 0.03

    # All y values should be >= 0 (no negative heights)
    assert all(yi >= 0 for yi in y)


def test_generate_trajectory_zero_velocity():
    """
    Test trajectory generation with zero velocity.

    With zero initial velocity, the projectile doesn't move,
    so only the origin point should be generated.
    """
    x, y = generate_trajectory(0, 45)
    assert len(x) == 1  # Only the origin point
    assert len(y) == 1
    assert x[0] == 0.0
    assert y[0] == 0.0


def test_generate_trajectory_90_angle():
    """
    Test trajectory generation with 90° angle (vertical launch).

    With a vertical launch:
    - All x coordinates should be 0 (no horizontal movement)
    - The maximum y should match the theoretical max height
    """
    x, y = generate_trajectory(10, 90)

    # All x values should be 0 (no horizontal movement)
    # Use approx to handle floating-point precision
    for xi in x:
        assert xi == pytest.approx(0.0, abs=1e-10)

    # Max y should match the theoretical max height
    # Use a slightly larger tolerance (1e-6) to account for numerical error
    # in the step-by-step trajectory calculation
    assert max(y) == pytest.approx(calculate_max_height(10, 90), abs=1e-6)


def test_generate_trajectory_custom_steps():
    """Test trajectory generation with custom number of steps."""
    x_50, y_50 = generate_trajectory(10, 45, steps=50)
    x_200, y_200 = generate_trajectory(10, 45, steps=200)

    # More steps should produce more points
    assert len(x_50) < len(x_200)
    assert len(y_50) < len(y_200)


def test_generate_trajectory_negative_velocity():
    """
    Test trajectory generation with negative velocity.

    Negative velocity means the projectile is launched in the opposite
    direction, so all x coordinates should be negative or zero.
    """
    x, y = generate_trajectory(-10, 45)
    # All x values should be negative or zero (opposite direction)
    assert all(xi <= 0 for xi in x)


# ============================================================
# Parameterized tests
# ============================================================

@pytest.mark.parametrize("velocity, angle, expected_range", [
    (10, 30, 8.83),
    (10, 60, 8.83),
    (20, 45, 40.82),
    (15, 30, 19.86),
])
def test_calculate_range_parametrized(velocity, angle, expected_range):
    """
    Parametrized tests for range with various inputs.

    Uses a tolerance of 0.03 to account for rounding in the expected values.
    """
    result = calculate_range(velocity, angle)
    assert abs(result - expected_range) < 0.03


@pytest.mark.parametrize("velocity, angle, expected_height", [
    (10, 30, 1.28),
    (10, 60, 3.83),
    (20, 45, 10.20),
])
def test_calculate_max_height_parametrized(velocity, angle, expected_height):
    """Parametrized tests for max height with various inputs."""
    result = calculate_max_height(velocity, angle)
    assert abs(result - expected_height) < 0.01


@pytest.mark.parametrize("velocity, angle, expected_time", [
    (10, 30, 1.02),
    (10, 60, 1.77),
    (20, 45, 2.89),
])
def test_calculate_time_of_flight_parametrized(velocity, angle, expected_time):
    """Parametrized tests for time of flight with various inputs."""
    result = calculate_time_of_flight(velocity, angle)
    assert abs(result - expected_time) < 0.01
