# cleaning the terminal to only shows the output of the code
import os
# Clears the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')




# # Python Simulation 11
# # Python List

#update a list
print()

names = ["1", "2", "3", "4"]
print(f"Names: {names}")

names[0] = "surigao"
names[1] = "anao-aon"
print(f"Names: {names}")

names.append("motor")
print(f"Names: {names}")