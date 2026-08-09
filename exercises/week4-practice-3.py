correct_pin = "9999"

for attempt in range(1, 4):
    pin = input(f"Attempt #{attempt} of 3 - Enter PIN: ")
    
    if pin == correct_pin:
        print(" Access Granted!")
        break
    else:
        print(" Incorrect PIN.")

if pin != correct_pin:
    print("\n Account locked due to 3 failed attempts.")
