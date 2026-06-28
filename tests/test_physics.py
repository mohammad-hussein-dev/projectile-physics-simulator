import pytest
from projectile_simulator.physics import (
    calculate_range, calculate_max_height, calculate_time_of_flight
)

def test_calculate_range():
    result = calculate_range(10, 45)
    assert abs(result - 10.204) < 0.01

def test_calculate_max_height():
    result = calculate_max_height(10, 45)
    assert abs(result - 2.551) < 0.01

def test_calculate_time_of_flight():
    result = calculate_time_of_flight(10, 45)
    assert abs(result - 1.443) < 0.01
