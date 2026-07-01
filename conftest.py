"""
Pytest configuration file.
This file is automatically loaded by pytest before running any tests.
"""

import warnings
import matplotlib

# Use non-interactive backend for all tests (must be before importing matplotlib)
matplotlib.use('Agg')

# Suppress all UserWarning from matplotlib
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")
