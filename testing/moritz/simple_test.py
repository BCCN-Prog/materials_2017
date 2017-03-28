from maxima import find_maxima

def test_exercise_example_1():
    x = [1, 2, 2, 3, 1]
    correct_results = [1, 3]
    assert find_maxima(x) == correct_results


def test_exercise_example_2():#
    x = [1, 3, 2, 2, 1]
    correct_results = [1, 3]
    assert find_maxima(x) == correct_results

def test_exercise_example_3():
    x = [3, 2, 2, 3]
    correct_results = [0, 3]
    assert find_maxima(x) == correct_results


def test_exercise_example_4():
    x = [-i**2 for i in range(-3, 4)]
    correct_results = [ 3]
    assert find_maxima(x) == correct_results
