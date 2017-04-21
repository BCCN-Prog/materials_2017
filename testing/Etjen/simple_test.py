from maxima import find_maxima
import numpy as np
import pdb 

def test_exercise_example_1():
    x = [0, 1, 2, 1, 2, 1, 0]
    result = find_maxima(x)
    correct_results = [2, 4]
    assert result == correct_results
    print(result)
    print(correct_results)

test_exercise_example_1()

def test_exercise_example_2():
    x = [-i**2 for i in range(-3, 4)]
    result = np.array(find_maxima(x))
    correct_results = np.where(x == np.max(x))
    assert result == correct_results
    
test_exercise_example_2()

def test_exercise_example_3():
    x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    result = find_maxima(x)
    correct_results = [16, 78]
    pdb.set_trace()
    assert result == correct_results.any()
    
test_exercise_example_3()
