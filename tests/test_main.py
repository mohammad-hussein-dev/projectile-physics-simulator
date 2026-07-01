"""
Unit tests for the __main__ module.
"""

import sys
import pytest


def test_main_module_runs():
    """Test that the __main__.py module imports without errors."""
    import projectile_simulator.__main__ as main_module
    assert hasattr(main_module, 'main')


def test_main_module_execution(monkeypatch, capsys):
    """
    Test that __main__.py executes main successfully.

    This test verifies that the __main__ module can run the CLI
    and produce the expected Persian output.
    """
    # Set sys.argv to avoid pytest arguments interfering
    monkeypatch.setattr(sys, 'argv', ['__main__.py'])

    # Simulate user input
    inputs = iter(["10", "45"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Import and execute __main__
    import projectile_simulator.__main__ as main_module

    # Call the main function
    main_module.main()

    # Capture output
    captured = capsys.readouterr()

    # Verify Persian output from the main module
    assert "شبیه‌ساز حرکت پرتابه" in captured.out
    assert "برد پرتابه: 10.20 متر" in captured.out
    assert "حداکثر ارتفاع: 2.55 متر" in captured.out
    assert "زمان کل پرواز: 1.44 ثانیه" in captured.out
