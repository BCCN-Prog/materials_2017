from maxima import find_maxima
import numpy as np

#a)

def test_exercise_example_1():
    x = [0, 1, 2, 1, 2, 1, 0]
    result = find_maxima(x)
    correct_results = [2, 4]
    assert result == correct_results
    
def test_exercise_example_2():
    x = [-i**2 for i in range(-3, 4)]
    result = np.array(find_maxima(x))
    correct_results = np.where(x == np.max(x))
    assert result == correct_results

# def test_exercise_example_3():
#     x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
#     result = np.array(find_maxima(x))
#     correct_results = np.where(x == np.max(x))
#     assert result == correct_results
    #this example doesn't work because its hard to find the correct results for the comparison

# #b)
     
# def test_exercise_example_4():
#     x = [4, 2, 1, 3, 1 , 2]
#     result = find_maxima(x)
#     correct_results = np.where(x == np.max(x)).tolist()
#     assert result == correct_results
    
# def test_exercise_example_5():
#     x = [4, 2, 1, 3, 1, 5]
#     result = find_maxima(x)
#     correct_results = np.where(x == np.max(x)).tolist()
#     assert result == correct_results
    
# def test_exercise_example_6():
#     x = [4, 2, 1, 3, 1]
#     result = find_maxima(x)
#     correct_results = np.where(x == np.max(x)).tolist()
#     assert result == correct_results
    
# #c)
    
def test_exercise_example_7():
    x = [1,2,2,1]
    result = find_maxima(x)
    correct_results = [1,2]#np.where(x == np.max(x))
    # print(correct_results,result)
    assert result == correct_results
