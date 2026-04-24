# Open the file in append mode so names are added, not overwritten
with open('guest_book.txt', 'a') as file:
  while True:
    name = input("Enter your name (or type 'q' to quit): ")

    if name.lower() == 'q':
      break

    print(f"Hello, {name}! Thanks for visiting.")

    # Write the name to the file with a newline
    file.write(name + '\n')