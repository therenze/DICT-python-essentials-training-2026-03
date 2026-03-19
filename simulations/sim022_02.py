import subprocess
import os
# The modern, safer way to clear the terminal
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)





# Python Simulation 22-02
# More on Python Classes

#list of employee and some details
print()
emp1 = ["ITO", "Junell", 36, "Level 1", 20_000]
emp2 = ["ITO", "Maria", 35, "Level 3", 30_000]

# class Employee:

#     def __init__(self, name, age, level, salary):
#         self.name = name
#         self.age = age
#         self.level = level
#         self.salary = salary

# print()

# emp1 = Employee("Junell", 36, "Level 1", 20_000)

# print(f"{emp1.name} {emp1.age} {emp1.level} {emp1.salary}\n")






#working with instance method
print()

class Programmer:

    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def programming(self):
        print(f"{self.name} is learning python.")
        print(f"Age: {self.age}\nLevel: {self.level}\nSalary: {self.salary}\n")

    def experience(self, years):
        print(f"{self.name} is an ITO for {years} years.")
        print(f"{self.name} is now {self.age} years old.\n")

    def inc_sal(self, years):
        if years>3:
            sal = self.salary * 3
            print(f"{self.name} ---- {sal}")
        else:
            sal = self.salary * 1.25
        return sal



emp1 = Programmer("Junell", 36, "Level 1", 20_000)
emp2 = Programmer("Maria", 35, "Level 3", 30_000)

emp1.programming()
emp2.programming()

emp1.experience(2)
emp2.experience(3)

print(f"{emp1.name} is now earning {emp1.inc_sal(4):.2f}")
print(f"{emp2.name} is now earning {emp2.inc_sal(1):.2f}")

# emp2.inc_sal(2)