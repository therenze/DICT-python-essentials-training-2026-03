# # # cleaning the terminal to only shows the output of the code
# # import os
# # # Clears the terminal screen
# # os.system('cls' if os.name == 'nt' else 'clear')



# # # Python Simulation 15
# # # Python For Loop

# # #looping from a list
# # print()
# # num = [10, 20, 30, 40, 50]
# # for each_num in num:
# #     print(each_num)



# # #looping from a tuple
# # print()
# # name = ("Junell", "Maria", "Hannah", "Elisha")
# # for each_name in name:
# #     print(each_name, end="-->")
# # print()



# # #looping through each character in a string input
# # print()
# # text = input("Enter a text: ")
# # for each_text in text:
# #     print(each_text)



# # #looping from a dictionary
# # print()
# # numNames = {1:"One", 2:"Two", 3:"Three"}
# # for pair in numNames.items():
# #     print(pair, type(pair), sep=" --> ", end="\n")



# # #looping from a range
# # print()
# # num_range = range(5)    #0 1 2 3 4
# # print(num_range, type(num_range), sep=" --> ")

# # for num in range(5):
# #     print(num)



# # #altering for loops action
# # print()
# # stop = int(input("Stopping Number[1-10]: "))
# # x = 10
# # for i in range(x):
# #     print(i)
# #     if i==stop:
# #         print("ENOUGH!!!")
# #         break




# # #nested for loop
# # print()
# # for x in range(1,4):
# #     for y in range(1,3):
# #         print(f"x{x} --- y{y}.")
# #     print()




# # #itering multiple list items
# # print()
# # odd = [1,3,5,7,9]
# # even = [2,4,6,8,10]

# # for o_num in odd:
# #     for e_num in even:
# #         prod = o_num * e_num
# #         print(f"{o_num} * {e_num} = {prod}")
# #     print()




# # #itering items in a list and getting its total
# # print()
# # num = [
# #         [1,2,3],
# #         [4,5,6],
# #         [7,8,9]
# #     ]

# # for i in num:
# #     print(i)
# #     sum = 0
# #     for j in i:
# #         print(j)
# #         sum += j
# #     print(f"The sum is {sum}\n")




# #removing duplicate items in list
# print()
# letters_list = list("AaAbBCCcDDDdAbcdxyafastbhc")
# print(f"List of Letters: {letters_list}")

# ls = []
# for ll in letters_list:
#     if ll in ls:
#         del(ll)
#     else:
#         ls.append(ll)
# print(f"Deleted Duplicate with New List: {ls}")

# print()
# print("Letters List: {}".format(letters_list))
# for l2 in letters_list:
#     lc = letters_list.count(l2)
#     if lc>1:
#         letters_list.remove(l2)
# print("Filtered Letters: {}".format(letters_list))

# print()
# my_text = list(input("Enter a text: "))
# print(f"User Text: {my_text}\tType Text: {type(my_text)}")

# store_list = []
# print()
# for s in my_text:
#     if s in store_list:
#         print(f"{s} has duplicate")
#     else:
#         store_list.append(s)

# print()
# num = [1.42,2,3,4,5]
# for i in num:
#     if type(i) is not int:
#         print(f"{i} is not integer")
#         break
#     else:
#         print(f"{i}")