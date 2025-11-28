valid=False
while not valid:
    try:
        number=int(input("Enter a number: "))
        while number%2==0:
           print("bye")
           valid=True
    except ValueError as e:
        print("Invalid input! Please enter a valid integer.")
        print("Error details:", e)