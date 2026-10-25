num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
try:
    result=num1/num2
    print("The result is: ",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    