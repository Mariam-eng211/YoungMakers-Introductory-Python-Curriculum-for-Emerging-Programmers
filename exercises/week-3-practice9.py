while True:
    secret_code = input("Enter the secret code to pass: ")
    
    if secret_code == "python123":
        print("Access granted!")
        break  # Immediately exits the while loop
    
    print("Wrong code! Try again.\n")
