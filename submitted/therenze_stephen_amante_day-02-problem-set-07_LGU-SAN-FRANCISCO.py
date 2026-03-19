#String method

input_string = input("\nEnter Any Word or Char: ")
validate_input_string = input_string
print("\n-----RESULTS-----")
print(f"Capitalizes the every first letter: {input_string.title()}")
print(f"Capitalizes the first letter of sentence: {input_string.capitalize()}")

print(f"Converted to lowercase: {input_string.lower()}")
print(f"Converted to uppercase: {input_string.upper()}")


print("\n-----VALIDATION-----")

print(f"Validate all char is uppercase: {validate_input_string} --> {validate_input_string.isupper()}")