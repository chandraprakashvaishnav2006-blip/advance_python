# class: it is a blueprint or template used to create an object 
# object: object is instance of class.
# it refers the actual entity of class.

class employee:
    company="HP"
    def skill(self):
        print(self)
        return 34000

e1=employee()
e2=employee()
print(e1.skill())
print(e2.skill())


# self: it is a refrence to a current object of class
# note: it is not a keyword it is a conventional name used for first parameter 