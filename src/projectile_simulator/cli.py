from projectile_simulator.physics import (
    calculate_range, calculate_max_height,
    calculate_time_of_flight, generate_trajectory
)
from projectile_simulator.visualizer import plot_trajectory

def main():
    print("=" * 40)
    print("🚀 Projectile Physics Simulator")
    print("=" * 40)
    
    try:
        v0 = float(input("سرعت اولیه (m/s) را وارد کنید: "))
        theta_deg = float(input("زاویه (درجه) را وارد کنید: "))
    except ValueError:
        print("❌ لطفاً اعداد معتبر وارد کنید.")
        return
    
    R = calculate_range(v0, theta_deg)
    H = calculate_max_height(v0, theta_deg)
    T = calculate_time_of_flight(v0, theta_deg)
    
    print(f"\n📊 نتایج:")
    print(f"   برد پرتابه: {R:.2f} متر")
    print(f"   حداکثر ارتفاع: {H:.2f} متر")
    print(f"   زمان کل پرواز: {T:.2f} ثانیه")
    
    x, y = generate_trajectory(v0, theta_deg)
    plot_trajectory(x, y)

if __name__ == "__main__":
    main()
