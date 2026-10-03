# POLYMORPHISM: 
# IT MEANS MANY FORMS.
# IT GIVES MORE FLEXIBILITY TO THE PROGRAMMER
# 1. OPERATOR OVERLOADING: IT IS A TYPE OF POLYMORPHISM IN WHICH WE CAN USE SAME OPERATOR FOR DIFFERENT PURPOSES.
# 2 OVERRIDING: IT IS A TYPE OF POLYMORPHISM IN WHICH WE CAN USE SAME METHOD NAME FOR DIFFERENT PURPOSES.
# NOTE: PYTHON SUPPORT OPERATOR OVERLOADING BUT JAVA DOES NOT SUPPORT OPERATOR OVERLOADING. JAVA SUPPORTS ONLY OVERRIDING.




# OPERATOR OVERLOADING: IT IS A TYPE OF POLYMORPHISM IN WHICH WE CAN USE SAME OPERATOR FOR DIFFERENT PURPOSES.
# class A:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):
#         return self.pages+other.pages    
# b1=A(100)
# b2=A(200)
# print(b1+b2)  # it will give 300 because + operator is



# class A:
#     def __init__(self,pages):
#         self.pages=pages
#     def __sub__(self,other):
#         return self.pages-other.pages    
# b1=A(100)
# b2=A(200)
# print(b1-b2)  # it will give -100 because - operator is



# class A:
#     def __init__(self,pages):
#         self.pages=pages
#     def __eq__(self,other):
#         return self.pages==other.pages    
# b1=A(100)
# b2=A(200)
# print(b1==b2)  # it will give False because == operator is


# class A:
#     def __init__(self,marks):
#         self.marks=marks
#     def __gt__(self,other):
#         return self.marks>other.marks    
# b1=A(100)
# b2=A(200)
# if b1>b2:
#     print("b1 is greater than b2")  
# else:
#     print("b2 is greater than b1")  # it will give b2 is greater than b1 because > operator is    


# class student :
#     def __init__ (self,name,marks):
#         self.name=name
#         self.marks=marks

#     def __lt__(self,other):
#         return self.marks<other.marks    


# a=student("ram",100)
# b=student("shyam",200)
# if a<b:
#     print("a is less than b")   
# else:
#     print("b is less than a")  # it will give a is less than b because < operator is    

