# constructor : it is a special feature of class that automatically called when object is created

# class employee():
#     def __init__ (self):
#         print("hello")
# e1=employee()

class emp():
    def __init__ (self,salary,name,bond):
        self.salary=salary
        self.name=name
        self.bond=bond
        # here it create an insance attribute of name salary and bond

    def details(self):
        print(self.salary)
        print(self.name)
        print(self.bond)

e1=emp(3400,"arav",4)
print(e1.details())

