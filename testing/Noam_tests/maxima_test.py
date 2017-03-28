#import pdb
import numpy as np
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

    localmax = []
    idx = []
    for i in range(len(x)):
        #pdb.set_trace()
        # `i` is a local maximum if the signal decreases before and after it
        if x[i-1] < x[i] and x[i+1] < x[i]:
            #idx.append(i)
            localmax.append(x[i])
            localmax.sort()
            if len(localmax) == 1:
                m= x.index(localmax[localmax])
            else:
                m=  x.index(localmax[len(localmax)-1])

    return m
    #return idx

    # NOTE for the curious: the code above could be written using
    # list comprehension as
    # return [i for i in range(len(x)) if x[i-1]<x[i] and x[i+1]<x[i]]
    # not that this would solve the bugs ;-)
