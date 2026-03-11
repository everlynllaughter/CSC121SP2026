# Create a list of sandwich orders
sandwich_orders = ["tuna", "ham and cheese", "turkey", "blt"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Loop through the sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)

    # Print message that the sandwich is being made
    print("I made your " + current_sandwich + " sandwich.")

    # Move the sandwich to the finished sandwiches list
    finished_sandwiches.append(current_sandwich)

# Print all finished sandwiches
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich + " sandwich")
