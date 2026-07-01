"""
Command-line interface for the projectile physics simulator.

This module provides a user-friendly CLI for running the projectile simulation.
It supports both Persian and English languages via the --lang flag.

Usage:
    python -m projectile_simulator.cli
    python -m projectile_simulator.cli --lang en

Examples:
    projectile                    # Run in Persian (default)
    projectile --lang en          # Run in English
"""

import argparse
from projectile_simulator.physics import (
    calculate_range,
    calculate_max_height,
    calculate_time_of_flight,
    generate_trajectory,
)
from projectile_simulator.visualizer import plot_trajectory


def get_texts(lang: str = "fa") -> dict:
    """
    Return user-facing texts in the specified language.

    Args:
        lang: Language code ('fa' for Persian, 'en' for English).

    Returns:
        A dictionary containing all UI strings for the selected language.
    """
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
    # Default to Persian
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


def main() -> None:
    """Main entry point for the CLI application."""
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(
        description="Projectile Physics Simulator — simulate and visualize 2D projectile motion."
    )
    parser.add_argument(
        "--lang",
        choices=["fa", "en"],
        default="fa",
        help="Choose language: fa (Persian) or en (English)"
    )
    args = parser.parse_args()  # pragma: no cover

    # Load UI texts based on the selected language
    texts = get_texts(args.lang)

    # Display the application header
    print("=" * 40)
    print(f"🚀 {texts['title']}")
    print("=" * 40)

    # Get user input with error handling
    try:
        v0 = float(input(texts["prompt_velocity"]))
        theta_deg = float(input(texts["prompt_angle"]))
    except ValueError:
        print(texts["invalid_input"])
        return

    # Ensure velocity is positive to avoid invalid physics calculations
    if v0 <= 0:
        error_msg = "❌ Velocity must be positive." if args.lang == "en" else "❌ سرعت باید مثبت باشد."
        print(error_msg)
        return

    # Perform physics calculations
    R = calculate_range(v0, theta_deg)
    H = calculate_max_height(v0, theta_deg)
    T = calculate_time_of_flight(v0, theta_deg)

    # Display the results
    print(f"\n{texts['results']}")
    print(f"   {texts['range'].format(R)}")
    print(f"   {texts['max_height'].format(H)}")
    print(f"   {texts['time_of_flight'].format(T)}")

    # Generate trajectory points and plot the graph
    x, y = generate_trajectory(v0, theta_deg)
    plot_trajectory(
        x, y,
        title="Projectile Trajectory" if args.lang == "en" else "مسیر حرکت پرتابه"
    )


if __name__ == "__main__":
    main()
