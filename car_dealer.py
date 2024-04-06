from car import Car
# CarDealer class allows for dealerships to add storage.
class CarDealer:
    def __init__(self):
        self.inventory = []

    def add_car(self, make, model, year, mileage):
        car = Car(make, model, year, mileage)
        self.inventory.append(car)
        print(f"Car added sucessfully to inventory: {car.get_descriptive_name()}")

    def list_inventory(storage):
        print('Current inventory: ')
        for i, car in enumerate(storage.inventory, 1):
            print(f"{i}. {car.get_descriptive_name()}")
            
        

