from models.aircraft import Aircraft
from models.flight import Flight
from models.passenger import Passenger
from models.booking import Booking
from repositories.aircraftRepo import AircraftRepository
from repositories.flightRepo import FlightRepository
from repositories.passengerRepo import PassengerRepository
from repositories.bookingRepo import BookingRepository


aircraft_repository = AircraftRepository()
flight_repository = FlightRepository()
passenger_repository = PassengerRepository()
booking_repository = BookingRepository()


def main():
    flag = True
    while flag == True:
        mainmenu()
        command = int(input('Please input a command: '))
        if command == 0:
            flag = False
        elif command <= 4:
            subMenu(command)
        else:
            print(f"Your input does not exist!")
            backToMenu()

def backToMenu():
    answer = (input("Do you want to continue (y/n): ")).lower()
    if answer == "y":
        main()
    elif answer == "n":
        exit()
    else:
        print("Enter a valid answer: ")
        backToMenu()

def toContinue(handlerCall):
    answer = (input("Do you want to continue (y/n): ")).lower()
    if answer == "y":
        subMenu(handlerCall)
    elif answer == "n":
        exit()
    else:
        print("Enter a valid answer: ")
        toContinue(handlerCall)


# AIRCRAFT MANAGEMENT SERVICE MENU - (MAIN MENU)
def mainmenu():
    print(
        '''
Press 0 to exit
Press 1 for AircraftManagement
Press 2 for FlightManagement
Press 3 for Passenger Management
Press 4 for Booking Management
'''
    )

# COMMAND LINE FOR SUBMENU
def subMenu(command):
    if command == 1:
        aircraftMenu()
        new_command = int(input('Please input a command to perform an operation: '))
        aircraftHandler(new_command)


    elif command == 2:
        flightMenu()
        new_command = int(input('Please input a command to perform an operation: '))
        flightHandler(new_command)

    elif command == 3:
        passengerMenu()
        new_command = int(input('Please input a command to perform an operation: '))
        passengerHandler(new_command)

    elif command == 4:
        bookingMenu()
        new_command = int(input('Please input a command to perform an operation: '))
        bookingHandler(new_command)

    else:
        print(f"Your input does not exist!")
        backToMenu()


# AIRCRAFT MANAGEMENT SYSTEM SERVICE OPTION MENU (SUB-MENU)
def aircraftMenu():
    print(
        '''
Press 1 to add Aircraft
Press 2 to Search for an Aircraft
Press 3 to Update Aircraft
Press 4 to List Aircraft
Press 5 to Delete Aircraft
Press 0 to Go back to main menu
        '''
    )


def flightMenu():
    print('''
Press 1 to add Flight
Press 2 to Search for a Flight
Press 3 to Update Flight
Press 4 to List Flight
Press 5 to Delete Flight
Press 0 to go back to main menu
    ''')


def passengerMenu():
    print('''
Press 1 to add Passenger
Press 2 to Search for a Passenger
Press 3 to Update Passenger
Press 4 to List Passenger
Press 5 to Delete Passenger
Press 0 to go back to main menu
    ''')


def bookingMenu():
    print('''
Press 1 to add Booking
Press 2 to Search for a Booking
Press 3 to Update Booking
Press 4 to List Booking
Press 5 to Delete Booking
Press 0 to go back to main menu
    ''')

def emptyDetails(name, capacity, type, reg_no):
    if (name == "" or name == None or name == " ") and \
            (capacity == "" or capacity == None or capacity == " ") and \
            (type == "" or type == None or type == " ") and \
            (reg_no == "" or reg_no == None or reg_no == " "):
        print("This entry cannot be left blank!")
        aircraftHandler(1)

# AIRCRAFT MANAGEMENT SERVICE HANDLER
def aircraftHandler(new_command):
    if new_command == 0:
        pass

    elif new_command == 1:
        name = input('Enter the name of aircraft: ')
        capacity = int(input('Enter aircraft capacity: '))
        type = input('Enter the aircraft type: ')
        reg_no = input('Enter the registration number: ')
        emptyDetails(name, capacity, type, reg_no)
        aircraft = Aircraft(name, type, capacity, reg_no)
        aircraft_repository.create(aircraft)
        toContinue(1)

    elif new_command == 2:
        id = int(input('Enter the id of the aircraft: '))
        aircraft_repository.find(id)
        toContinue(1)

    elif new_command == 3:
        aircraft_repository.show()
        id = int(input('Enter the id of the aircraft: '))
        aircraft_repository.find(id)
        name = input('Enter the name of aircraft: ')
        capacity = int(input('Enter aircraft capacity: '))
        type = input('Enter the aircraft type: ')
        reg_no = input('Enter the registration number: ')
        emptyDetails(name, capacity, type, reg_no)
        aircraft = Aircraft(name, type, capacity, reg_no)
        aircraft_repository.update(id, aircraft)
        toContinue(1)

    elif new_command == 4:
        aircraft_repository.show()
        toContinue(1)

    elif new_command == 5:
        id = int(input('Enter the id of the aircraft: '))
        aircraft_repository.delete(id)
        toContinue(1)

    else:
        print('Your Input does not Exist')
        toContinue(1)


