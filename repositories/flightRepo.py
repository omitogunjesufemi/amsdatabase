from models.flight import Flight
from repositories.baseRepo import BaseRepository


class FlightRepository(BaseRepository):
    def __int__(self):
        super().__init__()
        self.db = BaseRepository.db

    def create(self, flight: Flight):
        cursor = self.db.cursor()
        sql = "INSERT INTO flights(craft_id, flight_no, departure, departureTime, arrival, arrivalTime) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (flight.craft_id, flight.flight_no, flight.departure, flight.departure_time, flight.arrival, flight.arrival_time)
        cursor.execute(sql, val)
        self.db.commit()

    def update(self, flight_no, flight: Flight):
        cursor = self.db.cursor()
        sql = "UPDATE flights SET craft_id = %s, departure = %s, arrival = %s WHERE flight_no = %s"
        val = (flight.craft_id, flight.departure, flight.arrival, flight_no)
        cursor.execute(sql, val)
        self.db.commit()

    def show(self):
        cursor = self.db.cursor()
        sql = "SELECT a.craft_regNo, f.flight_no, f.departure, f.departureTime, f.arrival, f.arrivalTime FROM flights f JOIN aircrafts a ON a.id = f.craft_id"
        cursor.execute(sql)
        result = cursor.fetchall()
        for record in result:
            if record == None:
                print("Nothing to display")
            else:
                craft_id, flight_no, departure, departure_time, arrival, arrival_time = record
                flight = Flight(craft_id, flight_no, departure, departure_time, arrival, arrival_time)
                print(flight)


    def findREC(self, flight_no):
        cursor = self.db.cursor()
        sql = "SELECT a.craft_regNo, f.flight_no, f.departure, f.departureTime, f.arrival, f.arrivalTime FROM flights f JOIN aircrafts a ON a.id = f.craft_id WHERE flight_no = %s"
        val = (flight_no,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        craft_regNo = result[0]
        flight_no = result[1]
        departureTime = result[3]
        arrivalTime = result[5]
        record = [craft_regNo, flight_no, departureTime, arrivalTime, ]
        return record

    def findID(self, flight_no):
        cursor = self.db.cursor()
        sql = "SELECT id from flights WHERE flight_no = %s"
        val = (flight_no,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result[0]

    def findFlightCraftId(self, flight_no):
        cursor = self.db.cursor()
        sql = "SELECT craft_id from flights WHERE flight_no = %s"
        val = (flight_no,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result[0]



    def find(self, flight_no):
        cursor = self.db.cursor()
        sql = "SELECT a.craft_regNo, f.flight_no, f.departure, f.departureTime, f.arrival, f.arrivalTime FROM flights f JOIN aircrafts a ON a.id = f.craft_id WHERE flight_no = %s"
        val = (flight_no,)
        cursor.execute(sql,val)
        result = cursor.fetchone()
        craft_id, flight_no, departure, departure_time, arrival, arrival_time = result
        flight = Flight(craft_id, flight_no, departure, departure_time, arrival, arrival_time)
        print(flight)

    def delete(self, flight_no):
        cursor = self.db.cursor()
        self.find(flight_no)
        sql = "DELETE FROM flights WHERE flight_no = %s"
        val = (flight_no,)
        cursor.execute(sql, val)
        self.db.commit()