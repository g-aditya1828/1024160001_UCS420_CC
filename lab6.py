import numpy as np

#Ques 1
temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40]) 
#a)  Add 2°C to every reading using vectorization.
print(temperature + 2)

#b)  Convert the temperature readings from Celsius to Fahrenheit.
print(temperature * 9/5 + 32)

#c) Identify all readings greater than 32°C using Boolean indexing.
print(temperature[temperature > 32])

#d) Count how many readings exceed 32°C. 
print(np.sum(temperature > 32))

#e) Explain how vectorization and Boolean indexing can make data processing more efficient than explicitly iterating through every value. 


#Ques 2
steps = np.array([ [5000, 6200, 7100], [8000, 7500, 9000], [4500, 5100, 4800], [9000, 8500, 9500]]) 

#a) Calculate the total steps recorded.
print(np.sum(steps))

#b) Calculate the mean of steps
print(np.mean(steps))

#c) Find the maximum and minimum values.
print(np.max(steps))
print(np.min(steps))

#d) Calculate the total steps for each day using axis=0.
print(np.sum(steps, axis=0))

#e) Calculate the total steps for each user using axis=1
print(np.sum(steps, axis=1))

#f) Find the user/day position containing the maximum number of steps using argmax(). 
print(np.unravel_index(np.argmax(steps), steps.shape))

#ques 3
#a) Create the numPy array
original = np.array([1, 2, 3, 4, 5, 6]) 

#b) Create a slice containing elements from index 1 to 4 and store it in a variable named subset. 
subset = original[1:5]
print(subset)

#c) . Modify the first element of subset to 999 and display both original and subset. 
subset[0] = 999
print("Original array:", original)
print("Subset array:", subset)

#d)  Create another slice from original, but this time use .copy(). Modify its first element to 500 and display original and the copied array. 
copied_subset = original[1:5].copy()
copied_subset[0] = 500
print("Original array after copy modification:", original)
print("Copied array:", copied_subset)

#e) Create a NumPy array containing the numbers from 1 to 12 using np.arange() and reshape it into a 3 × 4 matrix. 
matrix = np.arange(1, 13).reshape(3, 4)
print("Matrix:" , matrix)

#f) f. From the 3 × 4 matrix, extract the following using NumPy indexing and slicing:
# • First row  
# • Last row  
# • Second column  
# • Elements from rows 1–2 and columns 2–3 

