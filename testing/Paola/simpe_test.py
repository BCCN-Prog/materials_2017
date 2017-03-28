from maxima import find_maxima

def test_exercise_example_1():
    x = [0, 1, 2, 1, 2, 1, 0]
    result = find_maxima(x)
    correct_results = [2, 4]
    assert result == correct_results
