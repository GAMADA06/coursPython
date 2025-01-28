class Vehicle:
    def move(self):
        return "Moving."


class Car(Vehicle):
    def move(self):
        return "Driving on the road."


class Boat(Vehicle):
    def move(self):
        return "Sailing on water."


# Exemple d'utilisation
vehicles = [Car(), Boat()]
for vehicle in vehicles:
    print(vehicle.move())
