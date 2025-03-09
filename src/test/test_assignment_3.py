import pytest
from main.assignment_3 import euler_method, runge_kutta, f

def test_euler_method():
    _, result = euler_method(f, 0, 1, 2, 10)
    assert abs(result - 1.2446380979332121) < 1e-6

def test_runge_kutta():
    _, result = runge_kutta(f, 0, 1, 2, 10)
    assert abs(result - 1.251316587879806) < 1e-6

pytest.main()