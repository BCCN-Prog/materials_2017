from maxima import find_maxima
import numpy as np

def test_exercise_example_1():
    x = [0, 1, 2, 1, 2, 1, 0]
    result = find_maxima(x)
    correct_results = [2, 4]
    assert result == correct_results

def test_exercise_example_2():
    x = [-i**2 for i in range(-3, 4)]
    # x = [-9, -4, -1, 0, -1, -4, -9]
    result = find_maxima(x)
    correct_results = [3]
    assert result == correct_results

def test_exercise_example_3():
    x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    # x =
    result = find_maxima(x)
    print(result)
    correct_results = [78]
    assert result == correct_results

def test_exercise_example_4():
    x = [4, 2, 1, 3, 1, 2]
    result = find_maxima(x)
    correct_results = [0]
    assert result == correct_results
