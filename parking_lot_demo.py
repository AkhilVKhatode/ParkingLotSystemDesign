from parking_lot import ParkingLot
from level import Level
from car import Car
from motorcycle import Motorcycle
from truck import Truck

class ParkingLotDemo:
    def run():
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1, 100))
        parking_lot.add_level(Level(2, 80))

        car = Car("CAR123")
        truck = Truck("Truck")
        motorcycle = Motorcycle("M1234")

        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(truck)
        parking_lot.park_vehicle(motorcycle)

        parking_lot.display_availability()
        parking_lot.unpark_vehicle(truck)
        parking_lot.display_availability()

if __name__ == "__main__":
    ParkingLotDemo.run()