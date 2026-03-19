# cleaning the terminal to only shows the output of the code
import os
# Clears the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')



prog_language = ["Python", "C++", "C", "PHP", ".NET", "Java", "Flask", "DJango"]

print("-" *50)
print(f"SEARCH A PROGRAMMING LANGUAGE OR".center(50))
print(f"TYPE 'EXIT' TO QUIT PROGRAM".center(50))
print(f"TYPE '1' TO VIEW LIBRARY".center(50))
print("-" *50)


while True:
    user_input = input("\nInput: ").strip()
    search_list = [lang.lower() for lang in prog_language]

    # The Break Condition
    if user_input.upper() == "EXIT":
        print("Exiting search... Goodbye!")
        break 

    elif user_input.upper() == "1":
        print(prog_language)

    elif user_input.lower() in search_list:
        prog_index = search_list.index(user_input.lower())
        print(f"Found!: Language: {user_input}, Index: {prog_index}")

    else:
        print(f"Language '{user_input}' Not Found!")

print("--- PROGRAM ENDED ---")
    


