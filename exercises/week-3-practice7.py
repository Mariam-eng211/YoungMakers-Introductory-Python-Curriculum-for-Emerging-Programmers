#break and continue

#break: Stops the loop completely when a condition is met.
#continue: Skips the rest of the current iteration and moves immediately to the next item.
# Example of break: Search for an item and stop early
items = ["bread", "milk", "eggs", "apples"]

for item in items:
    if item == "eggs":
        print("Found eggs! Stopping search.")
        break
    print(f"Checked {item}...")
