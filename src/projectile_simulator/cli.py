import argparse
from projectile_simulator.physics import (
    calculate_range, calculate_max_height,
    calculate_time_of_flight, generate_trajectory
)
from projectile_simulator.visualizer import plot_trajectory

def get_texts(lang="fa"):
    """Return texts in Persian or English"""
    if lang == "en":
        return {
            "title": "Projectile Physics Simulator",
            "prompt_velocity": "Enter initial velocity (m/s): ",
            "prompt_angle": "Enter angle (degrees): ",
            "invalid_input": "❌ Please enter valid numbers.",
            "results": "📊 Results:",
            "range": "Range: {:.2f} meters",
            "max_height": "Max Height: {:.2f} meters",
            "time_of_flight": "Time of Flight: {:.2f} seconds",
        }
    else:
        return {
            "title": "شبیه‌ساز حرکت پرتابه",
            "prompt_velocity": "سرعت اولیه (m/s) را وارد کنید: ",
            "prompt_angle": "زاویه (درجه) را وارد کنید: ",
            "invalid_input": "❌ لطفاً اعداد معتبر وارد کنید.",
            "results": "📊 نتایج:",
            "range": "برد پرتابه: {:.2f} متر",
            "max_height": "حداکثر ارتفاع: {:.2f} متر",
            "time_of_flight": "زمان کل پرواز: {:.2f} ثانیه",
        }

def main():
    parser = argparse.ArgumentParser(description="Projectile Physics Simulator")
    parser.add_argument("--lang", choices=["fa", "en"], default="fa", help="Choose language: fa (Persian) or en (English)")
    args = parser.parse_args()

    texts = get_texts(args.lang)
    print("=" * 40)
    print(f"🚀 {texts['title']}")
    print("=" * 40)

    try:
        v0 = float(input(texts["prompt_velocity"]))
        theta_deg = float(input(texts["prompt_angle"]))
    except ValueError:
        print(texts["invalid_input"])
        return

    R = calculate_range(v0, theta_deg)
    H = calculate_max_height(v0, theta_deg)
    T = calculate_time_of_flight(v0, theta_deg)

    print(f"\n{texts['results']}")
    print(f"   {texts['range'].format(R)}")
    print(f"   {texts['max_height'].format(H)}")
    print(f"   {texts['time_of_flight'].format(T)}")

    x, y = generate_trajectory(v0, theta_deg)
    plot_trajectory(x, y, title="Projectile Trajectory" if args.lang == "en" else "مسیر حرکت پرتابه")

if __name__ == "__main__":
    main()
