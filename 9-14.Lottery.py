from random import randint

# Step 2: list with 10 numbers and 5 letters
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
letters_list = ['A', 'B', 'C', 'D', 'E']

# Step 3: randomly select 4 numbers and 1 letter
lottery_numbers = []
for i in range(4):
  lottery_numbers.append(numbers_list[randint(0, 9)])

lottery_letter = letters_list[randint(0, 4)]

lottery = lottery_numbers + [lottery_letter]

# Step 4: get user input
user_input = input("Enter 4 numbers and 1 letter (example: 1 2 3 4 A): ")
user_list = user_input.split()

user_numbers = [int(num) for num in user_list[:4]]
user_letter = user_list[4]

user_ticket = user_numbers + [user_letter]

# Step 5: compare
print("Winning ticket:", lottery)
print("Your ticket:", user_ticket)

if user_ticket == lottery:
  print("You won!")
else:
  print("Sorry, you lost.")