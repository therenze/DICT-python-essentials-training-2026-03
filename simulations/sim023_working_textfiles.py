import subprocess
import os
# The modern, safer way to clear the terminal
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)




#Python Simulation 23
#Working with Text File

# #writing into the file
# print()
# file_path = "my_data.txt"
# with open(file_path, "a") as file:  #APPEND
#     count = 3
#     data = ""
#     while count!=0:  # 0 != 0    TRUE
#         data = input("Write this text into the file: ")
#         count-=1
#         file.write(data + "\n")

# print()
# print("Text has been added to the file successfully!!!")





# #reading from a file
# print()
# file_path = "my_data.txt"
# with open(file_path, "r") as file:
#     file_contents = file.read()

# print()
# print("File Contents:\n")
# print(file_contents)





# #processing read files
# print()
# file_path = "numbers.txt"
# with open(file_path, "r") as file:
#     lines = file.readlines()

# total_sum = 0

# for line in lines:  # 1 2 3 4 5 [STRING]
#     number = int(line) # 3
#     total_sum += number # 3 + 3 = 3
    
# print("Sum of numbers:", total_sum)
# print()






#editing/updating a file
print()

file_path = "new_data.txt"
with open(file_path, "r") as file:
    file_contents = file.read()

print()
print("Current File Contents:\n")
print(file_contents, "\n")

new_data = input("Enter the new content: ")

with open(file_path, "w") as file:
    file.write(new_data)

print()
print("File Content Updated Successfully!!!")