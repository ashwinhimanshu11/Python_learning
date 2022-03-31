from ast import operator


num1 = float(input("enter first number: "))
operator = input("enter operator: +, -, *, /\n")
num2 = float(input("enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid Operator!")