# SUPER FUNCTION : IT IS INBUILD FUNCTION TO CALL PARENT CLASS CONSTRUCTOR , METHODS AND VARIABLES EXPLICITLY
# FROM THE CHILD CLASS. IT IS USED TO AVOID OVERRIDING OF PARENT CLASS METHODS AND VARIABLES.IT IS USED TO SOLVE
# THE AMBIGUITY PROBLEM WITH SAME NAME OF METHODS AND VARIABLES IN PARENT AND CHILD CLASS.



# class p:
#     def m1(self):
#         print("m1 is called ")
# class p2(p):
#     def m1(self):
#         super().m1()
#         print("m2 is called")

# e=p2()
# e.m1()


class person:
    def details(self):
        name=input("enter name ")
        age=int(input("enter age "))
        height=float(input("enter height "))
        weight=float(input("enter weight "))
        print("name is ",name)
        print("age is ",age)
        print("height is ",height)
        print("weight is ",weight)

class student(person):
    def academic(self):
        roll_no=int(input("enter roll number "))
        marks=int(input("enter marks "))
        print("roll number is ",roll_no)
        print("marks is ",marks)

    def display(self):
        super().details()
        self.academic()    
e=student()
e.display()