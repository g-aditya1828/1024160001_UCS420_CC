import numpy as np

#Ques 1
a = np.array([1,2,3,4,5])
#a) Addition of 2 in all the element  
print(a + 2 )

#b) Multiplication of 3 in all the element
print(a * 3)

#c Divide all the element by 2
print(a / 2)

#ques 2
arr = np.array([1, 2, 3, 6, 4, 5])

#a) Reverse the Numpy array
print(arr[::-1])

#b) Find the most frequent value and their indice(s) in the following arrays: 
x = np.array([1,2,3,4,5,1,2,1,1,1]) 
print(np.bincount(x).argmax())
print(np.where(x == np.bincount(x).argmax()))
print(np.bincount(x))

y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3 ])
print(np.bincount(y).argmax())
print(np.where(y == np.bincount(y).argmax()))   

#Ques 3 For the given 2-D array access elements using row and column indices as follows:
# a) Access 1st row, 2nd column 
arr=np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
x = arr[0, 1]
print(x)
#b) Access 3rd row, 1st column
y = arr[2, 0]
print(y)

#ques 4
Adi = np.linspace(10, 100, 25) 
print(Adi)
print(Adi.ndim)
print(Adi.shape)
print(Adi.size)
print(Adi.dtype)
print(Adi.nbytes)
#transpose
print(Adi.T)

#ques 5

ucs420_adi = np.array([[10,20,30,40],[50,60,70,80],[90,15,20,35]])
print(ucs420_adi.mean())
print(ucs420_adi.median())
print(ucs420_adi.max())
print(ucs420_adi.min())
print(ucs420_adi.unique())

reshaped_ucs420_adi = ucs420_adi.reshape(4,3)
print(reshaped_ucs420_adi)

resize_ucs420_adi = np.resize(ucs420_adi, (2,6))
print(resize_ucs420_adi)