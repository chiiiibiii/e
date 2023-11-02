class Human:
    def __init__(self, name="Human"):
        self.name = name
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []
    def add_passenger(self, *args):
        for passenger in args:
            self.passenger.append(passenger)
    def print_passengers_names(self):
        if self.passenger!= []:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passenger:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")
nick = Human("Nick")
kate = Human("Kate")
car = Auto("Mercedes")
car.add_passenger(nick, kate)
car.print_passengers_names()