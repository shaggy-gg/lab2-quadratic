import sys
import os

# Добавляем src в путь импорта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from quadratic import solve_quadratic


def test_two_roots():
    """D > 0: два вещественных корня."""
    roots = solve_quadratic(1, -5, 6)
    assert len(roots) == 2
    assert abs(roots[0] - 3.0) < 1e-9
    assert abs(roots[1] - 2.0) < 1e-9
    print("test_two_roots: PASSED")


def test_one_root():
    """D = 0: один кратный корень."""
    roots = solve_quadratic(1, -2, 1)
    assert len(roots) == 1
    assert abs(roots[0] - 1.0) < 1e-9
    print("test_one_root: PASSED")


def test_no_roots():
    """D < 0: нет вещественных корней."""
    roots = solve_quadratic(1, 0, 1)
    assert len(roots) == 0
    print("test_no_roots: PASSED")


def test_invalid_a():
    """a = 0: должно вызывать ValueError."""
    try:
        solve_quadratic(0, 1, 1)
        print("test_invalid_a: FAILED (исключение не вызвано)")
    except ValueError:
        print("test_invalid_a: PASSED")


if __name__ == "__main__":
    test_two_roots()
    test_one_root()
    test_no_roots()
    test_invalid_a()
    print("\nВсе тесты пройдены.")
