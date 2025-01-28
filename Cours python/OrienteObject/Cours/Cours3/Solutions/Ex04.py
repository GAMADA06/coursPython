class Transport:
    def __init__(self, speed: float, capacity: int):
        self.speed = speed  # en km/h
        self.capacity = capacity

    def travel_time(self, distance: float) -> float:
        return distance / self.speed


class Bus(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed, capacity)


class Train(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed, capacity)


class Bicycle(Transport):
    def __init__(self, speed, capacity=1):
        super().__init__(speed, capacity)


# Exemple d'utilisation
bus = Bus(80, 50)
train = Train(200, 300)
bike = Bicycle(20)

distance = 100  # Distance en km

print(f"Temps de trajet en bus : {bus.travel_time(distance):.2f} heures")
print(f"Temps de trajet en train : {train.travel_time(distance):.2f} heures")
print(f"Temps de trajet en vélo : {bike.travel_time(distance):.2f} heures")
