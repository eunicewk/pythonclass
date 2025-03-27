import numpy as np

''' 
NumPy (Numerical Python) is an open source Python library thats widely used in science and engineering.
The NumPy library contains multidimensional array data structures, such as the homogeneous, N-dimensional ndarray, 
and a large library of functions that operate efficiently on these data structures. 
'''

#creating a numpy array
np_array = np.array([5,2,7,1,8,6,3,4])

#accessing integers using their index
print(np_array[0])

#sorting using the in-built method sort()
np_array.sort()
print(np_array)

#slicing elements the result includes the start index but excludes the end index
print(np_array[3:6])