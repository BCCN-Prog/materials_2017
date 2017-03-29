from maxima import find_maxima
import numpy as np

<<<<<<< HEAD
#def test_exercise_example_1():
    x = [0, 1, 2, 1, 2, 1, 0]
=======
def test_exercise_example_1():
    x = [4,2,1,3,1,2]
>>>>>>> 007ed11a2f2d80a240aa9aa307f06e0c4eafc0cd
    result = find_maxima(x)
    correct_results = [2, 4]
    assert result == correct_results

#def test_exercise_example_2():
    x = [-i**2 for i in range(-3, 4)]
    # (-9, -4, -1, -0, -1, -4)
    correct_results=[3]
    assert result == correct_results

def test_exercise_example_3():
    x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    # y[78]
    result = find_maxima(x)
    correct_results= [16,78]
    assert result == correct_results

def test_exercise_example_4():
    x= [4,2,1,3,1,2]
    result = find_maxima(x)
    correct_results= [0,3,5]
    assert result == correct_results
