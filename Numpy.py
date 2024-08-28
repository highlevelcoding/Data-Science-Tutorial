import numpy as np
a=np.array(24)
b=np.array([1,2,3])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(type(a))
print("zero dimension")
print('a:\n{}'.format(a))
print("one dimension")
print('b:\n{}'.format(b))
print("two dimension")
print('c:\n{}'.format(c))
print("three dimension")
print('d:\n{}'.format(d))
for i in np.nditer(c,order="F"):
    print(i)
n=b"Welcome to python"
np.frombuffer(n,dtype="S1",count=-1,offset=0)

#Multiplication using numpy
import numpy as np
a1=np.array([[1,2,3],[4,5,6],[7,8,9]])
a2=np.array([[9,8,7],[6,5,4],[3,2,1]])
result1=np.multiply(a1,a2)
print("Element wise multiplication:\n")
print(result1)
print(result.shape)
result2=np.matmul(a1,a2)
print("Matrix multiplication:\n")
print(result2)

import numpy as np
a1=np.array([[1,2,3],[4,5,6]])
a2=np.array([[9,8,7],[6,5,4]])
print(a1.reshape(3,2))

import numpy as np
a=np.eye(4,dtype="int")
print(a)

import numpy as np
a=np.zeros((3,3),dtype="int")
print(a)

import numpy as np
a=np.ones((3,3),dtype="int")
print(a)

array7=np.transpose(a)
print(array7)


import numpy as np
a=np.full((3,3),10)
print(a)

#Arthematic operations using numpy
import numpy as np
first_array=np.array([1,3,5,7])
second_array=np.array([2,4,6,8])
result1=first_array+second_array
print("Using the + operator:",result1)
result2=np.add(first_array,second_array)
print("Using the add() function:",result2)

result3=first_array-second_array
print("Using the - operator:",result3)
result4=np.subtract(first_array,second_array)
print("Using the subtract() function:",result4)

result5=first_array*second_array
print("Using the * operator:",result5)
result6=np.multiply(first_array,second_array)
print("Using the multiply() function:",result6)

result7=first_array/second_array
print("Using the / operator:",result7)
result8=np.divide(first_array,second_array)
print("Using the divide() function:",result8)

array1=np.array([1,3,5,7])
result9=array1**2
print("Using the ** operator:",result9)
result10=np.power(array1,2)
print("Using the power() function:",result10)

first_array=np.array([1,3,5,7])
second_array=np.array([2,4,6,8])
r1=first_array%second_array
print("Using the % operator:",r1)
r2=np.mod(first_array,second_array)
print("Using the mod() function:",r2)


import numpy as np
array1=np.array([1,3,5])
print("np.array():\n",array1)


#statistical operations using numpy
marks=np.array([76,78,81,66,85])
mean_marks=np.mean(marks)
print("mean:",mean_marks)

median_marks=np.median(marks)
print("median:",median_marks)

min_marks=np.min(marks)
print("min:",min_marks)

max_marks=np.max(marks)
print("max:",max_marks)


#logical opertors
import numpy as np
array1=np.array([1,2,3])
array2=np.array([3,2,1])
result1=array1<array2
print(result1)

result2=array1>array2
print(result2)

result3=array1==array2
print(result3)

result4=np.less(array1,array2)
print(result4)

result5=np.less_equal(array1,array2)
print(result5)

result6=np.greater(array1,array2)
print(result6)

result7=np.greater_equal(array1,array2)
print(result7)

result8=np.not_equal(array1,array2)
print(result8)

#Rounding function
numbers=np.array([1.23456,2.34567,3.45678,4.56789])
round_array=np.round(numbers,2)
print(round_array)

array1=np.array([1.23456,2.34567,3.45678,4.56789])
print("Array after floor():",np.floor(array1))
print("Array after ceil():",np.ceil(array1))


#2d array
array1=np.array([[2,4,6],[8,10,12],[14,16,18]])
result1=np.median(array1,axis=1)
print("Median  along horizontal axis:",result1)
result2=np.median(array1,axis=0)
print("Median  along vertical axis:",result2)
result3=np.median(array1)
print("Median  along entire array:",result3)

#standard deviation
array1=np.array([[2,5,9],[3,8,11],[4,6,7]])
result1=np.std(array1,axis=1)
print("std along horizontal axis:",result1)
result2=np.std(array1,axis=0)
print("std  along vertical axis:",result2)
result3=np.std(array1)
print("std  along entire array:",result3)

#string function in arrays
array1=np.array(["iphone:","price:"])
array2=np.array(["15","$900"])
#element-wise concatenation
result=np.char.add(array1,array2)
print(result)


array1=(['A','B','C'])
result=np.char.multiply(array1,2)
print(result)

array1=np.array(['eric','paul','sean'])
result=np.char.capitalize(array1)
print(result)

array1=np.array(['nEpalI','AmeriCAN','CaNaDiAn'])
result=np.char.upper(array1)
print(result)

array1=np.array(['nEpalI','AmeriCAN','CaNaDiAn'])
result=np.char.lower(array1)
print(result)

array1=(['c','python','swift'])
array2=(['c++','python','java'])
result=np.char.equal(array1,array2)
print(result)


array1=(['c','python','swift'])
array2=(['c++','python','java'])
result=np.char.not_equal(array1,array2)
print(result)

#array indexing
arr=np.array([1,2,3,4])
print("first element in array",arr[0])
print("sum of last two digits",arr[2]+arr[3])

arr=np.array([1,2,3,4,5,6,7])
print("slicing the elements from 1to 4",arr[1:5])
print("slicing the elements from 4 to end",arr[4:])
print("slicing the elements from start to 3",arr[:4])
