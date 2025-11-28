def add(a,b):
    sum=a+b
    return sum
def subtract(a,b):
    diff=a-b
    return diff
def multiply():
    product=a*b
    return product
def divide():
    quotient=a//b
    return quotient
print("Welcome to the calulator")
print("Addition")
print("Subtraction")
print("Multiplication")
print("Division")
choice=input("Please enter your choice of operation(+,-,*,/) :")
num1=int(input("Enter the first operator :"))
num2=int(input("Enter the second operator :"))
if choice=="+":
    add(num1,num2)
    print("The addition of ",num1," and ",num2," is ",add(num1,num2))
    
elif choice=="-":
    subtract(num1,num2)
    print("The addition of ",num1," and ",num2," is ",subtract(num1,num2))

elif choice=="*":
    multiply(num1,num2)
    print("The addition of ",num1," and ",num2," is ",multiply(num1,num2))
elif choice=="/":
    divide(num1,num2)
    print("The addition of ",num1," and ",num2," is ",divide(num1,num2))
else:
    print("Invalid input")
