print("hello world")

# ASSN 1.1
for i in range(3):
    print("hello Aditya!")

# adding two numbers
a = 10
b = 220
c = a + b
print(a, "+", b, "=", c)

#concatinating two strings
a = "bhagat"
b = "Singh"
c = a + " " + b
print(a, "+", b, "=", c)

#ASSN 2.1
a = 10
b = 20
c = 30
print(a, "+", b, "+", c, "=", a + b + c)

#ASSN 2.2
x = "hello"
y = "world"
z = "!"
print(x, "+", y, "+", z, "=", x + " " + y + " " + z)

#input two numbers from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = a+ b
print(a, "+", b, "=", c)

#while loop 
i = 1
while i <= 10:
    print(i)
    i += 1  

#range function
print("range(10)        -->", list(range(10)))

#for loop
for i in range(10):
    print(i)    

#printing table of 5
for i in range(1 , 11):
    print("5 *", i, "=", 5*i)

#sum of all numbers from 1 to 10
sum = 0
for i in range(1, 11):
    sum = sum + i
print("sum of all numbers from 1 to 10 is:", sum)

#ASSN 4.1
for i in range(1 , 11):
    print("7 *", i, "=", 7*i)

for i in range(1,11):
    print("9 *", i, "=", 9*i)

#ASSN 4.2
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "*", i, "=", n * i)

#ASSN 4.3
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print("sum of all numbers from 1 to", n, "is:", sum)

#input two number from user and compare them 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is less than", b)
else:
    print(a, "is equal to", b)

# check weather number is even or odd
num = int(input("Enter a number: "))    
if n% 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

