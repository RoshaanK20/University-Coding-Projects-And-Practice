class Vehicle:
    def __init__(self, brand, model, year, mileage, current_fuel_level):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage  # kilometers
        self.fuel_capacity = 64  # liters, can change
        self.fuel_efficiency = 23  # kilometers/liter, can change
        self.current_fuel_level = current_fuel_level  # liters

    def calculate_fuel_consumption(self, distance):
        fuel_needed = distance / self.fuel_efficiency
        if fuel_needed > self.current_fuel_level:
            print("Not enough fuel for the trip. You need to refuel.")
        else:
            print(f"Fuel Consumed: {fuel_needed:.2f} liters")

    def calculate_travel_time(self, distance, speed):
        if speed <= 0:
            print("Speed must be greater than 0 to calculate travel time.")
        else:
            travel_time = distance / speed
            print(f"Travel Time: {travel_time:.2f} hours")

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Mileage: {self.mileage} kilometers")
        print(f"Fuel Capacity: {self.fuel_capacity} liters")
        print(f"Fuel Efficiency: {self.fuel_efficiency} kilometers/liter")
        print(f"Current Fuel Level: {self.current_fuel_level} liters")

    def maintenance_schedule(self):
        print("Maintenance Schedule:")
        print("Oil Change: Every 5000 kilometers")
        print("Tire Rotation: Every 10,000 kilometers")
        print("Brake Inspection: Every 15,000 kilometers")

    def check_maintenance(self):
        if self.mileage >= 15000:
            print("Time for a brake inspection!")
        elif self.mileage >= 10000:
            print("Time for a tire rotation!")
        elif self.mileage >= 5000:
            print("Time for an oil change!")
        else:
            print("No maintenance needed yet.")

    def calculate_refueling_cost(self, distance, price_per_liter):
        fuel_needed = distance / self.fuel_efficiency
        if fuel_needed > self.current_fuel_level:
            refuel_cost = fuel_needed * price_per_liter
            print(f"Total Fuel Cost for the trip: PKR {refuel_cost:.2f}")
        else:
            remaining_fuel = self.current_fuel_level - fuel_needed
            print(f"Enough fuel for the trip. Remaining fuel: {remaining_fuel:.2f} liters")
            refuel_cost = fuel_needed * price_per_liter
            print(f"Fuel Cost for the trip: PKR {refuel_cost:.2f}")

def main():
    # Get user input
    brand = input("Enter vehicle brand: ")
    model = input("Enter vehicle model: ")
    year = int(input("Enter vehicle year: "))
    mileage = int(input("Enter vehicle mileage (kilometers): "))
    current_fuel_level = float(input("Enter current fuel level (liters): "))

    # Create an instance of the Vehicle class
    Car = Vehicle(brand, model, year, mileage, current_fuel_level)

    # Display vehicle details and perform calculations
    print("\nVehicle Details:")
    Car.display_details()

    distance = float(input("Enter distance to travel (kilometers): "))
    Car.calculate_fuel_consumption(distance)

    speed = float(input("Enter travel speed (km/h): "))
    Car.calculate_travel_time(distance, speed)

    Car.maintenance_schedule()
    Car.check_maintenance()

    price_per_liter = float(input("Enter fuel price per liter (PKR): "))
    Car.calculate_refueling_cost(distance, price_per_liter)

if __name__ == "__main__":
    main()