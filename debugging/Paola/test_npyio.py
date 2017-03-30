from numpy.testing import assert_, assert_raises
from numpy import genfromtxt
from io import BytesIO

class TestGenfromtxt:
    def test_genfromtxt_1number(self):
        data = b"1"
        myfile = genfromtxt(BytesIO(data), delimiter=",")
        shape = myfile.shape
        correct_shape = (1)  
        assert_(shape == correct_shape)
            #print("Incorrect shape for one number: "+str(shape))
        
    def test_genfromtxt_1d(self):
        data = b"1, 2, 3, 4"
        myfile = genfromtxt(BytesIO(data), delimiter=",")
        shape = myfile.shape
        correct_shape = (1, 4)
        assert_(shape == correct_shape) 
            #print("Incorrect shape for one-dimensional array: "+str(shape))
        
        
    def test_genfromtxt_2d(self):
        data = b"1, 2, 3, 4\n 5, 6, 7, 8"
        myfile = genfromtxt(BytesIO(data), delimiter=",")
        shape = myfile.shape
        correct_shape = (2, 4)
        assert_(shape == correct_shape)
            #print("Incorrect shape for two-dimensional array: "+str(shape))
   
#TestGenfromtxt.test_genfromtxt_1number() 
#TestGenfromtxt.test_genfromtxt_1d()
#TestGenfromtxt.test_genfromtxt_2d()

