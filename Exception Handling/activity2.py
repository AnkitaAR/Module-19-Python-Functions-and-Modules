try:
    num1,num2=eval(input("Enter two numbers separated by comma: "))
    res=num1/num2
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
    print("Error details:", e)
except SyntaxError as e:
    print("Error: Invalid input format. Please enter two numbers separated by a comma.")
    print("Error details:", e)
except:
    print("An unexpected error occurred.")
else:
    print("No exception")
    print("The result of division is:", res)
finally:
    print("This code will execute no matter what.")