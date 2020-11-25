from models.passenger import Passenger
from repositories.baseRepo import BaseRepository
class PassengerRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.db = BaseRepository.db

    def create(self, passenger: Passenger):
        cursor = self.db.cursor()
        sql = "INSERT INTO passengers(firstName, lastName, email, phone, address, gender) VALUES ( %s, %s, %s, %s, %s, %s)"
        val = (passenger.first_name, passenger.last_name, passenger.email, passenger.phone, passenger.address, passenger.gender)
        cursor.execute(sql, val)
        self.db.commit()
        passenger.id = cursor.lastrowid

    def update(self, phone, passenger: Passenger):
        cursor = self.db.cursor()
        sql = "UPDATE passengers SET firstName = %s, lastName = %s, address = %s, gender = %s WHERE phone = %s"
        val = (passenger.first_name, passenger.last_name, passenger.address, passenger.gender, phone)
        cursor.execute(sql, val)
        self.db.commit()

    def show(self):
        cursor = self.db.cursor()
        sql = "SELECT firstName, lastName, email, phone, address, gender FROM passengers"
        cursor.execute(sql)
        result = cursor.fetchall()
        for record in result:
            if record == None:
                print("Nothing to display")
            else:
                first_name, last_name, email, phone, address, gender = record
                passenger = Passenger(first_name, last_name, email, phone, address, gender)
                print(passenger)

    def find(self, phone):
        cursor = self.db.cursor()
        sql = "SELECT firstName, lastName, email, phone, address, gender FROM passengers WHERE phone = %s"
        val = (phone,)
        cursor.execute(sql,val)
        result = cursor.fetchone()
        first_name, last_name, email, phone, address, gender = result
        passenger = Passenger(first_name, last_name, email, phone, address, gender)
        print(passenger)

    def findEP(self, phone):
        cursor = self.db.cursor()
        sql = "SELECT firstName, lastName, email, phone, address, gender FROM passengers WHERE phone = %s"
        val = (phone,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        email = result[2]
        phone = result[3]
        gender = result[5]
        record = [email, phone, gender]
        return record

    def findID(self, phone):
        cursor = self.db.cursor()
        sql = "SELECT id FROM passengers WHERE phone = %s"
        val = (phone,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result[0]

    def delete(self, phone):
        cursor = self.db.cursor()
        self.find(phone)
        sql = "DELETE FROM passengers WHERE phone = %s"
        val = (phone,)
        cursor.execute(sql, val)
        self.db.commit()