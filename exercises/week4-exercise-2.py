total_cost = 0
tickets = int(input("How many tickets do you want to buy? "))

for i in range(1, tickets + 1):
    age = int(input(f"Enter age for person #{i}: "))
    
    if age < 12:
        print("-> Child ticket: $5")
        total_cost = total_cost + 5
    else:
        print("-> Adult ticket: $10")
        total_cost = total_cost + 10

print(f"\nTotal Cost for all tickets: ${total_cost}")
