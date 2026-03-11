# Movie theater ticket pricing program

# Ask the user how many tickets they want
num_tickets = int(input("Enter the number of tickets: "))

total_cost = 0

# Loop through each ticket
for i in range(num_tickets):
    age = int(input(f"Enter the age for ticket holder {i+1}: "))

    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    total_cost += price

# Display the total cost
print("The total cost of the tickets is: $" + str(total_cost))