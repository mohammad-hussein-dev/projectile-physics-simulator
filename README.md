## 📋 Projectile Physics Simulator

[![CI](https://github.com/mohammad-hussein-dev/projectile-physics-simulator/actions/workflows/ci.yml/badge.svg)](https://github.com/mohammad-hussein-dev/projectile-physics-simulator/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/mohammad-hussein-dev/projectile-physics-simulator/branch/main/graph/badge.svg)](https://codecov.io/gh/mohammad-hussein-dev/projectile-physics-simulator)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

> **A 2D projectile motion simulator built with Python and matplotlib** — turning kinematic equations into visual trajectories.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Installation & Usage](#-installation--usage)
- [Sample Output](#-sample-output)
- [Testing](#-testing)
- [Project Structure](#-project-structure)
- [Development Workflow](#-development-workflow)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

---

## 📖 Overview

This project simulates the trajectory of a projectile launched with a given **initial velocity** and **angle**. It calculates key physics parameters — **range**, **maximum height**, and **time of flight** — and visualizes the motion in a clean, interactive plot.

Perfect for students, educators, and anyone interested in the intersection of physics and programming.

**Perfect for:**
- Learning physics through interactive visualization
- Teaching projectile motion concepts
- Showcasing clean Python code with scientific computing
- Portfolio projects for aspiring developers

---

## ✨ Features

| Feature | Description |
| :--- | :--- |
| 🎯 **Accurate Physics** | Uses standard kinematic equations (`g = 9.8 m/s²`) |
| 📊 **Live Plotting** | Visualizes the trajectory using `matplotlib` |
| 🌍 **Bilingual** | Supports both Persian (`fa`) and English (`en`) output |
| ⚡ **CLI Interface** | Simple and intuitive command-line usage |
| ✅ **100% Test Coverage** | Fully tested with `pytest` |
| 🧹 **Clean Code** | Well-structured, modular, and maintainable |

---

## 🧮 Physics Behind It

The simulation uses the following kinematic equations:

| Parameter | Formula |
| :--- | :--- |
| **Range (R)** | `R = (v₀² × sin(2θ)) / g` |
| **Max Height (H)** | `H = (v₀² × sin²(θ)) / (2g)` |
| **Time of Flight (T)** | `T = (2 × v₀ × sin(θ)) / g` |

> Where `v₀` is initial velocity (m/s), `θ` is launch angle (degrees), and `g = 9.8 m/s²`.

---

## 🛠️ Technology Stack

| Category | Technologies |
| :--- | :--- |
| **Language** | Python 3.8+ |
| **Scientific Computing** | NumPy, Matplotlib |
| **Testing** | pytest, pytest-cov |
| **Code Quality** | Black, Ruff, MyPy |
| **CI/CD** | GitHub Actions, Codecov |
| **Package Management** | setuptools, pyproject.toml |

---

## 🚀 Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/mohammad-hussein-dev/projectile-physics-simulator.git
cd projectile-physics-simulator
```

### 2. Set up a virtual environment (recommended)

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

```
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

```
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

### Run all tests

```bash
pytest tests/ -v --cov=src/projectile_simulator --cov-report=term
```

### Run with coverage report

```bash
pytest tests/ -v --cov=src/projectile_simulator --cov-report=html
```

Open `htmlcov/index.html` in your browser for detailed coverage breakdown.

### Test coverage badge

[![codecov](https://codecov.io/gh/mohammad-hussein-dev/projectile-physics-simulator/branch/main/graph/badge.svg)](https://codecov.io/gh/mohammad-hussein-dev/projectile-physics-simulator)

---

## 📁 Project Structure

```
projectile-physics-simulator/
├── src/
│   └── projectile_simulator/
│       ├── __init__.py
│       ├── __main__.py          # Entry point for the package
│       ├── cli.py               # Command-line interface
│       ├── physics.py           # Physics calculations
│       └── visualizer.py        # Plotting and visualization
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   ├── test_main.py
│   ├── test_physics.py
│   └── test_visualizer.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── LICENSE
├── pyproject.toml               # Project metadata & dependencies
└── README.md
```

---

## 🛠️ Development Workflow

### Commit Convention

Following [Conventional Commits](https://www.conventionalcommits.org/):

```bash
feat(physics): add drag force calculation
fix(visualizer): correct axis labels
refactor(cli): simplify argument parsing
docs(readme): update installation guide
test(physics): add edge case tests
```

### Code Quality Tools

| Tool | Purpose |
| :--- | :--- |
| **Black** | Code formatting |
| **Ruff** | Linting & import sorting |
| **MyPy** | Static type checking |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'feat: add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

**Before submitting a PR, ensure:**
- ✅ All tests pass (`pytest`)
- ✅ Code is formatted (`black .`)
- ✅ Linting passes (`ruff check .`)
- ✅ No commented-out code or debug prints
- ✅ New features include tests
- ✅ Documentation is updated

---

## 📄 License

Distributed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

## 👨‍💻 Author

**Mohammad Hussein**  
- 🌐 GitHub: [@mohammad-hussein-dev](https://github.com/mohammad-hussein-dev)  
- 📧 Email: [king.mohamd.09876@gmail.com](mailto:king.mohamd.09876@gmail.com)  
- 💬 Telegram: [@mohammad_hussein_dev](https://t.me/mohammad_hussein_dev)

> *"I don't just write code — I simulate the universe."*

---

## ⭐ Support the Project

If you found this project helpful, please consider giving it a **star** on GitHub! ⭐  
It helps others discover it and motivates further development.

---

**Built with 🚀 and Python**
