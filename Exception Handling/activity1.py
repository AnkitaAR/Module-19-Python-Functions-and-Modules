try:
    number=int(input("Enter a number: "))
    print("You entered:", number)
except ValueError as e:
    print("Invalid input! Please enter a valid integer.")
    print("Error details:", e)