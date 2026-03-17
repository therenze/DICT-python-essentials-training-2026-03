print("\nDAY 1 - ACTIVITY 2: PROGRESSIVE ARITHMETIC APPLICATION")

# ask for a value
last_name = input("\nENTER LASTNAME: ")
find_char = last_name[0].upper()  #converting the first character to uppercase

# ord gets the ASCII value of the character, "A" = 65
num1 = ord(find_char) - 64  #subtracting 64 to get the position in the alphabet (A=1, B=2, ..., Z=26)
print(f"\nLastname is: {last_name} \nAlphabetical position of '{find_char}' is: {num1}")

half_value_of_num1 = num1 / 2
print(f"Half of '{num1}' is: {half_value_of_num1}") 

num2 = int(input("\nEnter a number: "))



print("\n--- STARTING PROGRESSIVE OPERATIONS ---")

# STEP A: Addition (num2 + half_value_of_num1)
res_add = num2 + half_value_of_num1
print(f"ADDITION: \n\t{num2} + {half_value_of_num1} = {res_add} | ID: {id(res_add)}")

# STEP B: Subtraction (num2 - half_value_of_num1)
res_sub = num2 - half_value_of_num1
print(f"SUBTRACTION: \n\t{num2} - {half_value_of_num1} = {res_sub} | ID: {id(res_sub)}")

# STEP C: Multiplication (num2 * half_value_of_num1)
res_mul = num2 * half_value_of_num1
print(f"MULTIPLICATION: \n\t{num2} * {half_value_of_num1} = {res_mul} | ID: {id(res_mul)}")

# STEP D: Division (num2 / half_value_of_num1)
res_div = num2 / half_value_of_num1
print(f"DIVISION: \n\t{num2} / {half_value_of_num1} = {res_div} | ID: {id(res_div)}")

# STEP E: Modulo (num2 % half_value_of_num1)
res_mod = num2 % half_value_of_num1
print(f"MODULO: \n\t{num2} % {half_value_of_num1} = {res_mod} | ID: {id(res_mod)}")

# STEP F: Exponentiation (num2 ** half_value_of_num1)
res_exp = num2 ** half_value_of_num1
print(f"EXPONENTIATION: \n\t{num2} ** {half_value_of_num1} = {res_exp} | ID: {id(res_exp)}")