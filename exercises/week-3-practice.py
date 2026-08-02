city = input("What city do you live in? ")
 temperature = float(input("What is the current temperature in °C? ")) 
# Using an f-string to embed variables directly 
print(f"It is currently {temperature}°C in {city}.")

price = float(input("Enter item price: ")) total_price = price * 1.08 
# Adding 8% tax
print("Total price with tax:", total_price)
