'''
Sample Python code to check Python style
'''

def my_func ( x ):
    '''
    Creates a list of integers up to x.
    '''

    return [i for i in range(x)]

def another_func(y):
    '''
    Creates an np array of integers up to y.
    '''
    import numpy as np

    return np.array(my_func(y))

