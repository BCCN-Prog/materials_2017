from maxima import find_maxima

def test_exercise_example_1():
    x = [1, 2, 2, 3, 1]
    result = find_maxima(x)
    correct_results = [1, 3]
    assert result == correct_results


def test_exercise_example_1():
    x = [1, 3, 2, 2, 1]
    result = find_maxima(x)
    correct_results = [1, 3]
    assert result == correct_results


def test_exercise_example_1():
    x = [3, 2, 2, 3]
    result = find_maxima(x)
    correct_results = [0, 3]
    assert result == correct_results
