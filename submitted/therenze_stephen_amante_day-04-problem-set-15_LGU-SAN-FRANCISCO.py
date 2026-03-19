alphabet = "abcdefghijklmnopqrstuvwxyz"

last_name = input("Enter your Last Name: ").strip().lower()

print(f"\n--- Sequence for {last_name.upper()} ---")

for letter in last_name:
   
    if letter in alphabet:
        sequence_num = alphabet.index(letter) + 1
        print(f"Letter: {letter.upper()} | Sequence #: {sequence_num}")
    else:
        print(f"Character: {letter} | (Not a letter)")




        



 
