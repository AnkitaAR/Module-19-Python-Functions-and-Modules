import math
try:
    n1=int(input("Enter the first number :"))
    n2=int(input("Enter the second number:"))
    result=math.lcm()
    print("LCM of",n1," and",n2," is :",result)
except ValueError as e:
    print("Invalid numbers")