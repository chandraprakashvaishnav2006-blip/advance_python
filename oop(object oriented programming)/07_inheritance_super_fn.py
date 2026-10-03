class p:
    def m1(self):
        print("m1 is called ")
class p2(p):
    def m1(self):
        super().m1()
        print("m2 is called")

e=p2()
e.m1()