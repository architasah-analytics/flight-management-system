import mysql.connector
from datetime import date

# Establish the connection to MySQL Database
db = mysql.connector.connect(host="localhost", user="root", passwd="Your_Password", database="flight_management")
if db.is_connected():
    print('Successfully Connected')

cursor = db.cursor()

    
# Function to add a new flight
def add_flight(source, destination, dep_date, dep_time, price, status):
    query = "INSERT INTO flights(source, destination, departure_date, departure_time, price, status) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (source, destination, dep_date, dep_time, price, status)
    cursor.execute(query, values)
    db.commit()
    print("Flight added successfully.")

# Function to view all flights
def view_flights():
    query = "SELECT * FROM flights"
    cursor.execute(query)
    flights = cursor.fetchall()
    for flight in flights:
        print(flight)

# Function to book a flight
def book_flight(passenger_id, flight_id):
    booking_date = date.today()
    query = "INSERT INTO bookings (passenger_id, flight_id, booking_date) VALUES (%s, %s, %s)"
    values = (passenger_id, flight_id, booking_date)
    cursor.execute(query, values)
    db.commit()
    print("Flight booked successfully.")

# Function to add a new passenger
def add_passenger(name, age, gender, contact):
    query = "INSERT INTO passenger (name, age, gender, contact) VALUES (%s, %s, %s, %s)"
    values = (name, age, gender, contact)
    cursor.execute(query, values)
    db.commit()
    print("Passenger added successfully.")

# Function to view all passengers
def view_passengers():
    query = "SELECT * FROM passenger"
    cursor.execute(query)
    passengers = cursor.fetchall()
    for passenger in passengers:
        print(passenger)

# Function to search for flights by source and destination
def search_flights(source, destination):
    query = "SELECT * FROM flights WHERE source = %s AND destination = %s"
    values = (source, destination)
    cursor.execute(query, values)
    flights = cursor.fetchall()
    for flight in flights:
        print(flight)

# Function to delete a flight and its associated bookings
def delete_flight_with_bookings(flight_id):
    try:
        # First, delete any related bookings
        cursor.execute("DELETE FROM bookings WHERE flight_id = %s", (flight_id,))
        db.commit()

        # Then, delete the flight itself
        cursor.execute("DELETE FROM flights WHERE flight_id = %s", (flight_id,))
        db.commit()

        print(f"Flight with ID {flight_id} and its related bookings have been deleted successfully.")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

# Function to delete a passenger and their associated bookings
def delete_passenger_with_bookings(passenger_id):
    try:
        # First, delete any related bookings
        cursor.execute("DELETE FROM bookings WHERE passenger_id = %s", (passenger_id,))
        db.commit()

        # Then, delete the passenger itself
        cursor.execute("DELETE FROM passenger WHERE passenger_id = %s", (passenger_id,))
        db.commit()

        print(f"Passenger with ID {passenger_id} and their related bookings have been deleted successfully.")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except Exception as ex:
        print(f"An error occurred: {ex}")
        

# Admin menu to add, update, and view flights
def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Flight")
        print("2. View All Flights")
        print("3. Delete Flight")
        print("4. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            source = input("Enter source: ")
            destination = input("Enter destination: ")
            dep_date = input("Enter departure date (YYYY-MM-DD): ")
            dep_time = input("Enter departure time (HH:MM:SS): ")
            price = float(input("Enter price: "))
            status = input("Enter status (Available/Cancelled): ")
            add_flight(source, destination, dep_date, dep_time, price, status)
        elif choice == 2:
            view_flights()
        elif choice == 3:
            flight_id = int(input("Enter Flight ID to delete: "))
            delete_flight_with_bookings(flight_id)
        elif choice == 4:
            break

# Passenger menu to add and view passengers
def passenger_menu():
    while True:
        print("\n--- Passenger Menu ---")
        print("1. Add Passenger")
        print("2. View All Passengers")
        print("3. Delete Passenger")
        print("4. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            contact = input("Enter contact: ")
            add_passenger(name, age, gender, contact)
        elif choice == 2:
            view_passengers()
        elif choice == 3:
            passenger_id = int(input("Enter Passenger ID to delete: "))
            delete_passenger_with_bookings(passenger_id)
        elif choice == 4:
            break

# Booking menu to book and view flights
def booking_menu():
    while True:
        print("\n--- Booking Menu ---")
        print("1. Book Flight")
        print("2. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            passenger_id = int(input("Enter Passenger ID: "))
            flight_id = int(input("Enter Flight ID: "))
            book_flight(passenger_id, flight_id)
        elif choice == 2:
            break

# Main menu for user interaction
def main_menu():
    while True:
        print("\n--- Flight Management System ---")
        print("1. Admin")
        print("2. Passenger")
        print("3. Booking")
        print("4. Search Flights")
        print("5. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            admin_menu()
        elif choice == 2:
            passenger_menu()
        elif choice == 3:
            booking_menu()
        elif choice == 4:
            source = input("Enter source: ")
            destination = input("Enter destination: ")
            search_flights(source, destination)
        elif choice == 5:
            break

# Start the application
if __name__== "__main__":
    main_menu()
