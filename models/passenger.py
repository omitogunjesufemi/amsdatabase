class Passenger:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    gender: str

    def __init__(self, first_name: str, last_name: str, email: str, phone: str, address: str, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.gender = gender

    def __str__(self):
        return f"{self.first_name:<18}{self.last_name:<18}{self.email:<30}{self.phone:<15}{self.address:<25}{self.gender}"