# Driverless Car System Assignment
Essex University Online<br>
PG Cert in Computer Science - Module OOP: Unit 11<br>
The design of this software system of a driverless car focuses around three essential operations:<br>
Obstacle Detection and Avoidance, Traffic Sign Recognition, and Automated Parking.<br>
569 words

## Installation
To run this software, ensure you have Python installed on your system. Clone the repository or download the source code to your local machine.<br>

```
git clone https://https://github.com/LeCodeByJean/portfolio/tree/303c4a06d8001159eaf37bd8d0cf811929741ae5/Projects/Modules/OOP/Unit11/Driverless_car
cd Driverless_car
```

The design choices and the structuring of this driverless car system were focused on the principles of Object-Oriented Programming and the need for a modular, scalable, and maintainable codebase.
The system is designed to support three chosen operations: Obstacle Detection and Avoidance, Traffic Sign Recognition, and Automated Parking, and is composed of seven classes, each encapsulating specific functionalities. This approach facilitates the extension, debugging, and maintenance of the system.

The “EnvironmentalDataSimulator” class was designed to mock the external environment by generating predefined data sets, ensuring that the system could be developed and tested without the need of any real-world data sources. The “generateData” method allows for easy expansion or modification of the simulated data.

The “SensorManager” class acts as an intermediary between the environmental data and the vehicle's processing units and demonstrates the use of the delegation pattern, where it delegates the task of data collection to the “EnvironmentalDataSimulator”. This pattern was chosen to decouple the data collection process from the data processing, allowing for different data sources to be integrated with minimal changes to the system.

The “VehicleController” class represents the core control system of the vehicle, encapsulating the logic for vehicle movement and state management. The methods within this class, such as “accelerate”, “brake”, and “turn”, are designed to reflect actions a real vehicle's control system might perform. This class is crucial for simulating the vehicle's responses to environmental data and commands from other system components. The initial design of this program included a separate "Coordinate" class to manage the vehicle's position, which was integrated directly into the "VehicleController" class during implementation, aiming to streamline the process of updating and accessing the vehicle's position.

The decision to separate the functionality of the autonomous vehicle system into distinct classes was driven by the principle of single responsibility and was particularly relevant for the "ObstacleDetector," class. Indeed, the "ObstacleDetector" class presented unique challenges, especially when considering the ethical implications of autonomous vehicle decision-making, famously illustrated by the Trolley dilemma. Implementing a system’s reaction to a situation where it must choose between the least unfavourable of two harmful outcomes, underscores the profound responsibility encoded within the obstacle detection and avoidance prioritization logic, introducing a layer of ethical and legal decision-making into the software development process.

Assert testing was employed to validate the functionality and reliability of components. For instance, tests for the EnvironmentalDataSimulator ensure that the generated data includes all necessary elements like traffic signs and obstacles, verifying the simulator's ability to provide comprehensive environmental data. Similarly, tests for the SensorManager check that data is correctly gathered and processed, confirming the manager's role as an effective intermediary.

The tests for the VehicleController focus on its response to the processed data, such as adapting the vehicle's speed based on traffic signs, ensuring that the vehicle behaves as expected in response to environmental conditions. The ObstacleDetector's tests validate its ability to detect, prioritize, and take the adequate action (breaking or swerving), highlighting the system's capability to handle dynamic scenarios.

In summary, the development of this driverless vehicle system was a comprehensive exercise in applying OOP principles to solve a complex problem. The modular design facilitated a clear separation of responsibilities, while assert testing ensured the reliability of each component.
