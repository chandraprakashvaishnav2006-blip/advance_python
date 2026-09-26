
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


