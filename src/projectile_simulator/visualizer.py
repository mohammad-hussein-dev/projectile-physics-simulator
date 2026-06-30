"""
Visualization module for projectile motion.

This module provides functions to plot the trajectory of a projectile
using Matplotlib. It supports both Persian and English labels for
international accessibility.
"""

import matplotlib.pyplot as plt
from typing import List, Optional


def plot_trajectory(
    x: List[float],
    y: List[float],
    title: str = "مسیر حرکت پرتابه"
) -> None:
    """
    Plot the projectile trajectory on a 2D graph.

    This function creates a clean, professional plot of the projectile's path
    with labeled axes, a grid, and proper axis limits. The plot title and axis
    labels are automatically adjusted based on the provided title string.

    Args:
        x: List of horizontal coordinates (meters) along the trajectory.
        y: List of vertical coordinates (meters) along the trajectory.
        title: Title of the plot. If set to "Projectile Trajectory",
               labels will be in English; otherwise, Persian labels are used.
               (Default: "مسیر حرکت پرتابه" — Persian)

    Returns:
        None (displays the plot window).

    Example:
        >>> x = [0.0, 1.0, 2.0, 3.0, 4.0]
        >>> y = [0.0, 2.5, 3.0, 2.5, 0.0]
        >>> plot_trajectory(x, y, title="Projectile Trajectory")
        # Opens a Matplotlib window with the trajectory.
    """
    # Create a new figure with a specified size
    plt.figure(figsize=(10, 5))

    # Plot the trajectory as a continuous blue line
    plt.plot(x, y, color='blue', linewidth=2, label='Trajectory')

    # Set the plot title (supports English or Persian)
    plt.title(title)

    # Set axis labels based on the language of the title
    is_english: bool = (title == "Projectile Trajectory")
    plt.xlabel('Horizontal Distance (m)' if is_english else 'فاصله افقی (متر)')
    plt.ylabel('Height (m)' if is_english else 'ارتفاع (متر)')

    # Add a subtle grid for readability
    plt.grid(True, linestyle='--', alpha=0.6)

    # Draw axes at y=0 and x=0 for reference
    plt.axhline(y=0, color='black', linewidth=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5)

    # Adjust axis limits to fit the trajectory with a small margin
    if x:
        plt.xlim(0, max(x) + 1)
        plt.ylim(0, max(y) + 1)

    # Display the plot
    plt.show()
