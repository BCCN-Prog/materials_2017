from maxima import find_maxima
import numpy as np
import pdb

def test_exercise_example_1():
    #x = [0, 1, 2, 1, 2, 1, 0]
    #x = [-i**2 for i in range(-3, 4)]
    x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    result = find_maxima(x)
    #correct_results = [2, 4]
    #correct_results = [3]
    correct_results = [78]

    assert result == correct_results
    print(result)

test_exercise_example_1()

