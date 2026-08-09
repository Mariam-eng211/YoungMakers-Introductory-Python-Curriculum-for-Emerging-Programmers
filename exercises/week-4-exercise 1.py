# 1. Variables & Input
start = int(input("Enter starting countdown number: "))

# 2. While Loop
while start > 0:
    print(f"Counting down: {start}")
    start = start - 1  # Decrease number by 1

# 3. If/Else & Output
if start == 0:
    print(" Blast off!")
else:
    print("Countdown failed.")
