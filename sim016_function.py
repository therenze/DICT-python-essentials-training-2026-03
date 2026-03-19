# cleaning the terminal to only shows the output of the code
import os
# Clears the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')







# Python Simulation 16
# Python Function

# #user-defined function
# print()
# def message():
#     """This function prints a message"""
#     print("Hello World!!!")
#     print("I am learning python.")
#     print("Thank you!!!")

# message()   #calling the defined function
# message()
# message()



#assigned a user-defined function
# print()
# def fav_fruits():
#     print("Apples, Mango, and Oranges.\n")
# f = fav_fruits()
# print(f, end="\n\n")



# #defining a function to receive data for processing
# def message(name:str):
#     print("Hello", name, end="\n\n")
#     print(f"{name} \t{type(name)}")
# message("Junell")
# message("Maria")
# message(123)



# #multiple parameters in function
# print()
# def gospel(g1,g2,g3,g4):
#     print("Christ's Apostles:", g1,g2,g3,g4, sep="\n", end="\n\n")
# gospel("Luke","Mark","Matthew","John")



# #defining a fucntion with unknown number of arguments
# print()
# def apostles(*a):
#     print(f"Christ's Apostles: {a[0]}, {a[1]}, {a[2]}")
# apostles("Simon","Peter","John","Thomas","Jude")



#getting the sum of numbers
print()
def get_sum(*n):
    sum = 0
    for num in n:
        sum += num
    return sum
print(f"The sum is {get_sum(1,2,3)}")
print(f"The sum is {get_sum(2,3,5123,2,5,2)}")



# #more on function
# print()
# def access(un,pw):
#     print("Username:", un)
#     print("Password:", pw)
# uname = "jtbojocan"
# pword = "admin"
# access(uname,pword)



# #receiving excess
# print()
# def names(**person):
#     print("Hello", person["fname"], person["lname"])
# names(fname="Junell", lname="Bojocan")
# names(fname="Maria", lname="Bojocan", age=36)
# #names(fname="Elisha")  KeyError: 'lname'



# #using the function's default value
# print()
# def numbers(num=35):
#     print(f"Num = {num}")
# numbers(15)
# numbers(1233)
# numbers()



# #functions with return value
# print()
# def total(n1,n2):
#     return n1+n2
# result = total(10,23)
# print(f"The sum is {result}")
# result = total(12.32,1.52)
# print(f"The sum is {result}")



# #the lambda function
# print()
# def sqr(x):
#     return x*x
# r1 = sqr(5)
# print(f"The square of 5 is {r1}")

# sqr2 = lambda x: x*x
# res = sqr2(5)
# print(f"\nThe square of 5 is now {res}")

# calc_total = lambda n1,n2: n1+n2
# print(f"The calculated total is {calc_total(10,32)}")

# message = lambda name: print("Hello", name)
# message("Junell")
# message("Maria")