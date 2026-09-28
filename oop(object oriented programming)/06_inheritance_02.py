
# # output  is m1 bcz of cunstructor is only in parent class
# class p:
#     def __init__(self):
#         print("m1")
# class c(p):
#     def m1(self):
#         print("m2")        
# o=c()        



#  output  is m2 bcz of cunstructor is on both class 

# class p:
#     def m1(self):
#         print("m1")
# class c(p):
#     def __init__(self):
#         super().m1()
#         print("m2")        
# o=c()



# class shopping:
    
#     def gen_bill(self,p,q):
#         self.bill=p*q
#         print("total bil is :",self.bill)
#     def discount(self,d):
#         self.disc= (self.bill*d)/100
#         print("the discout is ",self.disc)
#     def calculated_amount(self):
#         cal=self.bill-self.disc
#         print("calculated amount is ",cal)


# o=shopping()
# o.gen_bill(10,100)
# o.discount(10)
# o.calculated_amount()


class student :
    def __init__(self,roll,name,branch):
        self.roll=roll
        self.name=name
        self.branch=branch

   

# class student1(student):
#     def input(self,p,m,ph):
#         self.p=p
#         self.m=m
#         self.ph=ph
#     def cal(self):
#         cal=((self.p+self.m+self.ph)/300)*100    
#         print(f"total percentage is{cal}")
#     def info(self):
#             print("the name of student ",self.name)
#             print("the name of branch",self.branch)
#             print("the roll no of student ",self.roll)    
        

# s1=student1(21,"abhi","cs")

# s1.info()
# s1.input(80,80,80)
# s1.cal()

   

class emp:
    def __init__(self,name,id,sal):
        self.name=name
        self.id=id
        self.sal=sal
        print("the name of emp ",self.name)
        print("id of emp",self.id)
        print("the basic salary ",self.sal)

class salary(emp):
    def cal(self,hra,da):
        HRA=(self.sal*hra)/100
        DA=(self.sal*da)/100
        gross=self.sal+HRA+DA
        print("the name of emp ",self.name)
        print("id of emp",self.id)
        print("the basic salary ",self.sal)
        print("the HRA :",HRA)
        print(" the DA",DA)
        print("the gross salary :",gross)
o1=salary("arav",101,20000000000)   
o1.cal(8,10)


