
print("\n\n=====INPUT EMPLOYEE DETAILS=====")
name = input("\nEnter Employee Name: ")
hour = int(input("Enter Number of Hours: "))
sss = int(input("Enter SSS Contribution: "))
phil = int(input("Enter Phil Health Contribution: "))
loan = int(input("Enter Housing Loan: "))


rate = float(500)
gross = rate * hour
tax = float(gross * 0.10)
deduction = float(sss + phil + loan + tax)
net = float(gross - deduction)

print("\n\n=====PAYSLIP=====")
print("\n=====EMPLOYEE INFORMATION=====")

print("Employee Name: ",name)
print("Rendered Hours: ",hour)
print("Rate Per Hour: ",rate)
print("Gross Salary: ",gross)

print("\n\n=====DEDUCTION=====")
print("SSS: ",sss)
print("PhilHealth: ",phil)
print("Other Loan: ",loan)
print("Tax: ",tax)
print("Total Deduction: ",deduction)

print("\n\nNet Salary: ",net)