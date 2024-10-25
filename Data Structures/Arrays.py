
# Creating a list of fruits
from array import array
import numpy as np
fruits = ["apple", "banana", "cherry"]
my_list = [1, "Hello", 3.5]  # A list with an integer, a string, and a float


#1.Creating python arrays
my_array = array("i",[1,2,3,4,5]) #"i means data type integer"
#numpy arrays
my_Array = np.array([1,2,3,4]) #creating one dimension array;
matrix = np.array([[1,2,3,4], [4,5,6,7]]) #2x4 matrix (2 rows ,3 columns)
print(matrix)

#2.Array properties and attributes
print(my_Array.shape) #Prints tells you the dimensions of the array, will print (4,) meaning four columns
print(my_Array.size) #Tells the total number of elements in an array
print(my_Array.dtype) #integers , floating int64 float64
print(matrix.ndim) #prints the dimension 2,


#3.Basic array operations
#element wise operators
new_array = my_Array + 5 # Adds 5 to each element in my_Array array
print(new_array)

#aggregate functions
print(np.sum(my_array)) # sum
print(np.mean(my_array)) #mean
print(np.max(my_array)) #max value
print(np.min(my_array)) #minimum value


#4.Multidimensional arrays
multi_array = np.array ([[1,2,3,4],[5,6,7,8], [9,10,11,12]])
#accessing elements
print(multi_array[1,3])

#slicing and indexing
print(multi_array[0:2,1:3])
#5.Advanced array manipulations
#6.Broadcasting
#7.Commonly used numpy functions





