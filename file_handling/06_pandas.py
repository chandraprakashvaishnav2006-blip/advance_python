import pandas as pd

b=input("if you are an employee press yes or no: ")
a=b.lower()
if a == "yes":
    with open('data.csv', 'a') as f:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        gender = input("Enter your gender: ")
        f.write(f"{name},{age},{gender}\n")
        
else :
    print("You are not an employee.")


df = pd.read_csv('data.csv')
print(df)
