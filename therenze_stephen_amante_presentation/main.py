import subprocess
import os
# The modern, safer way to clear the terminal
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)



# get the word/name from the user
from package import Builder
my_builder = Builder() #object creation / instantiating the class


print("-" * 50)
print(f"WORD LENGTH SHAPE PATTERN".center(50))
print("-" * 50)
print(f"> > > > CHOICES < < < <".center(50))
print(f"BOX -- TRIANGLE -- FRAME -- DIAMOND".center(50))
print("-" * 50)
print()


#takes user input
word = input("INPUT ANYTHING: ")
choice = input("SELECT A SHAPE: ").upper()
size = len(word) #count number of char


#conditional statement
if choice == "BOX":
    print(f"\n\nBUILDING A BOX FOR '{word}' ({size}x{size}):")
    my_builder.box(size)

elif choice == "TRIANGLE":
    print(f"\n\nBUILDING A TRIANGLE FOR '{word}' (BASE: {size}):")
    my_builder.triangle(size)

elif choice == "FRAME":
    print(f"\n\nBUILDING A FRAME FOR '{word}' ({size}x{size}):")
    my_builder.frame(size)

elif choice == "DIAMOND":
    print(f"\n\nBUILDING A DIAMOND FOR '{word}' (WIDTH: {size}):")
    my_builder.diamond(size)

else:
    print(f"\n\n'{choice}' IS NOT A VALID OPTION.")
    print("AVAILABLE OPTIONS: [ BOX, TRIANGLE, FRAME, DIAMOND ]")
