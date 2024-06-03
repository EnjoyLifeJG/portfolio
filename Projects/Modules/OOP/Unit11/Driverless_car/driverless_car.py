'''
Student ID 12694149
Essex University Online
PG Cert in Computer Science - Module OOP: Unit 11

Activity instructions:
  " You are now required to implement the code designed to support the operation of a driverless car
    as described in Unit 7. This should be representative of the use case diagram, activity diagram,
    class diagram, sequence diagram, and state transition diagram defined in your design document.
    [...]
    Please write and test your scripts in Codio using the Python workspace created for you.
    All code scripts must be documented, explained, and follow best practices.
    You should ensure that your code is fully tested and provide evidence of your testing.
    Use Python's assert statement to achieve automated testing, in addition to any other types of
    testing you believe are useful in this deployment. Additionally, you should submit a commentary
    evaluating your approach and reflecting on the development process.
    This commentary should also be part of your README file/documentation (600 words)."
    
The design of this software system of a driverless car focuses around three essential operations:
Obstacle Detection and Avoidance, Traffic Sign Recognition, and Automated Parking.

'''

# --------------------------

class EnvironmentalDataSimulator:
    """Simulate environmental data for vehicle."""
    def __init__(self):
        # Initialize empty dictionary to store simulated data.
        self.simulateData = {}

    def generateData(self):
        """Generate pre defined simulated environmental data."""
        self.simulateData = {
            "traffic_sign": "50",
            "obstacles": {
                "objectType": "pedestrian","objectDistance": 3.5, # Distance in meters
                },
            "parking_space": {
                "type": "Perpendicular Back Parking",
                "isAccessible": False,
                "depth": 5.0,  # in meters
                "width": 2.5,  # in meters
                },
            "coordinates": {"x": 2.2944640456375662, "y": 48.858221628649794}, # Long/Lat coordinates of the Eiffel Tower
            "current_parameters": {
                "currentSpeed": 61,
                "currentSteeringAngle": 0 # percentage of turning capacity of the wheel (negative for counterclock)
            }
        }
        return self.simulateData

class SensorManager:
    """Manage collection and processing of data from sensors."""
    def __init__(self, simulator):
        self.sensorsData = []  # Queue for storing sensor data
        self.simulator = simulator  # EnvironmentalDataSimulator instance

    def gatherData(self):
        """Gather data from simulator and append it to sensorsData queue."""
        simulated_data = self.simulator.generateData()
        self.sensorsData.append(simulated_data)

    def processData(self):
        """Process first item in queue if available and return it."""
        if self.sensorsData:
            return self.sensorsData.pop(0)
        return None

class TrafficSignRecognizer:
    """Recognize and interpret traffic signs from sensor data."""
    def __init__(self, vehicle_controller):
        self.recognizedSigns = []  # Queue for storing recognized signs
        self.isVehicleCompliant = True  # compliant by default
        self.vehicle_controller = vehicle_controller  # Instance of VehicleController

    def recognizeSigns(self, sensor_data):
        """Check if sensor data contains a traffic sign and add it to the queue."""
        if "traffic_sign" in sensor_data:
            self.recognizedSigns.append(sensor_data["traffic_sign"])

    def interpretSigns(self):
        """Interpret first recognized sign if available and check compliance."""
        if self.recognizedSigns:
            sign = self.recognizedSigns.pop(0)
            print(f"Interpreted traffic sign: {sign}")
            if sign.isdigit(): # For speed limit signs
                speedLimit = int(sign)  # Convert speed limit sign to integer
                currentSpeed = self.vehicle_controller.speed
                if currentSpeed > speedLimit:
                    self.isVehicleCompliant = False
                    print(f"Vehicle is not compliant: current speed {currentSpeed} exceeds limit {speedLimit}. Adapting behavior.")
                    self.adaptVehicleBehaviour(speedLimit)
                else:
                    self.isVehicleCompliant = True
                    print(f"Vehicle current speed of {currentSpeed} is compliant with the speed limit of {speedLimit}.")
            else: # For non speed limit signs
                print(f"Sign '{sign}' is not a speed limit sign.")

    def adaptVehicleBehaviour(self, speedLimit):
        """Adapt vehicle behavior to comply."""
        currentSpeed = self.vehicle_controller.speed
        while currentSpeed > speedLimit:
            speedDifference = currentSpeed - speedLimit
            brakingIntensity = min(1, speedDifference / currentSpeed)  # Calculate braking intensity within the loop for smooth braking
            self.vehicle_controller.brake(brakingIntensity)
            currentSpeed = self.vehicle_controller.speed  # Updated speed after braking
            print(f"Applying brakes with intensity: {brakingIntensity*100}%. Current speed: {currentSpeed}km/h, target: {speedLimit}km/h")

