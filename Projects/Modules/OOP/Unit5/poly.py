class DriverlessCar:
    '''Class for a driverless Car. '''

    def __init__(self, mode="normal"):
        '''initialise a new instance of Driverless Car'''
        self.mode = mode # ideas for later: sport, snow, normal, eco, dontSpillTheCoffee
        self.speed = 0
        self.status = "Stopped"

    def change_mode(self, new_mode):
        '''Allow user to change the car's mode. '''
        if new_mode in ["normal", "eco"]:
            self.mode = new_mode
            print(f"Mode changed to {self.mode}.")
        else:
            print("Invalid mode. Please choose between 'normal' or 'eco'.")

    def move_forward(self):
        ''' Set the speed to [depentend of mode] and updating the status. '''
        self.status = "Moving"
        print("The vehicule is moving forward.")
        if self.mode == "normal":
            self.speed = 50
        elif self.mode == "eco":
            self.speed = 30

    def stop(self):
        ''' Stop the car by setting the speed to 0 and updating the status. '''
        self.speed = 0
        self.status = "Stopped"
        print("The vehicule has stopped.")

    def respond_to_obstacle(self, distance):
        """ Respond to an obstacle detected by the car. This method is intended to be
        overridden by subclasses.
        Args:
            distance (float): The distance to the detected obstacle. """
        _ = distance # Unused argument as this is a template method
        print(f"{self.model} detects an obstacle.")