#check if number is prime or not
num = int(input("Enter a number: "))
f = 0
for i in range(2 , num//2 + 1):
    if num % i == 0:
        f = 1
        break
if f == 0:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

#ASSN 5.1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 > num2 and num1 > num3:
    print(num1, "is the greatest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the greatest number")   
else:
    print(num3, "is the greatest number")

#2nd approach using max() function
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print(max(num1, num2, num3), "is the greatest number")

#ASSN 5.2 write a program to add all the numbers divisibl by 7 and 9 from 1 to n 
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    if i % 7 == 0 and i % 9 == 0:
        sum = sum + i
print("Sum of all numbers divisible by 7 and 9 from 1 to", n, "is:", sum)

#FUNCTIONS
def Add(a,b):
    c = a+b
    return c
print ("Add(10, 20) =", Add(10, 20))
print ("Add(100, 200) =", Add(100, 200))

#prime nuumber
def Isprime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return 1
print("Isprime(7) =", Isprime(7))

#Add 1 to n
def AddN(n):
    s = sum(range(n+1))
    return s
print("AddN(10) =", AddN(10))

#ASSN 6.1
def addOdd(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            sum = sum + i
    return sum
print("addOdd(10) =", addOdd(10))

import math as m 
print("math.sqrt(16) =", m.sqrt(16))
print("math.pow(2, 3) =", m.pow(2, 3))

#ASSN 6.2
import math
def prime_add(n):
    total_sum = 0
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            total_sum += num      
    return total_sum
n = int(input("Enter n: "))
print("Sum:", prime_add(n))


#Math library
import math as m
import math as m
print ("exp(-200)    --> ", m.exp(-200))  
print ("log(100,2)   --> ", m.log(100,2)) 
print ("log(100,10)  --> ", m.log(100,10))
print ("log10(100)   --> ", m.log10(100)) 
print ("m.cos(30)    --> ", m.cos(30))    
print ("m.sin(30)    --> ", m.sin(30))    
print ("m.tan(30)    --> ", m.tan(30))    
print ("m.sqrt(324)  --> ", m.sqrt(324))
print ("m.ceil(89.9) --> ", m.ceil(89.9))
print ("m.floor(89.9)--> ", m.floor(89.9))


#Strings
var = 'Hello World!'
print ("var      --> ", var)
print ("var[0]   --> ", var[0])
print ("var[1:5] --> ", var[1:5])
print ("var[:-5] --> ", var[:-5])
print ("Length --> : ", len(var))
print ("Upper  --> : ", var.upper())
print ("Lower  --> : ", var.lower())

#String formatting
name=input("Enter your name: ")
age=int(input("Enter your age : "))
price=float(input("Enter the book price: "))
s="\nYour name is %s, age is %d and book price is %f" %(name.upper(),age,price)
print (s)

#String in Triple Quotes
para_str = """This is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)

#String strip
var =" Indian   Army    "

print("String    --> ", var)
print("Length    --> ", len(var))
print("var strip --> ", var.strip())
print("Length of var after strip --> ", len(var.strip()))

print("var split --> ", var.split())
print("var split --> ", var.split(' '))
print("var split --> ", var.split(','))
print("var split --> ", var.strip().split(','))

s1="Indian Army"
s2="malayalam"
s3="madam"
s4="teacher"
print ("s1 --> ", s1==s1[::-1])
print ("s2 --> ", s2==s2[::-1])
print ("s3 --> ", s3==s3[::-1])
print ("s4 --> ", s4==s4[::-1])


#Random Numbers/String
import random as r
print (r.random())
print (r.random())
print (round(r.random(),4))


import random as r
print (r.randint(1, 100))
print (r.randint(1, 100))
print (r.randint(-10, 10))
print (r.randint(-10, 10))

import random as r
print (r.uniform(1, 100))
print (r.uniform(1, 100))
print (r.uniform (-10, 10))
print (r.uniform (-10, 10))
print (round(r.uniform (-10, 10),2))

A=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print (r.sample(A, 4))
print (r.sample(A, 2))
print (r.sample(range(0,100), 2))
print (r.sample(range(-100,100), 5))

#Generate random string
import string as s
import random as r
print ("String        --> ",s.ascii_letters)

passwd=r.sample(s.ascii_letters, 6)
print ("Selected Char --> ",passwd)

passwd1="".join(passwd)
print ("passwd1       --> ",passwd1)

passwd2="+".join(passwd)
print ("passwd2       --> ",passwd2)

passwd3="*".join(passwd)
print ("passwd3       --> ",passwd3)

#Generate random digits
import string as s
import random as r
print ("Digits --> ",s.digits)

otp=r.sample(s.digits, 5)
print ("Selected num1 --> ",otp)
otp="".join(otp)
print ("otp1          --> ",otp)

otp=r.sample(s.digits, 5)
print ("Selected num2 --> ",otp)
otp="".join(otp)
print ("otp2          --> ",otp)

otp=r.sample(s.digits, 5)
print ("Selected num2 --> ",otp)
otp="".join(otp)
print ("otp3          --> ",otp)

#Exception handaling for division by zero
for i in range(-5,6):
	try:
		print ("100/",i," --> ", 100/i)
	except:
		print ("error")

#Exception handaling for array out of index
L=[1,2,3,4,5]

for i in range(8):
	try:
		print (i," --> ",L[i])
	except:
		print ("error")

#Exception handaling for file not found
fileName=input("Enter File Name: ")
try:
	fp=open(fileName)	# Open the file in reading mode
	fp.close()
except:
	print ("Error !! \"%s\" File Not Found"%(fileName))

print ("Done")

#Data Structures 1 - list
L = ["Pratham",  'Sharma', 3.14,  3 ]
print ("Original List: ", L)
print ("Number of elements in list: ", len(L))

#List Iteration using for loop


L = ["Pratham",  'Sharma', 3.14,  3 ]
print ("Original List: ", L)
for i in range(0, len(L)):
	print (L[i])


#Adding and deleting from list
L = ["Pratham",  'Sharma', 3.14,  3 ]
print ("Original List       --> ", L)

L.append("Rahul")
print ("List After Adding   --> ", L)

del L[1]
print ("List After Deleting --> ", L)


#Sum/Average of List
L=[3, 6, 9, 12, 5, 3, 2]
print ("Original List --> ", L)

print ("Sum     --> ", sum(L))
print ("Average --> ", sum(L)/len(L))
print ("Average --> ", sum(L)//len(L))

print ("L * 3   --> ", L * 3)     # Every element get tripled
print ("L + L   --> ", L + L)     # Every element get doubled


#Min/Max/Sort the list
print ("Original List --> ", L)

print ("max --> ", max(L))
print ("min --> ", min(L))

print ("\nBefore Sort            --> ", L)
L.sort()

print ("After Sort (Asending)  --> ", L)

L.sort(reverse=True)
print ("After Sort (Desending) --> ", L)

#Data Structures 2 - Dictionary

CGPA={1:8.9, 2:5.6, 4:6.7, 7:9.1, 8:5.3}
print ("Dictionary      --> ", CGPA)
print ("Num of elements --> ", len(CGPA))

print ("CGPA of 1       --> ", CGPA[1])
print ("CGPA of 4       --> ", CGPA[4])
print ("CGPA of 7       --> ", CGPA[7])
print ("CGPA of 3       --> ", CGPA[3])

#traverse dictionary
CGPA={1:8.9, 2:5.6, 4:6.7, 7:9.1, 8:5.3}
for k in CGPA:
	print ("CGPA of ", k, " --> ", CGPA[k])


#Updating, Adding and Deleting from Dictionary
CGPA={1:8.9,2:5.6,4:6.7,7:9.1,8:5.3}
print ("Original Dictionary --> ", CGPA)
CGPA[4] = 9.2
print ("After Updating (4)  --> ", CGPA)
CGPA[3] = 8.6
print ("After Adding (3)    --> ", CGPA)
del CGPA[1]
print ("After Deleting (1)  --> ", CGPA)
CGPA.clear()
print ("After Clear         --> ", CGPA)
del CGPA
print ("After Delete        --> ", CGPA)

#data structures 3 - Tuple
T = ("Pratham", 'Sharma', 3.14, 3)

print ("T               -->", T)
print ("Num of elements -->", len(T))
print ("Type of Object  -->", type(T))

# Method 2
T = tuple(["Pratham", 'Sharma', 3.14, 3])   # Convert list to tuple
#T = tuple(("Pratham", 'Sharma', 3.14, 3))  # Also Works


#Accessing/Selecting in Tuple
T = (3, 6, 9, 12, 5, 3, 2)
print ("T     -->", T)

print ("T[1]  -->", T[1])
print ("T[2]  -->", T[2])
print ("T[-1] -->", T[-1])
print ("T[-2] -->", T[-2])


#Merging part of Tuples
T1 = (3, 6, 9)
T2 = (12, 5, 3, 2)

print ("T1 -->", T1)
print ("T2 -->", T2)

T3 = T1[1:2] + T2[1:3]
print ("T3 -->", T3)

T4 = T1[:-2] + T2[:-3]
print ("T4 -->", T4)

#Adding element to Tuple - (Jugaad)
T = ("Pratham", 'Sharma', 3.14, 3)
print ("T         -->", T)
T1 = list(T)
T1.append(9.8)
T = tuple(T1)
print ("After Add -->", T)

#Inserting element in Tuple - (Jugaad)
T = ("Pratham", 'Sharma', 3.14, 3)
print ("T            -->", T)

T1 = list(T)
T1.insert(2, "Rahul")
T = tuple(T1)
print ("After Insert -->", T)

#Data Structure 4 - Set
s = set(['A', 'B', 'E', 'F','E', 'F' ])
print ("Original set           --> ", s)
print ("Num of elements in set --> ", len(s))

#Opertions on Sets
a = set(['A', 'B', 'E', 'F' ])
b = set(["A", "C", "D", "E"])
print ("Original set a      --> ", a)
print ("Original set b      --> ", b)
print ("Union of a and b    --> ", a.union(b))
print ("Intersection of a,b --> ", a.intersection(b))
print ("Difference a - b    --> ", a - b)
print ("Difference a - b    --> ", a.difference(b))
print ("Difference b - a    --> ", b - a)
print ("Difference b - a    --> ", b.difference(a))
print ("Symetric Diff a - b --> ", a.symmetric_difference(b))
print ("Symetric Diff b - a --> ", b.symmetric_difference(a))


#Add, delete, pop element from set
a = set(['A', 'B', 'E', 'F' ])
print ("Original set a       --> ", a)
a.add("D")
print ("Set After Adding (D) --> ", a)
a.add("D")
print ("Set After Adding (D) --> ", a)
a.remove("D")
print ("Set After Deleting(D)--> ", a)
a.pop()
print ("Set After pop        --> ", a)
a.pop()
print ("Set After pop        --> ", a)

#Command Line Argument
import sys
print (sys.argv)
a = int(sys.argv[1]) 	# First Number
b = int(sys.argv[2])	# Second Number
c = a + b
print (a, " + ", b, " --> ", c)

#File Handling
fp=open('result.txt','w')	# Open the file in writing mode
for  i in range(1,11):
	fp.write(str(i) + "\n")	# Writing to the file line by line
fp.close()

print ("Writing done !! \nOpen result.txt to view the content")

#Read a file and print its content
fp=open('result.txt')		# Open the file in reading mode
for line in fp: 		    # print line by line
	print (line.strip())
fp.close()

#Read from one file, Convert it to upper case and write to other file
Readfp=open('result.txt')		# Open the file in reading mode
Writefp=open('abc.txt','w')	# Open the file in writing mode
for line in Readfp:
	Writefp.write(line.upper())

Writefp.close()
Readfp.close()

print ("Writing done !! \nOpen result.txt to view the content")