class ObstacleDetector:
    """
    Detect and manage objects and obstacles, evaluate avoidability and
    determine action to minimize harm (trolley dilemma).
    """
    def __init__(self, vehicleController, sensorManager):
        # Dictionary with known, pre defined object types and their pre set fragility index
        self.knownObjects = {
            "non-human": 0.2,  # public bench, tree, garbage bin, etc
            "pedestrian": 0.8,
            "group of pedestrians": 1.0,
            "cyclist": 0.7, # slightly less fragile than pedestrian because more likely to have a helmet
            "vehicle": 0.3,
            "animal": 0.5,
            "motorcycle": 0.6
        }
        self.detectedObjects = []  # Initiate stack for detected objects
        self.avoidancePriority = []  # Initiate queue for avoidance priority
        self.vehicleController = vehicleController  # Instance of VehicleController
        self.sensorManager = sensorManager  # Instance of SensorManager
        
    def update(self):
        sensorData = self.sensorManager.processData()
        if sensorData is not None:
            self.gatherData(sensorData)

    def gatherData(self, sensorData):
        """
        Gather data from sensors for type, distance, avoidability based on current speed and object distance.
        """
        if "obstacles" in sensorData:  # Check if obstacles data exists
            obstacles = sensorData["obstacles"]
            # Check if obstacles is list to also handle case of multiple obstacles
            if isinstance(obstacles, list):
                for obstacle in obstacles:
                    self.processObstacleData(obstacle)
            else:  # Single obstacle case, as a dictionary
                self.processObstacleData(obstacles)

    def processObstacleData(self, obstacle):
        """
        Process single obstacle data and append it to detectedObjects.
        """
        obstacleData = {
            "objectType": obstacle["objectType"],
            "objectDistance": obstacle["objectDistance"],
            "isAvoidable": self.evaluateAvoidability(obstacle["objectDistance"]),
            "fragilityIndex": self.knownObjects.get(obstacle["objectType"], 0)
        }
        self.detectedObjects.append(obstacleData)


    def evaluateAvoidability(self, objectDistance):
        """
        Evaluate if obstacle is avoidable based on distance and
        the vehicle's speed using simplified formula for braking distance.
        """
        currentSpeed = self.vehicleController.speed
        deceleration = 7.5  # Average deceleration in m/s^2
        brakingDistance = (((currentSpeed / 3.6) ** 2) / (2 * deceleration))
        return objectDistance >= brakingDistance

    def processData(self):
        """Sort detectedObjects into the avoidancePriority queue based on fragility index."""
        while self.detectedObjects:
            obj = self.detectedObjects.pop()
            index = 0
            while index < len(self.avoidancePriority) and self.avoidancePriority[index]["fragilityIndex"] > obj["fragilityIndex"]:
                index += 1
            self.avoidancePriority.insert(index, obj)

    def avoidObstacle(self):
        """Avoid highest priority obstacle using vehicleController methods"""
        if self.avoidancePriority:
            obstacle = self.avoidancePriority.pop(0)
            if obstacle["isAvoidable"]:
                print(f"Braking to avoid {obstacle['objectType']}.")
                self.vehicleController.brake(1) # breaking intensity of 100%
            else: # if cannot break on time: basic avoidance strategy by swerving
                print(f"Swerving to avoid {obstacle['objectType']}.")
                self.vehicleController.swerve()
        else:
            print("No obstacles in view.")

