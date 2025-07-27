class Vehicle:
    def __init__(self, brand, model, year, mileage, current_fuel_level):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage  # kilometers
        self.fuel_capacity = 100  # liters, can change
        self.fuel_efficiency = 16  # kilometers/liter, can change
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
        oil_change_interval = 5000
        tire_rotation_interval = 10000
        brake_inspection_interval = 15000

        next_oil_change = oil_change_interval - (self.mileage % oil_change_interval)
        next_tire_rotation = tire_rotation_interval - (self.mileage % tire_rotation_interval)
        next_brake_inspection = brake_inspection_interval - (self.mileage % brake_inspection_interval)

        print("Maintenance Schedule:")
        print(f"Total Kilometers Traveled: {self.mileage} kilometers")
        print(f"Oil Change: Every {oil_change_interval} kilometers")
        print(f"Next Oil Change in: {next_oil_change} kilometers")
        print(f"Tire Rotation: Every {tire_rotation_interval} kilometers")
        print(f"Next Tire Rotation in: {next_tire_rotation} kilometers")
        print(f"Brake Inspection: Every {brake_inspection_interval} kilometers")
        print(f"Next Brake Inspection in: {next_brake_inspection} kilometers")

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