# ParkingLotSystemDesign

## Functional Requirements
1. The parking facility must consist of several floors, each containing a defined number of parking spaces.
2. It should accommodate various vehicle categories, including motorcycles, cars, and trucks.
3. Every parking space must be designated for a specific type of vehicle.
4. When a vehicle enters, the system should allocate an appropriate spot, and release it once the vehicle leaves.
5. It must maintain a live status of parking space availability and display this information to users.
6. The system should support multiple access points for entry and exit, managing concurrent requests efficiently.

## Core Classes, Interfaces, and Enums
1. ParkingLot: A singleton class that ensures a single shared instance across the application. It manages the list of parking levels and handles the logic for vehicle parking and removal.
2. Level: Models a floor within the lot. It keeps track of its parking spots and facilitates vehicle parking/unparking operations on that level.
3. ParkingSpot: Represents a single spot within the lot, maintaining whether it’s occupied and which vehicle is parked there.
4. Vehicle: An abstract class that serves as a blueprint for specific vehicle types like Car, Motorcycle, and Truck.
5. VehicleType: An enumeration defining supported vehicle categories.
6. Concurrency is handled using synchronized blocks to maintain thread safety during shared resource access.
7. Main: Acts as the entry point, demonstrating how the system functions.

## Applied Design Patterns
1. Singleton: Guarantees that only one instance of the parking lot exists throughout the application lifecycle.
2. Factory (optional): Can be used to instantiate vehicle objects dynamically based on the input type.
3. Observer (optional): Could be integrated to alert users when new parking spots become available.
