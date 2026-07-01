```markdown
# 🚀 Projectile Physics Simulator

[![CI](https://github.com/mohammad-hussein-dev/projectile-physics-simulator/actions/workflows/ci.yml/badge.svg)](https://github.com/mohammad-hussein-dev/projectile-physics-simulator/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> A 2D projectile motion simulator built with Python and matplotlib — turning kinematic equations into visual trajectories.

---

## 📖 Overview

This project simulates the trajectory of a projectile launched with a given **initial velocity** and **angle**. It calculates key physics parameters — **range**, **maximum height**, and **time of flight** — and visualizes the motion in a clean, interactive plot.

Perfect for students, educators, and anyone interested in the intersection of physics and programming.

### ✨ Features

- 🎯 **Accurate Physics** — Uses standard kinematic equations (`g = 9.8 m/s²`)
- 📊 **Live Plotting** — Visualizes the trajectory using `matplotlib`
- 🌍 **Bilingual** — Supports both Persian (`fa`) and English (`en`) output
- ⚡ **CLI Interface** — Simple and intuitive command-line usage
- ✅ **100% Test Coverage** — Fully tested with `pytest`

---

## 🧮 Physics Behind It

The simulation uses the following equations:

| Parameter | Formula |
| :--- | :--- |
| **Range (R)** | `R = (v₀² × sin(2θ)) / g` |
| **Max Height (H)** | `H = (v₀² × sin²(θ)) / (2g)` |
| **Time of Flight (T)** | `T = (2 × v₀ × sin(θ)) / g` |

> Where `v₀` is initial velocity (m/s), `θ` is launch angle (degrees), and `g = 9.8 m/s²`.

---

## 🛠️ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/mohammad-hussein-dev/projectile-physics-simulator.git
cd projectile-physics-simulator
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install the package

```bash
pip install -e .
```

### 4. Run the simulator

```bash
# Persian (default)
projectile

# English
projectile --lang en
```

You will be prompted to enter:

- **Initial velocity** (m/s)
- **Launch angle** (degrees)

The program will then display the calculated results and show a trajectory plot.

---

## 📊 Sample Output

### English Version

```bash
========================================
🚀 Projectile Physics Simulator
========================================
Enter initial velocity (m/s): 10
Enter angle (degrees): 45

📊 Results:
   Range: 10.20 meters
   Max Height: 2.55 meters
   Time of Flight: 1.44 seconds
```

![Trajectory](trajectory_en.png)

---

### نسخه‌ی فارسی

```bash
========================================
🚀 شبیه‌ساز حرکت پرتابه
========================================
سرعت اولیه (m/s) را وارد کنید: 10
زاویه (درجه) را وارد کنید: 45

📊 نتایج:
   برد پرتابه: 10.20 متر
   حداکثر ارتفاع: 2.55 متر
   زمان کل پرواز: 1.44 ثانیه
```

![Trajectory](trajectory_fa.png)

---

## 🧪 Testing

This project uses `pytest` for unit testing with **100% test coverage**.

Run the tests:

```bash
pytest tests/ -v --cov=src/projectile_simulator --cov-report=term
```

---

## 📁 Project Structure

```
projectile-physics-simulator/
├── src/
│   └── projectile_simulator/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── physics.py
│       └── visualizer.py
├── tests/
│   ├── test_cli.py
│   ├── test_main.py
│   ├── test_physics.py
│   └── test_visualizer.py
├── pyproject.toml
├── README.md
├── LICENSE
└── .github/workflows/ci.yml
```

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements, feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Mohammad Hussein** — [GitHub](https://github.com/mohammad-hussein-dev)

---

⭐ If you found this project helpful, consider giving it a star on GitHub!
```
