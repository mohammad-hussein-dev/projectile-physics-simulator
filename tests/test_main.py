"""
Unit tests for the __main__ module.
"""

import sys
import subprocess
import pytest


def test_main_module_runs():
    """Test that the __main__.py module imports without errors."""
    import projectile_simulator.__main__ as main_module
    assert hasattr(main_module, 'main')


def test_main_module_execution(monkeypatch, capsys):
    """Test that __main__.py executes main successfully."""
    monkeypatch.setattr(sys, 'argv', ['__main__.py'])

    inputs = iter(["10", "45"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    import projectile_simulator.__main__ as main_module
    main_module.main()

    captured = capsys.readouterr()
    assert "شبیه‌ساز حرکت پرتابه" in captured.out


def test_main_module_as_script():
    """Test running __main__.py as a script."""
    result = subprocess.run(
        [sys.executable, "-m", "projectile_simulator"],
        input="10\n45\n",
        capture_output=True,
        text=True,
    )
    assert "شبیه‌ساز حرکت پرتابه" in result.stdout
