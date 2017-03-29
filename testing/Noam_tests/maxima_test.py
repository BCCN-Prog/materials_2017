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



    idx = []
    for i in range(len(x)):
        #pdb.set_trace()
        # `i` is a local maximum if the signal decreases before and after it
        if i == 0 and x[i]>x[i+1]:
            idx.append(i)
        elif i == (len(x)-1) and x[i-1] < x[i]:
            idx.append(i)
        elif x[i-1] < x[i] and x[i+1] < x[i]:
            idx.append(i)

    return idx

x= [4,2,1,3,1,2]
print (find_maxima(x))
