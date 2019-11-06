class Location:

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

class Trip:

    def __init__(self):
        self.stops = []
    
    def add_destination(self, city):
        self.stops.append(city)
    
    def travel(self):
        print("Began trip.")
        for index in range(0, len(self.stops) - 1):
            print(f'Travelled from {self.stops[index]} to {self.stops[index + 1]}')
        print('Ended trip.')
        # print(len(self.stops))


toronto = Location("Toronto")
ottawa = Location("Ottawa")
montreal = Location("Montreal")
quebec = Location("Quebec City")
halifax = Location("Halifax")
stjohns = Location("St. John's")


tour = Trip()
tour.add_destination(toronto)
tour.add_destination(ottawa)
tour.add_destination(montreal)
tour.add_destination(quebec)
tour.add_destination(halifax)
tour.add_destination(stjohns)
tour.travel()



