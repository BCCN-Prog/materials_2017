from maxima import find_maxima

def test_exercise_example_1():
    x = [1, 2, 2, 1]
    result = find_maxima(x)
    correct_results = [1, 2]
    assert result == correct_results, "Incorrect result"

test_exercise_example_1()
