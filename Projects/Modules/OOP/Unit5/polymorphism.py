class DriverlessCar:
    def __init__(self, model):
        self.model = model
        self.speed = 0
        self.status = "Stopped"

    def move_forward(self):
        self.speed = 30
        self.status = "Moving"
        print(f"{self.model} is moving forward.")

    def stop(self):
        self.speed = 0
        self.status = "Stopped"
        print(f"{self.model} has stopped.")

    def respond_to_obstacle(self, distance):
        # General response to an obstacle (overridden by subclass ObstacleDetectionSystem)
        print(f"{self.model} detects an obstacle.")

class ObstacleDetectionSystem(DriverlessCar):
    def respond_to_obstacle(self, distance):
        print(f"{self.model} detects an obstacle at {distance} meters.")
        if distance < 10:
            self.stop()
        elif distance < 30:
            self.slow_down()

    def slow_down(self):
        self.speed = 15
        print(f"{self.model} is slowing down due to an obstacle ahead.")

# Use case
car = ObstacleDetectionSystem("Driverless car")
car.move_forward()
car.respond_to_obstacle(10)