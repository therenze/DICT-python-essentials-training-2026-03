import subprocess
import os
# The modern, safer way to clear the terminal
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)



# Python Simulation 22-01
# Classes in Python

#creating a class
print()
#class serves as blueprint or template of objects(instances)
#it defines set of attributes(properties) and methods(functions) describing
#behavior and characteristics of objects belonging to that class

class Student:

    def stud_details(self):
        print("My name is " + self.name)
        print("Taking", self.program)
        print("I am", self.age, "years old.\n")


#creating an object or instance of a class
s1 = Student()
#set the attributes
s1.name = "Junell"
s1.program = "BSIT"
s1.age = 36
s1.stud_details()



#creating another object or instance of a class
s2 = Student()
s2.name = "Maria"
s2.program = "BSCS"
s2.age = 35
s2.stud_details()



#creating a custom constructor
"""
A custom constructor, which is the __init__ method within a class, serves
the purpose of initializing the attributes or properties of an instance of
that class. It is invoked when an object is created, enabling the programmer
to set initial values for specific properties of the object. By defining
a custom constructor, you can control how the object's attributes are
initialized when it's instantiated.
"""
class My_Student:

    #custom constructor with 3 argument and the self
    def __init__(self, name, program, age):
        #defining instance attribute
        self.name = name        #name attribute
        self.program = program  #program attribute
        self.age = age          #age attribute


    def stud_details(self):
        #refencing instance attribute for a specific object (self.____)
        print("My name is " + self.name) 
        print("Taking", self.program)
        print("I am", self.age, "years old.\n")



print()
#create an object of a class
s1 = My_Student("Rosario", "BSIS", 35)
s2 = My_Student("Hannah", "BSN", 5)
s3 = My_Student("Elisha", "BEED", 17)

s1.stud_details()
s2.stud_details()
s3.stud_details()
