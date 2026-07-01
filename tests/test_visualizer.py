"""
Unit tests for the visualizer module.
"""

import warnings
import matplotlib

# Use non-interactive backend for testing
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from projectile_simulator.visualizer import plot_trajectory

# Suppress UserWarning from plt.show() in non-interactive environment
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")


def test_plot_trajectory_standard():
    """Test trajectory plotting with standard data."""
    x = [0.0, 1.0, 2.0, 3.0, 4.0]
    y = [0.0, 2.0, 3.0, 2.0, 0.0]

    # Just test that the function runs without errors
    plot_trajectory(x, y, title="Test Title")

    # Verify that a figure was created
    assert plt.gcf().number > 0

    # Clean up
    plt.close()


def test_plot_trajectory_english_title():
    """Test trajectory plotting with English title."""
    x = [0.0, 1.0, 2.0]
    y = [0.0, 1.0, 0.0]

    plot_trajectory(x, y, title="Projectile Trajectory")

    # The axis labels should be in English
    assert plt.gca().get_xlabel() == "Horizontal Distance (m)"
    assert plt.gca().get_ylabel() == "Height (m)"

    plt.close()


def test_plot_trajectory_persian_title():
    """Test trajectory plotting with Persian title."""
    x = [0.0, 1.0, 2.0]
    y = [0.0, 1.0, 0.0]

    plot_trajectory(x, y, title="مسیر حرکت پرتابه")

    # The axis labels should be in Persian
    assert plt.gca().get_xlabel() == "فاصله افقی (متر)"
    assert plt.gca().get_ylabel() == "ارتفاع (متر)"

    plt.close()


def test_plot_trajectory_empty_data():
    """Test trajectory plotting with empty data."""
    plot_trajectory([], [])

    # Should not crash, and should still create a figure
    assert plt.gcf().number > 0

    plt.close()
