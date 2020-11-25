class Aircraft:
    id: int
    name: str
    type: str
    capacity: int
    reg_no: str

    def __init__(self, name: str, type: str, capacity: int, reg_no: str):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.reg_no = reg_no

    def __str__(self):
        return f"{self.name:<25}{self.type:<25}{self.capacity:<25}{self.reg_no}"