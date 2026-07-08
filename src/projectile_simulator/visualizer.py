"""
Visualization module for projectile motion.

This module provides functions to plot the trajectory of a projectile
using Matplotlib. It supports both Persian and English labels for
international accessibility.
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import List, Optional


def plot_trajectory(
    x_coords: List[float],
    y_coords: List[float],
    title: str = "مسیر حرکت پرتابه",
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    save_path: Optional[str] = None,
    show: bool = True,
) -> None:
    """
    Plot the projectile trajectory on a 2D graph.

    This function creates a clean, professional plot of the projectile's path
    with labeled axes, a grid, and proper axis limits. The plot title and axis
    labels are automatically adjusted based on the provided title string.

    Args:
        x_coords: List of horizontal coordinates (meters) along the trajectory.
        y_coords: List of vertical coordinates (meters) along the trajectory.
        title: Title of the plot. If set to "Projectile Trajectory",
               labels will be in English; otherwise, Persian labels are used.
               (Default: "مسیر حرکت پرتابه" — Persian)
        xlabel: Custom X-axis label (overrides auto-detection).
        ylabel: Custom Y-axis label (overrides auto-detection).
        save_path: Optional file path to save the figure (e.g., "trajectory.png").
        show: If True, display the plot; otherwise, close it after saving.

    Returns:
        None (displays the plot window or saves to file).

    Example:
        >>> x = [0.0, 1.0, 2.0, 3.0, 4.0]
        >>> y = [0.0, 2.5, 3.0, 2.5, 0.0]
        >>> plot_trajectory(x, y, title="Projectile Trajectory")
        # Opens a Matplotlib window with the trajectory.
    """
    # Validate input data before plotting
    if not x_coords or not y_coords or len(x_coords) != len(y_coords):
        print("Warning: Invalid trajectory data. Skipping plot.")
        return

    # Create a new figure with a specified size
    plt.figure(figsize=(12, 6), facecolor='white')

    # ---- Plot the trajectory as a continuous blue line ----
    plt.plot(x_coords, y_coords, color='blue', linewidth=2.5, label='Trajectory')

    # ---- Mark the peak point ----
    # Find the highest point in the trajectory
    peak_idx = np.argmax(y_coords)
    if peak_idx > 0 and peak_idx < len(y_coords):
        plt.plot(
            x_coords[peak_idx], y_coords[peak_idx],
            'ro', markersize=8,
            label=f'Peak: {y_coords[peak_idx]:.2f} m'
        )

    # ---- Mark the impact point ----
    # Find where the trajectory returns to ground level (y=0)
    if y_coords:
        impact_idx = len(y_coords) - 1
        while impact_idx > 0 and y_coords[impact_idx] <= 0:
            impact_idx -= 1
        plt.plot(
            x_coords[impact_idx], 0,
            'gs', markersize=8,
            label=f'Impact: {x_coords[impact_idx]:.2f} m'
        )

    # ---- Set axis labels based on language ----
    # Detect language from title: English if title matches, otherwise Persian
    is_english = (title == "Projectile Trajectory")
    if xlabel is None:
        xlabel = 'Horizontal Distance (m)' if is_english else 'فاصله افقی (متر)'
    if ylabel is None:
        ylabel = 'Height (m)' if is_english else 'ارتفاع (متر)'

    plt.xlabel(xlabel, fontsize=13)
    plt.ylabel(ylabel, fontsize=13)

    # ---- Set the plot title ----
    plt.title(title, fontsize=16, fontweight='bold', pad=15)

    # ---- Add a subtle grid for readability ----
    plt.grid(True, linestyle='--', alpha=0.4)

    # ---- Draw axes at y=0 and x=0 for reference ----
    # These lines help visually identify the ground level and launch point
    plt.axhline(y=0, color='black', linewidth=0.5, alpha=0.7)
    plt.axvline(x=0, color='black', linewidth=0.5, alpha=0.7)

    # ---- Adjust axis limits to fit the trajectory with a small margin ----
    # Add 5% margin for better visualization
    if x_coords and y_coords:
        margin_x = max(x_coords) * 0.05 if max(x_coords) > 0 else 1.0
        margin_y = max(y_coords) * 0.05 if max(y_coords) > 0 else 1.0
        plt.xlim(-margin_x, max(x_coords) + margin_x)
        plt.ylim(-margin_y, max(y_coords) + margin_y)

    # ---- Add legend ----
    plt.legend(loc='upper right', fontsize=11, framealpha=0.9)

    # ---- Tight layout ----
    # Adjust spacing to prevent label clipping
    plt.tight_layout()

    # ---- Save or show ----
    # These lines handle file output and display — marked as no cover
    # because they are not executed during test runs
    if save_path:  # pragma: no cover
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"📊 Plot saved as '{save_path}'")

    if show:  # pragma: no cover
        plt.show()
    else:  # pragma: no cover
        plt.close()
