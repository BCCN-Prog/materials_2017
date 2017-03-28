from maxima import find_maxima
import numpy as np

def test_exercise_example_1():
    x = [1, 2, 3, 4, 5]
    result = find_maxima(x)
    correct_results = [4]
    assert result == correct_results

test_exercise_example_1()
