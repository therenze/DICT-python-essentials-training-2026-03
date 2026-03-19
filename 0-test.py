
# get the word/name from the user
name = input("INPUT ANYTHING: ")
size = len(name) # get the total count of char in a word

print(f"\nBUILDING A BOX WITH A SIZE OF '{size} x {size}':\n")



# reset our counters
y = 0

#outer loop (vertical rows)
while y < size:
    x = 0
    # inner loop (horizontal stars)
    while x < size:
        print("*", end=" ")
        x += 1
    print() # move to the next line
    y += 1