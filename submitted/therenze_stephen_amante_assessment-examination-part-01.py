import random
import os

options = ["SURIGAO", "CHINA", "USA", "KEYBOARD WARRIOR"]

# Initialize Scores
user_score = 0
computer_score = 0
game_number = 1

# Game Loop
while user_score < 3 and computer_score < 3:
    # Clear screen directly inside the loop
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print("---" * 18)
    header = f" ROUND {game_number} | YOU: {user_score} - COMPUTER: {computer_score} "
    print(header.center(50))
    print("---" * 18)

    banner1 = "AVAILABLE OPTIONS 1 TO 4"
    banner2 = "[1]SURIGAO - [2]CHINA - [3]USA - [4]KEYBOARD WARRIORS"
    print(banner1.center(50))
    print(banner2.center(50))
    print("---"*18)

    # catch user input
    user_choice = input("\nENTER YOUR NUMBER CHOICE: ")
    choice_index = int(user_choice) - 1
    user_pick = options[choice_index]

    #catch computer input
    computer_choice = random.choice(options)

    #printing choices
    print(f"\nYOU CHOSE: \t{user_pick}")
    print(f"COMPUTER: \t{computer_choice}")

    # Game Logic
    wins = {
        "KEYBOARD WARRIOR": ["SURIGAO", "CHINA", "USA"],
        "USA": ["CHINA", "SURIGAO"],
        "CHINA": ["SURIGAO"]
    }

    if user_pick == computer_choice:
        print("\nIT'S A TIE!")
    elif computer_choice in wins.get(user_pick, []):
        print(f"\nYOU WIN! {user_pick} beats {computer_choice}")
        user_score += 1
        game_number += 1
    else:
        print(f"\nYOU LOSE! {computer_choice} beats {user_pick}")
        computer_score += 1
        game_number += 1

    # Pause to see results
    if user_score < 3 and computer_score < 3:
        print("\n\n","---"*18)
        banner3 = "> > Press Enter for the next round < <"
        input(banner3.center(50))



# 4. Final Result
if os.name == 'nt': os.system('cls')
else: os.system('clear')

print("===" * 15)
if user_score == 3:
    print(f"SERIES OVER: YOU WON {user_score}-{computer_score}!".center(45))
else:
    print(f"SERIES OVER: COMPUTER WON {computer_score}-{user_score}!".center(45))
print("===" * 15)