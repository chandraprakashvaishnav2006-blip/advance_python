# try:
#     f=open("abczy.txt",'r')
#     content=f.read()
#     print(content)
#     f.close()
# except FileNotFoundError:
#     print("File not found.")





# Reading line by line
# j=0
# try:
#     f = open("abcz.txt", "r")
#     for line in f: # Efficient for large files
#         print(line.strip()) # Remove newline characters
#         j+=1
#     print(f"Total lines read: {j}")    
#     f.close()
# except FileNotFoundError:
#     print("File not found.")





# class A:
#     def info(self):
#         self.name=input("Enter your name: ")
#         self.rollno=int(input("Enter your roll number: "))
#         self.marks=float(input("Enter your marks: "))
#     def update(self):
#         with open("MARKS.txt","a") as f:
#             f.write(f"{self.name}\n{self.rollno}\n{self.marks}\n")
#             print("Data updated successfully.")
#     def read(self):
#         with open("MARKS.txt","r") as f:
#             content=f.read()    
#             print(content)


# e=A()
# e.info()
# e.update()
# e.read()



import pandas as pd
from tabulate import tabulate


class A:

    def info(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.profession = input("Enter your profession: ")

    def update(self):
        data = {
            "Name": [self.name],
            "Age": [self.age],
            "Profession": [self.profession]
        }

        df = pd.DataFrame(data)

        df.to_csv("DATA.csv", mode="a", index=False, header=False)

        print("Data inserted successfully.")

    def read(self):
        df = pd.read_csv(
            "DATA.csv",
            names=["Name", "Age", "Profession"]
        )

        print("\nStored Data:")
        print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))


e = A()

e.info()
e.update()
e.read()