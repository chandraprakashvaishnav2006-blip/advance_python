import pandas as pd
class student:
    def details(self,):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.roll_no = int(input("Enter your roll number: "))
    def marks(self):
        self.physics = float(input("Enter your physics marks: "))
        self.chemistry = float(input("Enter your chemistry marks: "))
        self.maths = float(input("Enter your maths marks: "))
        self.python = float(input("Enter your python marks: "))
        self.total =( (self.physics + self.chemistry + self.maths + self.python) / 400)*100
    def attendances(self):
        self.attendance = float(input("Enter your attendance percentage: "))
        if self.attendance >= 75:
            print("You are eligible for the exam.")
        else:
            print("You are not eligible for the exam.")
    def write(self):
        with open("DATA.csv",'w') as f:
            f.write(f"name={self.name}\n")
            f.write(f"age={self.age}\n")
            f.write(f"roll no={self.roll_no}\n")
            f.write(f"marks of physics={self.physics}\n")
            f.write(f"marks of chemistry={self.chemistry}\n")
            f.write(f"marks of maths={self.maths}\n")
            f.write(f"marks of python={self.python}\n")
            f.write(f"total marks={self.total}\n")
            f.write(f"attendance percentage={self.attendance}\n")
    def read(self):
        df=pd.read_csv("DATA.csv")
        print(df)

e=student()
e.details()
e.marks()                    
e.attendances()
e.write()
e.read()
                        