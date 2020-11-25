class Flight:
    craft_id: int
    flight_no: str
    departure: str
    departure_time: str
    arrival: str
    arrival_time: str

    def __init__(self, craft_id: int, flight_no: str, departure: str, departure_time: str, arrival: str, arrival_time: str):
        self.craft_id = craft_id
        self.flight_no = flight_no
        self.departure = departure
        self.departure_time = departure_time
        self.arrival = arrival
        self.arrival_time = arrival_time

    def __str__(self):
        return f"{self.craft_id}\t\t{self.flight_no:<15}{self.departure:<10}{self.departure_time}\t\t{self.arrival:<10}{self.arrival_time}"