class ParkingAssistant:
    """Manage autonomous parking operations."""
    def __init__(self, sensorManager, vehicleController):
        self.sensor_manager = sensorManager
        self.vehicleController = vehicleController
        self.parkingSpace = None
        self.parkingRequested = False

    def requestParking(self):
        """Request parking based on user input."""
        self.parkingRequested = True
        self.findSpace()

    def findSpace(self):
        """Find parking space using sensor data and AvailableParking."""
        availableParking = AvailableParking(self.sensor_manager)
        if availableParking.isAccessible:
            self.parkingSpace = {
                "type": availableParking.parkingType,
                "depth": availableParking.depth,
                "width": availableParking.width,
                "isAccessible": availableParking.isAccessible
            }
            print(f"Found parking space: {self.parkingSpace['type']}")
            self.parkVehicle()
        else:
            print("No suitable parking space found.")

    def parkVehicle(self):
        """Execute maneuvers to park the vehicle. Very complex logic needed for self-parking.
        As it is not the main focus of this assignment, I did not implemented it.
        """
        print("Parking vehicle.")

class AvailableParking:
    """Represent a potential parking spot, fetching details from SensorManager, and compares it against car dimensions."""
    def __init__(self, sensor_manager):
         # Car dimensions (Height, Length, Width in meters) - taken as an example from a Volkswagen Golf5 2005
        self.my_dimensions = {
            "height": 1.47, # for potential future implementations of height control - not in use at the moment
            "length": 4.25,
            "width": 1.76
        }
        parking_data = self.get_parking_data(sensor_manager)
        if parking_data:
            self.parkingType = parking_data.get('type', 'unknown')
            self.depth = parking_data.get('depth', 0)
            self.width = parking_data.get('width', 0)
            self.isAccessible = self.check_accessibility(parking_data) # Determine if parking spot is accessible based on car dimensions
        else:
            self.initialize_default_values()
            
    def initialize_default_values(self):
        """Initialize default values for parking space properties."""
        self.parkingType = 'unknown'
        self.depth = 0
        self.width = 0
        self.isAccessible = False

    def get_parking_data(self, sensor_manager):
        """Retrieve parking space data from sensor manager."""
        sensor_data = sensor_manager.processData()
        if sensor_data and "parking_space" in sensor_data:
            return sensor_data["parking_space"]
        return None

    def check_accessibility(self, parking_data):
        """Check if parking spot is accessible based on car's dimensions + additional 10% space for doors."""
        required_length = self.my_dimensions["length"] * 1.1
        required_width = self.my_dimensions["width"] * 1.1
        if parking_data["depth"] >= required_length and parking_data["width"] >= required_width:
            return True
        return False
    

class VehicleController:
    """Controls the vehicle's movement and state."""
    def __init__(self):
        self.x = 0.0 # x coordinate
        self.y = 0.0 # y coordinate
        self.speed = 0.0 # Initial speed in km/h
        self.steering_angle = 0.0 # Initial steering wheel position (in percentage of turning capacity)
        self.state = '' # Vehicle's initial state

    def accelerate(self, increment):
        """Increase vehicle's speed."""
        self.speed += increment
        self.state = (f"Accelerating by {increment}.")
        print(self.state)

    def brake(self, brakingIntensity):
        """Decrease vehicle's speed."""
        self.speed = max(0, self.speed - brakingIntensity * self.speed)  # Ensure speed doesn't go negative
        self.state = (f"Braking with {brakingIntensity * 100}% intensity.")
        print(self.state)

    def turn(self, angle):
        """Change vehicle's steering angle."""
        self.steering_angle += angle
        self.state = (f"Turning by {angle}% of turning capacity.")
        print(self.state)

    def swerve(self):
        """Emergency collision avoidance strategy when simply breaking is not enough"""
        self.brake = 1 # break with 100% breaking intensity
        self.steering_angle = -0.5  # Example swerving: turn the wheel counterclock (vehicle to the Left) by 50% of capacity
        self.state = ("Emergency swerving.")
        print("Emergency maneuver executed. If emergency care is needed, call 112 (across Europe).")

    def updatePosition(self, sensor_manager):
        """Update vehicle's position based on sensor data."""
        sensor_data = sensor_manager.processData()
        if sensor_data and 'coordinates' in sensor_data:
            self.x = sensor_data['coordinates'].get('x', self.x)
            self.y = sensor_data['coordinates'].get('y', self.y)
            print(f"Updated position to x: {self.x}, y: {self.y}")
    
    def updateCurrentParameters(self, current_parameters):
        """Update vehicle's current speed and steering angle based on sensor data."""
        if 'currentSpeed' in current_parameters:
            self.speed = current_parameters['currentSpeed']
        if 'currentSteeringAngle' in current_parameters:
            self.steering_angle = current_parameters['currentSteeringAngle']



    # --------------- TESTING ---------------- #

