import pdb
def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """

    if type(x) != type([]):
        message = 'Input argument must be a list, got %d instead' % type(x)
        raise TypeError(message)

    idx=[]
    import pdb;pdb.set_trace()
    for i in range(len(x)):
        if i==0 and x[i] > x[i+1]:
            idx.append(i)

        elif i==len(x)-1 and x[i] > x[i-1]:
            idx.append(i)

        elif i<len(x)-1 and  (x[i-1] <= x[i]) and (x[i+1] <= x[i]):
            idx.append(i)

    return idx

    # NOTE for the curious: the code above could be written using
    # list comprehension as
    # return [i for i in range(len(x)) if x[i-1]<x[i] and x[i+1]<x[i]]
    # not that this would solve the bugs ;-)

print(find_maxima([1,2,2,3,1]))
