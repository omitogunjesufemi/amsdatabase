from datetime import date
class Booking:
    flight_id: int
    passenger_id: int
    flight_class: str
    date: str
    booking_ref: str
    seat_number: int

    def __init__(self, flight_id: int, passenger_id: int, flight_class: str,  date: str, booking_ref: str, seat_number: int):
        self.flight_id = flight_id
        self.passenger_id = passenger_id
        self.flight_class = flight_class
        self.date = date
        self.booking_ref = booking_ref
        self.seat_number = seat_number


    def __str__(self):
        return f"{self.flight_id:<16}{self.passenger_id:<19}{self.flight_class:<17}{self.date:<18}{self.booking_ref:16}{self.seat_number}"