if __name__ == "__main__":
    # Instantiate classes for testing
    edSimulator = EnvironmentalDataSimulator()
    sensorManager = SensorManager(edSimulator)
    vehicle_controller = VehicleController()
    tsRecognizer = TrafficSignRecognizer(vehicle_controller)
    parking_assistant = ParkingAssistant(sensorManager, vehicle_controller)


    # ~~~~~~~~~ Test 1 ~~~~~~~~~~~
    print("Test 1:")
    # Generate and process data
    simulated_data = edSimulator.generateData()
    assert "traffic_sign" in simulated_data, "Simulated data must include traffic sign."
    assert "obstacles" in simulated_data, "Simulated data must include obstacles."
    assert "coordinates" in simulated_data, "Simulated data must include coordinates."
    assert "current_parameters" in simulated_data, "Simulated data must include current parameters."

    sensorManager.gatherData()
    sensorData = sensorManager.processData()
    assert sensorData is not None, "Sensor data should not be None after gathering data."
    # Update vehicle's position based on sensor data
    vehicle_controller.updatePosition(sensorManager)
    
    print("Test 1 completed: passed.")


   # ~~~~~~~~~ Test 2 ~~~~~~~~~~~
    # Update vehicle's current parameters based on sensor data
    print("Test 2:")
    if 'current_parameters' in sensorData:
        vehicle_controller.updateCurrentParameters(sensorData['current_parameters'])
    expected_speed = simulated_data["current_parameters"]["currentSpeed"]
    assert vehicle_controller.speed == expected_speed, f"Vehicle speed should be {expected_speed} before adaptation."

    # Recognize signs and interpret them for compliance check
    tsRecognizer.recognizeSigns(sensorData)
    tsRecognizer.interpretSigns()
    
    print("Test 2 completed: passed.")


    # ~~~~~~~~~ Test 3 ~~~~~~~~~~~
    # Check for compliance after potential adaptation
    print("Test 3:")
    speed_limit = int(simulated_data["traffic_sign"])
    adapted_speed = vehicle_controller.speed
    assert adapted_speed <= speed_limit, f"After adaptation, vehicle speed ({adapted_speed}) should be compliant with the speed limit of {speed_limit}."
    
    print("Test 3 completed: passed.")


    # ~~~~~~~~~ Test 4 ~~~~~~~~~~~
    # Simulate 1 obstacle detection scenario
    print("Test 4:")
    sensorManager.sensorsData.append({
        "obstacles": {"objectType": "pedestrian", "objectDistance": 10.0},
        "current_parameters": {"currentSpeed": 50}
        })

    # Process data and update Obstacle Detector
    obstacleDetector = ObstacleDetector(vehicle_controller, sensorManager)
    obstacleDetector.update()

    # Check if obstacle was detected and added to detectedObjects
    assert len(obstacleDetector.detectedObjects) > 0, "Obstacle should be detected."

    # Process data for avoidance priority
    obstacleDetector.processData()

    # Check isAvoidable 
    one_obstacle = obstacleDetector.avoidancePriority[0]  # Get the first (highest priority) obstacle
    print(f"Obstacle is {'avoidable' if one_obstacle['isAvoidable'] else 'not avoidable'}.")

    # Perform avoidance
    obstacleDetector.avoidObstacle()
    
    print("Test 4 completed: passed.")   
    
    
    # ~~~~~~~~~ Test 5 ~~~~~~~~~~~
    # Simulate "trolley problem" for priority avoidance by fragility index, not matter the order of appearence
    print("Test 5:")
    obstacle_to_avoid = "group of pedestrians" #should be an element with a higher fragility index than secondary object - check dictionary "knownObjects" if needed
    secondary_object = "non-human"
    sensorManager.sensorsData.append({
        "obstacles": [
            {"objectType": secondary_object, "objectDistance": 7.0}, # Here, secondary object appears first in front of vehicle to make sure sorting by fragility index
            {"objectType": obstacle_to_avoid, "objectDistance": 3.0}
        ],
        "current_parameters": {"currentSpeed": 50}
    })

    # Process data and update Obstacle Detector
    obstacleDetector = ObstacleDetector(vehicle_controller, sensorManager)
    obstacleDetector.update()

    # Check if obstacles were detected and added to detectedObjects
    assert len(obstacleDetector.detectedObjects)  == 2, "Two obstacles should have been detected."
    
    # Process data for avoidance priority
    obstacleDetector.processData()
    
    print(obstacleDetector.avoidancePriority[0]['objectType'])

    # Check prioritization logic: if objects were indeed re sorted by fragility index: obstacle_to_avoid should be [0] on avoidancePriority
    assert obstacleDetector.avoidancePriority[0]['objectType'] == obstacle_to_avoid, "Priority object non prioritized"

    # Check is avoidable for the first obstacle
    print(f"Obstacle to avoid is {'avoidable' if obstacleDetector.avoidancePriority[0]['isAvoidable'] == True else 'not avoidable'}.")

    print("Test 5 completed: passed.")

    # Perform avoidance
    obstacleDetector.avoidObstacle()
    

    # ~~~~~~~~~ Test 6 ~~~~~~~~~~~
    # Simulate finding suitable parking space
    print("Test 6:")
    # Simulate parking space data in sensorManager
    sensorManager.sensorsData.append({
        "parking_space": {
            "type": "Parallel",
            "isAccessible": True,
            "depth": 5.5,  # Slightly larger than (car's length + 10%)
            "width": 2.0   # Slightly larger than (car's width + 10%)
        }
    })

    # Trigger parking space search
    parking_assistant.requestParking()

    # Expected criteria
    expected_parking_type = "Parallel"
    is_accessible = parking_assistant.parkingSpace["isAccessible"]
    found_parking_type = parking_assistant.parkingSpace["type"]

    assert is_accessible, "Test 6: The parking space should be accessible."
    assert found_parking_type == expected_parking_type, f"Test 6: The parking space type should be '{expected_parking_type}'."
    
    print("Test 6 completed: passed.")
    
    
    # ~~~~~~~~~ Test 7 ~~~~~~~~~~~
    # Verify Coordinates at Eiffel Tower
    print("Test 7:")
    # Expected coordinates of the Eiffel Tower
    expected_coordinates = {"x": 2.2945, "y": 48.8584} #approx.

    # Update coordinates
    sensorManager.gatherData()
    vehicle_controller.updatePosition(sensorManager)

    # Fetch current vehicle coordinates
    current_coordinates = {"x": vehicle_controller.x, "y": vehicle_controller.y}
    print(current_coordinates)
    # Calculate difference to allow for minor precision variations
    coordinate_tolerance = 0.001
    x_difference = abs(current_coordinates["x"] - expected_coordinates["x"])
    y_difference = abs(current_coordinates["y"] - expected_coordinates["y"])

    assert x_difference <= coordinate_tolerance and y_difference <= coordinate_tolerance, f"The coordinates should be at the Eiffel Tower in Paris. Expected approximately {expected_coordinates}, but found {current_coordinates}."

    print("Test 7 completed: passed. Welcome to Paris !")


    print("All tests passed successfully.")