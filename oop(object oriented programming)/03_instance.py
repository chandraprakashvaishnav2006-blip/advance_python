class emp:
    company="ASUS"
    def __init__ (self,company):
        self.company=company

    def details(self):
        print(self.company)


e1=emp("tesla")
print(e1.company)
print(emp.company)  

