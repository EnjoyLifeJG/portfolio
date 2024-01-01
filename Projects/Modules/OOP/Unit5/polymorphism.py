# By Jean-G. De Souza
# Essex University Online
# PG Cert in Computer Science - Module OOP: Unit 5
# Activity instructions: Write a Python program with polymorphism that is usable within the summative assessment for the driverless car.

# --------------------------

class DriverlessCar:
    """ Class for a driverless car. """

    def __init__(self, model):
        """ Initialize a new DriverlessCar instance. """
        self.model = model
        self.speed = 0
        self.status = "Stopped"

    def move_forward(self):
        """ Move the car forward by setting the speed to 30 and updating the status. """
        self.speed = 30
        self.status = "Moving"
        print(f"{self.model} is moving forward.")

    def stop(self):
        """ Stop the car by setting the speed to 0 and updating the status. """
        self.speed = 0
        self.status = "Stopped"
        print(f"{self.model} has stopped.")

    def respond_to_obstacle(self, distance):
        """ Respond to an obstacle detected by the car. This method is intended to be
        overridden by subclasses.
        Args:
            distance (float): The distance to the detected obstacle. """
        _ = distance # Unused argument as this is a template method
        print(f"{self.model} detects an obstacle.")


class ObstacleDetectionSystem(DriverlessCar):
    """ A subclass of DriverlessCar, equipped with an obstacle detection system.
    Overrides the respond_to_obstacle method to provide specific reactions when an obstacle is detected. """

    def respond_to_obstacle(self, distance):
        """ Override the respond_to_obstacle method to handle obstacles based on their distance."""
        print(f"{self.model} detects an obstacle at {distance} meters.")
        if distance < 10:
            self.stop()
        elif distance < 30:
            self.slow_down()

    def slow_down(self):
        """ Reduce the speed of the car to slow down when approaching an obstacle. """
        self.speed = 15
        print(f"{self.model} is slowing down due to an obstacle ahead.")

# Use case
car = ObstacleDetectionSystem("Driverless car")
car.move_forward()
car.respond_to_obstacle(10)
