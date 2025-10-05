class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def book_ticket(self):
        if self.seats > 0:
            print(f"Ticket booked successfully! Your seat number is {self.seats}.")
            self.seats -= 1
        else:
            print("Sorry, no seats available.")

    def get_status(self):
        print(f"Number of available seats: {self.seats}")

    def get_fare(self):
        print(f"The fare for the train {self.name} is: {self.fare} INR")

intercity = Train("Intercity Express", 500, 3)
intercity.get_fare()
intercity.get_status()
intercity.book_ticket()
intercity.get_status()
