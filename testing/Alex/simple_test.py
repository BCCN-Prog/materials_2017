from maxima import find_maxima

def test_exercise_example_1():
    x = [0, 1, 2, 1, 2, 1, 0]
    result = find_maxima(x)
    correct_results = [2, 4]
    assert result == correct_results

def test_exercise_example_2():
     x1 = [4, 2, 1, 3, 1, 2]
     x2 = [4, 2, 1, 3, 1, 5]
     x3 = [4, 2, 1, 3, 1]
     result1 = find_maxima(x1)
     result2 = find_maxima(x2)
     result3 = find_maxima(x3)
     correct_results1 = [0,3,5]
     correct_results2 = [0,3,5]
     correct_results3 = [0,3]
     assert result1 == correct_results1
     assert result2 == correct_results2
     assert result3 == correct_results3

def test_exercise_example_3():
    x = [1, 2, 2, 1]
    result = find_maxima(x)
    correct_results = [1, 2]
    assert result == correct_results

def test_exercise_example_4():
    x1 = [1, 2, 2, 3, 1]
    x2 = [1, 3, 2, 2, 1]
    x3 = [3, 2, 2, 3]
    result1 = find_maxima(x1)
    result2 = find_maxima(x2)
    result3 = find_maxima(x3)
    correct_results1 = [1,3]
    correct_results2 = [1,3]
    correct_results3 = [0,3]
    assert result1 == correct_results1
    assert result2 == correct_results2
    assert result3 == correct_results3
