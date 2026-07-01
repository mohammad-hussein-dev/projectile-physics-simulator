"""
Unit tests for the visualizer module.
"""

import matplotlib.pyplot as plt
from projectile_simulator.visualizer import plot_trajectory


def test_plot_trajectory_standard():
    """Test trajectory plotting with standard data."""
    x = [0.0, 1.0, 2.0, 3.0, 4.0]
    y = [0.0, 2.0, 3.0, 2.0, 0.0]

    plot_trajectory(x, y, title="Test Title")
    assert plt.gcf().number > 0
    plt.close()


def test_plot_trajectory_english_title():
    """Test trajectory plotting with English title."""
    x = [0.0, 1.0, 2.0]
    y = [0.0, 1.0, 0.0]

    plot_trajectory(x, y, title="Projectile Trajectory")
    assert plt.gca().get_xlabel() == "Horizontal Distance (m)"
    assert plt.gca().get_ylabel() == "Height (m)"
    plt.close()


def test_plot_trajectory_persian_title():
    """Test trajectory plotting with Persian title."""
    x = [0.0, 1.0, 2.0]
    y = [0.0, 1.0, 0.0]

    plot_trajectory(x, y, title="مسیر حرکت پرتابه")
    assert plt.gca().get_xlabel() == "فاصله افقی (متر)"
    assert plt.gca().get_ylabel() == "ارتفاع (متر)"
    plt.close()


def test_plot_trajectory_empty_data():
    """Test trajectory plotting with empty data."""
    plot_trajectory([], [])
    assert plt.gcf().number > 0
    plt.close()
