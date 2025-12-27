import random
n=random.randint(1,10)
print("Welcome to number game :")
print("I will generate a number between 1 to 10 you have to guess it right")
while True:
    a=int(input("Guess a number between 1 to 10:"))
    if n==a:
        print("You guessed it right, the number was :",a)
        break
    else:
        print("Not the correct guess,Try again")
