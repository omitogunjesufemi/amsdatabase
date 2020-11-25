from models.aircraft import Aircraft
from repositories.baseRepo import BaseRepository
class AircraftRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.db = BaseRepository.db

    def create(self, aircraft: Aircraft):
        cursor = self.db.cursor()
        sql = "INSERT INTO aircrafts(craft_name, craft_type, craft_capacity, craft_regNo) VALUES (%s, %s, %s, %s)"
        val = (aircraft.name, aircraft.type, aircraft.capacity, aircraft.reg_no)
        cursor.execute(sql, val)
        self.db.commit()
        aircraft.id = cursor.lastrowid

    def update(self, id: int, aircraft: Aircraft):
        cursor = self.db.cursor()
        sql = "UPDATE aircrafts SET craft_regNo = %s, craft_type = %s, craft_capacity = %s, craft_name = %s WHERE id = %s"
        val = (aircraft.reg_no, aircraft.type, aircraft.capacity, aircraft.name, id)
        cursor.execute(sql, val)
        self.db.commit()

    def show(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM aircrafts"
        cursor.execute(sql)
        result = cursor.fetchall()
        for record in result:
            if record == None:
                print("Nothing to display")
            else:
                id, craft_name, craft_type, craft_capacity, craft_regNo = record
                aircraft = Aircraft(craft_name, craft_type, craft_capacity, craft_regNo)
                print(aircraft)

    def delete(self, id:int):
        cursor = self.db.cursor()
        self.find(id)
        sql = "DELETE FROM aircrafts WHERE id = %s"
        val = (id,)
        cursor.execute(sql,val)
        self.db.commit()

    def find(self, id: int):
        cursor = self.db.cursor()
        sql = "SELECT id, craft_name, craft_type, craft_capacity, craft_regNo FROM aircrafts WHERE id = %s"
        val = (id,)
        cursor.execute(sql,val)
        result = cursor.fetchone()
        id, craft_name, craft_type, craft_capacity, craft_regNo = result
        aircraft = Aircraft(craft_name, craft_type, craft_capacity, craft_regNo)
        print(aircraft)

    def findCraftId(self, craft_regNo):
        cursor = self.db.cursor()
        sql = "SELECT id FROM aircrafts WHERE craft_regNo = %s"
        val = (craft_regNo,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        record = result[0]
        return record

    def findCraftCapacity(self, craft_regNo):
        cursor = self.db.cursor()
        sql = "SELECT craft_capacity FROM aircrafts WHERE craft_regNo = %s"
        val = (craft_regNo,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        record = result[0]
        return record

    def findRegNo(self, id):
        cursor = self.db.cursor()
        sql = "SELECT craft_regNo FROM aircrafts WHERE id = %s"
        val = (id,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        record = result[0]
        return record