# FLIGHT MANGEMENT SERVICE HANDLER
def flightHandler(new_command):
    if new_command == 0:
        pass

    elif new_command == 1:
        aircraft_repository.show()
        craft_regNo = input('Enter the registration number of the aircraft: ')
        craft_id = aircraft_repository.findCraftId(craft_regNo)
        flight_no = input('Enter the flight number')
        departure = input('Enter your state of Departure: ')
        departure_time = input('Enter the departure time of flight: ')
        arrival = input('Enter your state of destination: ')
        arrival_time = input('Enter the arrival time of flight: ')
        flight = Flight(craft_id, flight_no, departure, departure_time, arrival, arrival_time)
        flight_repository.create(flight)
        toContinue(2)

    elif new_command == 2:
        flight_no = input('Please input the flight number: ')
        flight_repository.find(flight_no)
        toContinue(2)

    elif new_command == 3:
        flight_repository.show()
        flight_no = input('Enter the flight number: ')
        flight = flight_repository.findREC(flight_no)
        arrivalTime = flight[3]
        departureTime = flight[2]
        craft_regNo = input('Enter the registration number of the aircraft attached to flight: ')
        craft_id = aircraft_repository.findCraftId(craft_regNo)
        departure = input('Enter your state of Departure: ')
        arrival = input('Enter the arrival point: ')
        flight = Flight(craft_id, flight_no, departure, departureTime, arrival, arrivalTime)
        flight_repository.update(flight_no, flight)
        toContinue(2)

    elif new_command == 4:
        flight_repository.show()
        toContinue(2)

    elif new_command == 5:
        flight_no = input('Enter the flight number to delete the flight: ')
        flight_repository.delete(flight_no)
        toContinue(2)

    else:
        print('Your Input does not Exist')
        toContinue(2)



# PASSENGER MANAGEMENT SERVICE HANDLER
def passengerHandler(new_command):
    if new_command == 0:
        pass

    elif new_command == 1:
        first_name = input('Enter the first name of passenger: ')
        last_name = input('Enter the last name of passenger: ')
        email = input('Enter the passenger email: ')
        phone = input('Enter the passenger cell number: ')
        address = input('Enter the passenger address: ')
        gender = input('Enter passenger gender: ')
        passenger = Passenger(first_name, last_name, email, phone, address, gender)
        passenger_repository.create(passenger)
        toContinue(3)

    elif new_command == 2:
        phone = input('Enter the passenger cell number: ')
        passenger_repository.find(phone)
        toContinue(3)

    elif new_command == 3:
        phone = input('Enter the passenger cell number: ')
        passenger_repository.find(phone)
        not_to_be_changed = passenger_repository.findEP(phone)
        first_name = input('Enter the first name of passenger: ')
        last_name = input('Enter the last name of passenger: ')
        email = not_to_be_changed[0]
        address = input('Enter the passenger address: ')
        gender = not_to_be_changed[2]
        passenger = Passenger(first_name, last_name, email, phone, address, gender)
        passenger_repository.update(phone, passenger)
        toContinue(3)

    elif new_command == 4:
        passenger_repository.show()
        toContinue(3)

    elif new_command == 5:
        phone = input('Enter the passenger cell number: ')
        passenger_repository.delete(phone)
        toContinue(3)

    else:
        print('Your Input does not Exist')
        toContinue(3)

#SEAT NUMBERS
def seatNumberCounter(flight_no):
    count = 1
    seat = booking_repository.findSeat()
    for all in seat:
        if flight_no in all:
            count += 1
    return count

def seatNumberGenerator(flight_no, count):
    craft_id = flight_repository.findFlightCraftId(flight_no)
    craft_regNo = aircraft_repository.findRegNo(craft_id)
    craft_capacity = aircraft_repository.findCraftCapacity(craft_regNo)
    if count <= craft_capacity:
        seat_number = count
        return seat_number
    elif count > craft_capacity:
        return f"All seats are fully booked!"


# BOOKING MANAGEMENT SERVICE HANDLER
def bookingHandler(new_command):
    if new_command == 0:
        pass

    elif new_command == 1:
        phone = input('Enter the passenger cell number: ')
        passenger_id = passenger_repository.findID(phone)
        flight_no = input('Enter the flight number: ')
        flight_id = flight_repository.findID(flight_no)
        flight_class = input('Enter the ticket Class: ')
        date = input('Enter the date of booking: ')
        booking_ref = input('Enter the booking reference: ')
        seat_count = seatNumberCounter(flight_no)
        seat_number = seatNumberGenerator(flight_no, seat_count)

        booking = Booking(flight_id, passenger_id, flight_class, date, booking_ref, seat_number)
        booking_repository.create(booking)
        toContinue(4)

    elif new_command == 2:
        booking_ref = input('Enter the booking reference to retrieve booking details: ')
        booking_repository.find(booking_ref)
        toContinue(4)

    elif new_command == 3:
        passenger = input('Enter the passenger ID number: ')
        flight = input('Enter the flight aircraft registration number: ')
        ticketType = input('Enter the ticket type: ')
        ticketClass = input('Enter the ticket Class: ')
        seatNumber = input('Enter the passenger seat number: ')
        booking_repository.update(booking_ref, booking)
        toContinue(4)

    elif new_command == 4:
        booking_repository.show()
        toContinue(4)

    elif new_command == 5:
        booking_ref = input('Enter the booking reference to retrieve booking details: ')
        booking_repository.delete(booking_ref)
        toContinue(4)

    else:
        print('Your Input does not Exist')
        toContinue(4)

main()
# subMenu()