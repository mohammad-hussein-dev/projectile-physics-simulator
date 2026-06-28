import matplotlib.pyplot as plt

def plot_trajectory(x: list, y: list, title: str = "مسیر حرکت پرتابه"):
    """Plot the projectile trajectory with optional title"""
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, color='blue', linewidth=2)
    plt.title(title)
    plt.xlabel('Horizontal Distance (m)' if title == "Projectile Trajectory" else 'فاصله افقی (متر)')
    plt.ylabel('Height (m)' if title == "Projectile Trajectory" else 'ارتفاع (متر)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.axhline(y=0, color='black', linewidth=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5)
    if x:
        plt.xlim(0, max(x) + 1)
        plt.ylim(0, max(y) + 1)
    plt.show()
