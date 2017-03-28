from maxima import find_maxima
import numpy as np

def test_exercise_example_1():
    x = [0, 1, 2, 1, 2, 1, 0]
    result = find_maxima(x)
    correct_results = [2, 4]
    
    assert result == correct_results


def test_exercise_example_2():

    x = [4, 2, 1, 3, 1, 2]

    result = find_maxima(x)
    correct_results = [0,3,5]
    assert result == correct_results

     


def test_exercise_example_3():

    x = [4, 2, 1, 3, 1, 5]

    result = find_maxima(x)
    correct_results = [0,3,5]
    assert result == correct_results



def test_exercise_example_4():

    x = [4, 2, 1, 3, 1]
    result = find_maxima(x)
    correct_results = [0,3]
    print (result)
    assert result == correct_results



def test_exercise_example_5():

    x = [1, 2, 2, 1]

    result = find_maxima(x)
    correct_results = [1,2]
    print (result)
    assert result == correct_results

def test_exercise_example_6():


    x = [1, 2, 2, 3, 1]
    result = find_maxima(x)
    correct_results = [1,3]
    print (result)
    assert result == correct_results

def test_exercise_example_7():


    x = [1, 3, 2, 2, 1]
    result = find_maxima(x)
    correct_results = [1,3]
    print (result)
    assert result == correct_results

def test_exercise_example_8():


    x = [3, 2, 2, 3]
    result = find_maxima(x)
    correct_results = [0,3]
    print (result)
    assert result == correct_results


    

test_exercise_example_1()
test_exercise_example_2()
test_exercise_example_3()
test_exercise_example_4()
test_exercise_example_5()
test_exercise_example_6()
test_exercise_example_7()
test_exercise_example_8()
