# ParkingLotSystemDesign

## Functional Requirements
The parking facility must consist of several floors, each containing a defined number of parking spaces.
It should accommodate various vehicle categories, including motorcycles, cars, and trucks.
Every parking space must be designated for a specific type of vehicle.
When a vehicle enters, the system should allocate an appropriate spot, and release it once the vehicle leaves.
It must maintain a live status of parking space availability and display this information to users.
The system should support multiple access points for entry and exit, managing concurrent requests efficiently.

## Core Classes, Interfaces, and Enums
ParkingLot: A singleton class that ensures a single shared instance across the application. It manages the list of parking levels and handles the logic for vehicle parking and removal.
Level: Models a floor within the lot. It keeps track of its parking spots and facilitates vehicle parking/unparking operations on that level.
ParkingSpot: Represents a single spot within the lot, maintaining whether it’s occupied and which vehicle is parked there.
Vehicle: An abstract class that serves as a blueprint for specific vehicle types like Car, Motorcycle, and Truck.
VehicleType: An enumeration defining supported vehicle categories.
Concurrency is handled using synchronized blocks to maintain thread safety during shared resource access.
Main: Acts as the entry point, demonstrating how the system functions.

## Applied Design Patterns
Singleton: Guarantees that only one instance of the parking lot exists throughout the application lifecycle.
Factory (optional): Can be used to instantiate vehicle objects dynamically based on the input type.
Observer (optional): Could be integrated to alert users when new parking spots become available.
