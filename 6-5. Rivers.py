# Dictionary of rivers and the countries they run through
rivers = {
    "Nile": "Uganda",
    "Tana": "Kenya",
    "Orange": "South Africa"
}

# 1. Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river} River runs through {country}.")

print()  # blank line for readability

# 2. Print the name of each river
print("Rivers:")
for river in rivers.keys():
    print(river)

print()

# 3. Print the name of each country
print("Countries:")
for country in rivers.values():
    print(country)