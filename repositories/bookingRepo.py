from models.booking import Booking
from repositories.baseRepo import BaseRepository
class BookingRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.db = BaseRepository.db

    def create(self, booking: Booking):
        cursor = self.db.cursor()
        sql = "INSERT INTO bookings(flight_id, passenger_id, flight_class, date, booking_ref, seat_number) VALUES ( %s, %s, %s, %s, %s, %s)"
        val = (booking.flight_id, booking.passenger_id, booking.flight_class, booking.date, booking.booking_ref, booking.seat_number)
        cursor.execute(sql, val)
        self.db.commit()
        booking.id = cursor.lastrowid

    def update(self, booking_ref, booking: Booking):
        cursor = self.db.cursor()
        sql = "UPDATE bookings SET flight_class = %s WHERE booking_ref = %s"
        val = (booking.flight_class, booking_ref)
        cursor.execute(sql, val)
        self.db.commit()

    def show(self):
        cursor = self.db.cursor()
        sql = "SELECT f.flight_no, p.firstName, p.lastName, p.phone, b.flight_class, b.date, b.booking_ref, b.seat_number FROM bookings b JOIN flights f ON f.id = b.flight_id JOIN passengers p ON p.id = b.passenger_id"
        cursor.execute(sql)
        result = cursor.fetchall()
        for record in result:
            if record == None:
                print("Nothing to display")
            else:
                flight_no, first_name, last_name, phone, flight_class, date, booking_ref, seat_number = record
                print(f"{flight_no:<18}{first_name:<18}{last_name:<18}{phone:<15}{flight_class:<15}{date}\t\t{booking_ref:<15}{seat_number}")

    def find(self, booking_ref):
        cursor = self.db.cursor()
        sql = "SELECT f.flight_no, p.firstName, p.lastName, p.phone, b.flight_class, b.date, b.booking_ref, b.seat_number FROM bookings b JOIN flights f ON f.id = b.flight_id JOIN passengers p ON p.id = b.passenger_id WHERE booking_ref = %s"
        val = (booking_ref,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        flight_no, first_name, last_name, phone, flight_class, date, booking_ref, seat_number = result
        print(f"{flight_no:<18}{first_name:<18}{last_name:<18}{phone:<15}{flight_class:<15}{date}\t\t{booking_ref:<15}{seat_number}")

    def findSeat(self):
        cursor = self.db.cursor()
        sql = "SELECT f.flight_no, p.firstName, p.lastName, p.phone, b.flight_class, b.date, b.booking_ref, b.seat_number FROM bookings b JOIN flights f ON f.id = b.flight_id JOIN passengers p ON p.id = b.passenger_id"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result



    def delete(self, booking_ref):
        cursor = self.db.cursor()
        self.find(booking_ref)
        sql = "DELETE FROM bookings WHERE booking_ref = %s"
        val = (booking_ref,)
        cursor.execute(sql, val)
        self.db.commit()