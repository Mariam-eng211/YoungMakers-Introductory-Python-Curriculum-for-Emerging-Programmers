#for loop: Used when you know in advance how many times to repeat something (e.g., “repeat 5 times” or “for every item in a list”).
#while loop: Used when you want to keep repeating code as long as a condition remains True (e.g., “keep asking until the user types 'quit'”).
#Always make sure the condition eventually becomes False (like updating count). Otherwise, you will create an infinite loop that runs forever!
count = 1

# Runs as long as count is less than or equal to 5
while count <= 5:
    print(f"Current count: {count}")
    count += 1  # Increment count by 1 (same as count = count + 1)

print("Loop finished!")
