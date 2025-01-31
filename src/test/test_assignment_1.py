import pytest
from main.assignment_1 import approximation_algorithm, bisection_method, fixed_point_iteration, newton_raphson_method

def test_approximation_algorithm():
    iterations, final_count = approximation_algorithm()
    assert final_count == 4
    expected_values = [1.5, 1.4166666666666665, 1.4142156862745097, 1.4142135623746899, 1.414213562373095]
    assert [val[1] for val in iterations] == expected_values

def test_bisection_method():
    iterations, root, count = bisection_method()
    assert count == 17
    assert abs(root - 1.3653030395507812) < 0.0001

def test_fixed_point_iteration():
    iterations, result, count = fixed_point_iteration()
    assert result == "Success"
    assert count == 20
    assert abs(iterations[-1][1] - 1.3652302361581812) < 0.000001

def test_newton_raphson_method():
    iterations, root, count = newton_raphson_method()
    assert count == 4
    assert abs(root - 1.3652300134353668) < 0.0001

pytest.main()