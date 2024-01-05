'''
By Jean-G. De Souza
Essex University Online
PG Cert in Computer Science - Module OOP: Unit 7

    Activity instructions:
  " Create a nested dictionary of data on cars within a Car class.
    Extend the program to work with the dictionary by calling the following methods:
    items(), keys(), values() "
'''

# --------------------------

class Car:
    '''Class for cars data in nested dictionary'''
    def __init__(self):
        self.cars = {}  # Initialize empty dictionary to store cars data

    def add_car(self, brand, model, year):
        ''' Add car information. '''
        if brand in self.cars:
            # If brand exists, append new model to the list
            self.cars[brand].append({"model": model, "year": year})
        else:
            # If brand does not exist, create a new entry with a list
            self.cars[brand] = [{"model": model, "year": year}]

    def get_items(self):
        ''' Return all items in dictionary. '''
        return self.cars.items()

    def get_keys(self):
        ''' Return all car brands (keys). '''
        return self.cars.keys()

    def get_values(self):
        ''' Return all models and years (values) for each brand. '''
        return self.cars.values()


# ---- Use Example ----
car_inventory = Car()
car_inventory.add_car("Ford", "Focus", 2020)
car_inventory.add_car("Peugeot", "206", 2018)
car_inventory.add_car("Peugeot", "308", 2019)

# Displaying the results using the new methods
print("Items:", list(car_inventory.get_items()))
print("Keys:", list(car_inventory.get_keys()))
print("Values:", list(car_inventory.get_values()))
