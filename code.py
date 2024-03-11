import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input('choose rock/paper/scissors or Q to quit: ').lower()
    if user_input == "q":
        break
    
    if user_input not in ["rock", "paper", "scissors"]:
        print('Please enter a valid option.')
        continue

    random_num =random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    
    computer_pick = options[random_num]
    print("Computer picked", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        computer_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
        continue

    elif user_input == computer_pick:
        print("Tie!")
        continue
    
    else:
        print("You lost!")
        computer_wins += 1
        continue

print("You won", user_wins,"times. Computer won", computer_wins,"times.")  
print("\n\tGoodbye! ")

