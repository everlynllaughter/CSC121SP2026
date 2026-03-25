def make_car(manufacturer, model, **kwargs):
 car = {
 "manufacturer": manufacturer,
 "model": model
 }

 # Add any additional keyword arguments
 for key, value in kwargs.items():
    car[key] = value

 return car


# Call the function
car = make_car("Mazda", "CX-5", color="blue", tow_package=True)

# Print the result
print(car)