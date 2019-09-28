num1=float(input("Enter first number: "))
operator=input("Operator")
num2=float(input("Enter second number:"))
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
else:
    print (num1/num2)
