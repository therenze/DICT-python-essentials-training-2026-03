# cleaning the terminal to only shows the output of the code
import os
# Clears the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')



import random

# 1. Setup the options
options = ["SURIGAO", "CHINA", "USA", "KEYBOARD WARRIOR"]

print("---"*17)
banner1 = "AVAILABLE OPTIONS 1 TO 4"
banner2 = "[1]SURIGAO - [2]CHINA - [3]USA - [4]KEYBOARD WARRIORS"
print(banner1.center(50))
print(banner2.center(50))

print("---"*17)
user_choice = input(f"ENTER YOUR NUMBER CHOICE: ")
choice_index = int(user_choice) - 1



# 2. Computer makes a random choice
computer_choice = random.choice(options)
print(f"\nYOU CHOOSE: \t{options[choice_index]}")
print(f"COMPUTER: \t{computer_choice}\n")



# 3. Game Logic
user_pick = options[choice_index]
wins = {
    "KEYBOARD WARRIOR": ["SURIGAO", "CHINA", "USA"],
    "USA": ["CHINA", "SURIGAO"],
    "CHINA": ["SURIGAO"]
    }

if user_pick == computer_choice:
    print("IT'S A TIE!")

elif computer_choice in wins.get(user_pick, []):
    print(f"YOU WIN! {user_pick} BEATS {computer_choice}")
    # user_score += 1
else:
    print(f"YOU LOSE! {computer_choice} BEATS {user_pick}")
    # computer_score += 1






