animals = ["zebra", "tiger", "cheetah"]

for animal in animals:
    print(animal)

print()

for animal in animals:
    if animal == "zebra":
        print("A zebra has bold black and white stripes all over its body.")
    elif animal == "tiger":
        print("A tiger has dark vertical stripes on orange fur.")
    elif animal == "cheetah":
        print("A cheetah has black spots covering its tan coat.")

print()

print("All of these animals have patterns on their fur.")




guests = ["Irene Rex", "Lucy Rex", "Eunice Rex"]

guests.insert(0, "Michelle Obama")
guests.insert(2, "Clark Peoples")
guests.append("Ayo Edibiri")

guests.sort()

print("The first three items in the list are:")
print(guests[:3])

print("\nThree items from the middle of the list are:")
middle_index = len(guests) // 2
print(guests[middle_index - 1: middle_index + 2])

print("\nThe last three items in the list are:")
print(guests[-3:])




pizzas = ["pepperoni", "cheese", "buffalo chicken"]

for pizza in pizzas:
    print(pizza)

print()

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print()

print("I really love pizza!")