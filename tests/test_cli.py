"""
Unit tests for the CLI module.
"""

import sys
import pytest
from projectile_simulator.cli import main


def test_cli_main_persian(monkeypatch, capsys):
    """Test CLI in Persian language (default)."""
    monkeypatch.setattr(sys, 'argv', ['cli.py'])

    inputs = iter(["10", "45"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "شبیه‌ساز حرکت پرتابه" in captured.out
    assert "برد پرتابه: 10.20 متر" in captured.out
    assert "حداکثر ارتفاع: 2.55 متر" in captured.out
    assert "زمان کل پرواز: 1.44 ثانیه" in captured.out


def test_cli_main_english(monkeypatch, capsys):
    """Test CLI in English language."""
    monkeypatch.setattr(sys, 'argv', ['cli.py', '--lang', 'en'])

    inputs = iter(["10", "45"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "Projectile Physics Simulator" in captured.out
    assert "Range: 10.20 meters" in captured.out
    assert "Max Height: 2.55 meters" in captured.out
    assert "Time of Flight: 1.44 seconds" in captured.out


def test_cli_invalid_input(monkeypatch, capsys):
    """Test CLI with invalid input (non-numeric)."""
    monkeypatch.setattr(sys, 'argv', ['cli.py'])

    inputs = iter(["abc", "45"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "لطفاً اعداد معتبر وارد کنید" in captured.out


def test_cli_negative_velocity(monkeypatch, capsys):
    """Test CLI with negative velocity (should error)."""
    monkeypatch.setattr(sys, 'argv', ['cli.py'])

    inputs = iter(["-5", "45"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main()

    captured = capsys.readouterr()
    assert "سرعت باید مثبت باشد" in captured.out


def test_cli_invalid_language(monkeypatch, capsys):
    """Test CLI with invalid language flag (should exit with error)."""
    monkeypatch.setattr(sys, 'argv', ['cli.py', '--lang', 'invalid'])

    # Using pytest.raises to catch SystemExit
    with pytest.raises(SystemExit) as excinfo:
        main()

    # Verify the error code and message
    assert excinfo.value.code == 2  # argparse exits with code 2 for errors

    # Capture stderr to verify the error message
    captured = capsys.readouterr()
    assert "error: argument --lang: invalid choice" in captured.err
