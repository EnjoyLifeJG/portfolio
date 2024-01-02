# Program name: Poly.py
# By Jean-G. De Souza
# Essex University Online
# PG Cert in Computer Science / Module OOP / Unit 5
# Activity instructions: Write a Python program with polymorphism that is usable within the summative assessment for the driverless car.

# --------------------------

class DriverlessCar:
    '''Class for a driverless Car. '''

    def __init__(self, mode="normal"):
        '''initialise a new instance of Driverless Car'''
        self.mode = mode # ideas for later: dontSpillTheCoffee (normal by default)
        self.speed = 0
        self.status = "Stopped"

    def change_mode(self, new_mode):
        '''Allow user to change the car's mode. '''
        if new_mode in ["normal", "eco", "sport"]:
            self.mode = new_mode
            print(f"Mode changed to {self.mode}.")
        else:
            print("Invalid mode. Please choose between 'normal' , 'sport' or 'eco'.")

    def move_forward(self):
        ''' Setspeed to 50 (Normal Mode) and updating status. Made to be overitten by subclass. '''
        self.status = "Moving"
        print("The vehicule is moving forward.")
        self.speed = 50

    def stop(self):
        ''' Stop the car by setting the speed to 0 and updating the status. '''
        self.speed = 0
        self.status = "Stopped"
        print("The vehicule has stopped.")

    def respond_to_obstacle(self, distance):
        """ Respond to an obstacle detected by the car. """
        self.distance = distance
        print(f"The vehicule detected an obstacle at {distance} meters.")

class EcoMode(DriverlessCar):
    '''SubClass of DriverlessCar for Eco mode'''
    def move_forward(self):
        self.speed = 30

class SportMode(DriverlessCar):
    '''SubClass of DriverlessCar for Sport mode'''

    def move_forward(self):
        '''Overides the speed of move_forward of the class to a sportier speed. (To be changed from speed to acceleration in the unit 7 assignment.) '''
        self.speed = 80
