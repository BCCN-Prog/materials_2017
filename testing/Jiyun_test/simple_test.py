from maxima import find_maxima

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
