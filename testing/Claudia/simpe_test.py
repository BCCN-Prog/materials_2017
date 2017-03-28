from maxima import find_maxima
import numpy as np


## standard examples
def test_exercise_example_1():
    x = [0, 1, 2, 1, 2, 1, 0]
    result = find_maxima(x)
    correct_results = [2, 4]
    assert result == correct_results
    
def test_exercise_example_2():
    x = [-i**2 for i in range(-3, 4)]
    result = find_maxima(x)
    correct_results = [3]
    assert result == correct_results
    
def test_exercise_example_3():
    x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    result = find_maxima(x)
    correct_results = [16, 78]
    assert result == correct_results
    
# peaks at the borders    
def test_exercise_example_4():
    x = [4, 2, 1, 3, 1, 2]
    result = find_maxima(x)
    correct_results = [0, 3, 5]
    assert result == correct_results
    
def test_exercise_example_5():
    x = [4, 2, 1, 3, 1, 5]
    result = find_maxima(x)
    correct_results = [0, 3, 5]
    assert result == correct_results
    
def test_exercise_example_6():
    x = [4, 2, 1, 3, 1]
    result = find_maxima(x)
    correct_results = [0, 3]
    assert result == correct_results
    
## multiple adjacent peaks        
def test_exercise_example_7():
    x = [1, 2, 2, 1]
    result = find_maxima(x)
    correct_results = [1, 2]
    assert result == correct_results
    
def test_exercise_example_8():
    x = [1, 2, 2, 3, 1]
    result = find_maxima(x)
    correct_results = [1, 3]
    assert result == correct_results
    
def test_exercise_example_9():
    x = [1, 3, 2, 2, 1]
    result = find_maxima(x)
    correct_results = [1, 3]
    assert result == correct_results
    
def test_exercise_example_10():
    x = [3, 2, 2, 3]
    result = find_maxima(x)
    correct_results = [0, 3]
    assert result == correct_results
    
    
    
    


    
    
    




 


