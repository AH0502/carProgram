from car import Car
from car_dealer import CarDealer
def add_car():
    print("Would you like to add a vehicle to the database?")
    user_data = input().lower()
    if user_data == 'yes':
        print("Enter the make, model, and year followed by spaces: ")
        make, model, year = input().split()
        new_car = Car(make, model, year)
        print("Vehicle added to database successfully!")
        print(new_car.get_descriptive_name())
    else:
        print("Thank you for wasting my time!")

def startup():
    print('Thank you for using the self-service car database! For a list of availiable commands: Type "help"')
    user_input = input().lower()
    if user_input == 'help':
        help()
def main():
    print(f"0-Add Car\n1-Exit")
    user_input = input().lower()
def help():
    print(f"Availiable commands are: \n\n0-Add Car\n1-Exit")
    main()

startup()
    
          




    