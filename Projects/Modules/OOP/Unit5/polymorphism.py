'''
By Jean-G. De Souza
Essex University Online
PG Cert in Computer Science - Module OOP: Unit 5
Activity instructions:
        Write a Python program with polymorphism that is usable
        within the summative assessment for the driverless car.
'''

# --------------------------

class DriverlessCar:
    '''Class for a driverless Car. '''

    def __init__(self, mode="normal"):
        '''initialise a new instance of Driverless Car'''
        self.mode = mode
        self.speed = 0
        self.status = "Stopped"

    def change_mode(self, new_mode):
        '''Allow user to change the car's mode. '''
        if new_mode in ["normal", "eco", "sport", "DontSpillTheCoffee"]:
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

    def slow_down(self):
        """ Reduce the speed of the car to slow down. """
        self.speed = 15
        print("The vehicule is slowing down.")

    def respond_to_obstacle(self, distance):
        """ Handle by default obstacles based on their distance. Overriden by Mode subclasses. """
        if distance < 10:
            self.stop()
            print(f"The vehicule detected an obstacle at {distance} meters. Stoping the vehicule.")
        elif distance < 30:
            self.slow_down()
            print(f"The vehicule detected an obstacle at {distance} meters. Slowing down.")



class EcoMode(DriverlessCar):
    '''SubClass of DriverlessCar for Eco mode'''
    def move_forward(self):
        self.speed = 30


class SportMode(DriverlessCar):
    '''SubClass of DriverlessCar for Sport mode'''
    def move_forward(self):
        '''Overrides the speed of move_forward of the class to a sportier speed.
            (To be changed from speed to acceleration in the unit 7 assignment.) '''
        self.speed = 80
        print(f"The vehicle is going forward at a speed of {self.speed} KPH.")

    def respond_to_obstacle(self, distance):
        """ Overrides the default obstacles response specifically for the Sport Mode. """
        if distance < 5:
            self.stop()
            print(f"The vehicule detected an obstacle at {distance} meters. Stoping the vehicule.")
        elif distance < 10:
            self.slow_down()
            print(f"The vehicule detected an obstacle at {distance} meters. Slowing down.")


class DontSpillTheCoffeeMode(DriverlessCar):
    '''SubClass of DriverlessCar for Don't Spill The Coffee mode'''
    def move_forward(self):
        '''Overrides the speed of move_forward of the class to a sportier speed. '''
        self.speed = 30
        print("The vehicle is going forward as if there were a \
              burning-hot cup of coffee on the driver's lap.")

    def respond_to_obstacle(self, distance):
        """ Overrides the default obstacles response specifically
            for the Don't Spill The Coffee Mode. """
        if distance < 20:
            self.stop()
            print(f"The vehicule detected an obstacle at {distance} meters. Stoping the vehicule.")
        elif distance < 40:
            self.slow_down()
            print(f"The vehicule detected an obstacle at {distance} meters. \
                  Slowing down the vehicule.")


# -------- NOTES ----------

# Add the notion of acceleration in addition to speed, for the unit 7 assignment.
# Add the notion of deceleration in addition to Stop and SlowDown, for the unit 7 assignment.
