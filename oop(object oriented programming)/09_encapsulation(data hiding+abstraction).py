# ENCAPSULATION:
# THE PROCESS OF BINDING DATA MEMBERS AND METHODSS TOGETHER INTO A SINGLE UNIT IS KNOWN
# AS ENCAPSULATION. IT IS ONE OF THE FUNDAMENTAL CONCEPTS OF OBJECT ORIENTED PROGRAMMING. 
# IT IS USED TO HIDE THE INTERNAL REPRESENTATION, OR STATE, OF AN OBJECT FROM THE OUTSIDE. 
# THIS IS ACHIEVED BY MAKING THE DATA MEMBERS PRIVATE AND PROVIDING PUBLIC METHODS TO ACCESS AND MODIFY THEM.

# PYTHON CLASS IS AN GOOD EXAMPLE OF ENCAPSULATION. 
# IN PYTHON, WE CAN MAKE DATA MEMBERS PRIVATE BY PREFIXING THEM WITH TWO UNDERSCORES (__).


# IF ANY COMPONENT FOLLOWS DATA HIDING AND ABSTRACTIONN SUCH TYPE OF COMPONENT IS KNOWN AS ENCAPSULATED
# COMPONENT. ENCAPSULATION IS USED TO HIDE THE INTERNAL REPRESENTATION, OR STATE, OF AN OBJECT FROM THE OUTSIDE.

# DATA HIDING : BY DEFAULT ANY METHOD OR VARIABLE IN A CLASS IS PUBLIC . IT MEANS WE CAN ACCESS THEM
# IT WITHIN AND OUTSIDE OF THE CLASS. BUT IF WE WANT TO HIDE ANY METHOD OR VARIABLE FROM OUTSIDE OF THE CLASS
# THEN WE CAN DECLARE THAT METHOD OR VARIABLE AS PRIVATE. IN PYTHON, WE CAN MAKE DATA MEMBERS PRIVATE BY 
# PREFIXING THEM WITH TWO UNDERSCORES (__).

# class test:
#     def __init__(self):
#         self.__a=10  # private variable
#     def __get(self):
#         print(self.__a ) # public method to access private variable
# t=test()  
# # print(t._test__get())  # 10
# t._test__get()


# NAME MANGLING: TO ACCESS PRIVATE VARIABLES AND METHODS OUTSIDE OF THE CLASS, 
# WE CAN USE NAME MANGLING. EXAMPLE :  T._TEST__GET()



# ABSTRACTION: IT MEANS INCOMPLETE 

# ABSTRACTION METHOD:
# IT HAS ONLY DECLARATION BUT NOT BODY.
# IN CHILD CLASS THESE METHODS ARE REQUIRED TO IMPLEMENT 
# WE SHOULD USE @ ABSTRACT METHOD DECORATOR 

# from abc import ABC, abstractmethod

# # Abstract class
# class Vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         pass


# # Child class
# class Car(Vehicle):

#     def start(self):
#         print("Car starts with a key")


# class Bike(Vehicle):

#     def start(self):
#         print("Bike starts with a button")


# # Objects
# car = Car()
# bike = Bike()

# car.start()
# bike.start()



# ABSTRACT CLASS :
# SOMETIMES IMPLEMENTATION OF CLASS IS NOT COMPLETE SUCH TYPES OF PARTIALLY IMPLEMENTED CLASS IS KNOWN
# AS ABSTRACTION CLASS. ABSTRACT CLASS IS A CLASS THAT CANNOT BE INSTANTIATED. IT IS USED TO PROVIDE A 
# BASE FOR OTHER CLASSES TO INHERIT FROM. ABSTRACT CLASS CAN CONTAIN ABSTRACT METHODS, 
# WHICH ARE METHODS THAT HAVE NO IMPLEMENTATION AND MUST BE IMPLEMENTED BY SUBCLASSES.

# EVERY ABSTRACT CLASS IS A CLASS BUT NOT EVERY CLASS IS AN ABSTRACT CLASS.





# program 1:
class bank:
    def data(self):
        self.accountno=input("enter your account number ")
        self.balance=int(input("enter your bank balance "))
    def __task(self):
        operation=input("""enter your task deposit , withdraw ,display balance press d to dposit
        press w to withdraw and press b to display balance """)
        if operation=="d":
            self.dep=int(input("enter amount to deposit"))
            print("amount deposited successfully")
            self.balance=self.balance+self.dep
            print("your latest balance is",self.balance )  
        elif operation=="w":
            self.wit=int(input("enter amount to with draw"))
            print("amount withdrawed successfully")
            self.balance=self.balance-self.wit
            print("your latest balance is",self.balance )  
        else :
            print("your latest balance is",self.balance )  
b=bank()
b.data()
b._bank__task()


# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):

#     @abstractmethod
#     def Area(self):
#         pass


# class Circle(Shape):

#     def __init__(self, radius):
#         self.radius = radius

#     def Area(self):
#         return math.pi * self.radius * self.radius


# r = float(input("Enter radius: "))

# c = Circle(r)

# print("Area of Circle =", c.Area())
            
