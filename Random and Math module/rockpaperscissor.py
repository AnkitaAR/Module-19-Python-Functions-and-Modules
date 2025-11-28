import random
while True:
    action=input("Enter your action (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"You chose: {action} and the computer chose: {computer_action}.")
    if action==computer_action:
        print(f"Both players selected {action}. It's a tie!")
    elif action=="rock":
        if computer_action=="scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif action=="paper":
        if computer_action=="rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cut paper! You lose.")
    elif action=="scissors":
        if computer_action=="paper":
            print("Scissors cut paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    play_again=input("Play again? (y/n): ")
    if play_again.lower()!="y":
        break
