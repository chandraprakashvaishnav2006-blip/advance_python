# import pandas as pd

# data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [24, 30, 28],
#     "Profession": ["Engineer", "Data Scientist", "Teacher"]
# }

# # Convert to DataFrame and display
# df = pd.DataFrame(data)
# print(df)   


# from tabulate import tabulate

# # Data as a list of lists
# data = [
#     ["Alice", 24, "Engineer"],
#     ["Bob", 30, "Data Scientist"],
#     ["Charlie", 28, "Teacher"]
# ]

# # Display with headers and a grid format
# print(tabulate(data, headers=["Name", "Age", "Profession"], tablefmt="grid"))   





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