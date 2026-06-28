import math

GRAVITY = 9.8  # m/s²

def calculate_range(velocity: float, angle_deg: float) -> float:
    theta = math.radians(angle_deg)
    return (velocity ** 2 * math.sin(2 * theta)) / GRAVITY

def calculate_max_height(velocity: float, angle_deg: float) -> float:
    theta = math.radians(angle_deg)
    return (velocity ** 2 * (math.sin(theta) ** 2)) / (2 * GRAVITY)

def calculate_time_of_flight(velocity: float, angle_deg: float) -> float:
    theta = math.radians(angle_deg)
    return 2 * velocity * math.sin(theta) / GRAVITY

def generate_trajectory(velocity: float, angle_deg: float, steps: int = 100):
    theta = math.radians(angle_deg)
    T = calculate_time_of_flight(velocity, angle_deg)
    
    t = [i / steps for i in range(int(T * steps) + 1)]
    x = [velocity * math.cos(theta) * ti for ti in t]
    y = [velocity * math.sin(theta) * ti - 0.5 * GRAVITY * ti ** 2 for ti in t]
    return x, y
