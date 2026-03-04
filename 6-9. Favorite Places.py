# Create the dictionary
favorite_places = {
    "Dalton": ["Paradise Falls in North Carolina"],
    "Claire": ["The Beach"],
    "Everlyn": ["Calgary, Alberta"]
}

# Loop through the dictionary and print each person's favorite places
for name, places in favorite_places.items():
    print(name + "'s favorite places:")
    for place in places:
        print(place)
    print()