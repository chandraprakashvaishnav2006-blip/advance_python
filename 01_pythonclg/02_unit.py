"""
UNIT 2 - CONTROL STATEMENTS
1. CONDITIONAL STATEMENTS
 (A) IF
 (B) ELSE
 (c) ELIF
2. ITERATIVE STATEMENTS
 (A)FOR
 (B)WHILE
 NOTE: A DO-WHILE LOOP IS NOT SUPPORTED IN PYTHON.
3. TRANSFER STATEMENTS
 (A)BREAK
 (B)CONTINUE
 (C)PASS


 del keyword:
 it is used to delete a variable, item, or attribute
  
None:
it represents the absence of a value; it is not used to delete something

string:
a sequence of character within single or double quote 

Note:In most of other languages like C, C++, Java, a single character with in single quotes is treated as char data type value.
But in Python weare not having char data type. Hence it is treated as String only. 

indexing:
it is a method to access character of strings 


Accessing Characters by using Slice Operator: 
• Syntax:s[begin index:end index:step] 
• Begin Index: From where we have to consider slice(substring) 
• End Index: We have to terminate the slice(substring)at end index-1 
• Step: Incremented Value. 

Note: •If weare not specifying bEgin index then it will consider from beginning ofthe string. 
• If weare not specifying end index then it will consider up to end ofthe string. 
• The default value for step is 1. 

index(): index()method is exactly same as find()method except that if the specified substring is not available then we will get Value Error. 

To Check Typeof Characters Present ina String: 
Python contains the following methods for this purpose.  
1) isalnum():Returns True if all characters are alphanumeric(ato z, Ato Z,0 to 9 ) 
2) isalpha():Returns True if all characters are only alphabet symbols(at oz, At oZ) 
3) isdigit(): Returns True if all characters are digits only(0 to 9) 
4) islower():Returns True if all characters are lowercase alphabet symbols
 5) isupper():Returns True if all characters are uppercase apl ha bet symbols 
 6) istitle(): Returns True if string is in title case
 7) isspace():Returns True if string contains only spaces 

"""
# EXAMPLE OF IF/ELSE
# name = input("Enter your name: ")
# b=name.lower()
# if b== "abhi":
#     print("hello abhi")
# else:
#     print("hello guest")

# # biggest of 3 no
# n1=int(input("enter 1st no "))
# n2=int(input("enter 2nd no "))
# n3=int(input("enter 3rd no "))
# if n1>=n2 and n1>=n3:
#     print("n1 is biggest")
# elif n2>=n1 and n2>=n3:
#     print("n2 is biggest")
# else:
#     print(f"n3={n3} is biggest")

# for loop 
# n=int(input("enter a no "))
# for i in range(1,n+1):
#     print(i)

#  for loop
# z= "makhmal zoorawar"
# for i in z:
#     print(i,end=" ")

# to find no of letters in word
# a=input("enter a word :")
# c=0
# for i in a:
#     print(i,end="")
#     c+=1
# print()    
# print(f"no of letters is {c} ")
# print(len(a))

# while loop 
# i=0
# while i<=10:
#     print(i)
#     i=i+1

# for i in range(0,4):
#     for k in range (0,i):
#             print(" ",end="")    
#     for j in range(0,4):
#          print("*",end=" ")
#     print()     
       
    
# f=open("astra.txt",'r')
# content=f.read()
# print(content)
# f.close()

# import pickle

# student = {"name": "Rahul", "age": 20, "marks": 85}

# # Pickling: Save the object to a file
# with open("student.pkl", "wb") as file:
#     pickle.dump(student, file)

# print("Object saved successfully!")

# import pickle

# # Unpickling: Read the object from the file
# with open("student.pkl", "rb") as file:
#     data = pickle.load(file)

# print(data)

# import random as r
# print(r.uniform(5,7))


# class a:
#     def god(self):
#         print("hello cp papa")
# class b(a):
#     def god(self):
#         super().god()
#         print("lalita")     
# e=b()        
# e.god()


# class Student:
#     def __init__(self, marks):
#         self.marks = marks

#     def __add__(self, other):
#         return self.marks + other.marks

# s1 = Student(80)
# s2 = Student(90)

# print(s1 + s2)

# import numpy as np
# a=np.array([[1,2,3],[4,5,6]])
# print(a.ndim)
# b=np.sum(a)
# c=np.average(a)
# d=np.arrange(a)
# print(b)
# print(c)
# print(d)        
# for x in a :
#     for y in x:
#         print(y)


# for x in np.nditer(a):
#         print (x)

# for x in np.nditer(a, order='C'):
#         print(x)



# from abc import ABC, abstractmethod

# # Abstract class
# class Animal(ABC):

#     # Abstract method
#     @abstractmethod
#     def sound(self):
#         pass

# # Child class
# class Dog(Animal):

#     # Implementing the abstract method
#     def sound(self):
#         print("Dog barks")

# # Creating an object
# d = Dog()
# d.sound()


try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

print("Program continues")