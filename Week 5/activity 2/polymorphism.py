# Activity 2: Polymorphism Challenge!
class Vehicle:
    def __init__(self, name, color, max_speed):
        self.name = name
        self.color = color
        self.max_speed = max_speed

    def move(self):
        return "The vehicle is moving."

    def get_specs(self):
        return f"{self.color} {self.name}, Max Speed: {self.max_speed}"


class Car(Vehicle):
    def __init__(self, name, color, max_speed, fuel_type):
        super().__init__(name, color, max_speed)
        self.fuel_type = fuel_type

    def move(self):
        return f"The {self.name} is driving on the road with a vrooooom! 🚗"


class Plane(Vehicle):
    def __init__(self, name, color, max_speed, airline):
        super().__init__(name, color, max_speed)
        self.airline = airline

    def move(self):
        return f"The {self.name} is flying high in the sky! ✈️"


class Boat(Vehicle):
    def __init__(self, name, color, max_speed, boat_type):
        super().__init__(name, color, max_speed)
        self.boat_type = boat_type

    def move(self):
        return f"The {self.name} is sailing across the water! 🚢"


# Demonstration
def main():
    print("\nVEHICLE POLYMORPHISM DEMONSTRATION")
    print("--------------------------------")

    # Create vehicle instances
    sedan = Car("Toyota Camry", "Blue", 120, "Gasoline")
    jet = Plane("Boeing 747", "White", 900, "Delta Airlines")
    yacht = Boat("Sea Breeze", "White", 30, "Luxury Yacht")

    # Store vehicles in a list to demonstrate polymorphism
    vehicles = [sedan, jet, yacht]

    # Call the move method on each vehicle to show polymorphic behavior
    for vehicle in vehicles:
        print(f"\n{vehicle.get_specs()}")
        print(vehicle.move())

# Run the main function
if __name__ == "__main__":
    main()