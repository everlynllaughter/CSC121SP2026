try:
  num1 = input("Enter the first number: ")
  num2 = input("Enter the second number: ")

  # Convert inputs to integers
  num1 = int(num1)
  num2 = int(num2)

  result = num1 + num2

  print(f"The sum is {result}.")

except ValueError:
  print("Oops! Please enter valid numbers, not text.")
