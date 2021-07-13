class Flight():
    # Method to create new flight
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    #method to add a passenger
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    #method to return number of open seats
    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)
people = ["An", "Qn", "En", "jen"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to filght successful")
    else:
        print(f"No seats available for {person}")