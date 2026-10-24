
# Flight Reservation System
# Using Searching and Sorting

flights = [
    {"flight_no": 101, "from": "Pune", "to": "Delhi",
     "price": 4500, "seats": 5},

    {"flight_no": 102, "from": "Mumbai", "to": "Nashik",
     "price": 2500, "seats": 3},

    {"flight_no": 103, "from": "Pune", "to": "Mumbai",
     "price": 3500, "seats": 4},

    {"flight_no": 104, "from": "Delhi", "to": "Chennai",
     "price": 5500, "seats": 2},

    {"flight_no": 105, "from": "Mumbai", "to": "Delhi",
     "price": 4000, "seats": 6}
]


# Display all flights
def display_flights():
    print("\n\t\t----- Available Flights -----")
    print("Flight No\tFrom\t\tTo\t\tPrice\t\tSeats")
    print("-" * 75)

    for flight in flights:
        print(f"{flight['flight_no']}\t\t"
              f"{flight['from']}\t\t"
              f"{flight['to']}\t\t"
              f"{flight['price']}\t\t"
              f"{flight['seats']}")

    print("-" * 75)


# Search flight using Linear Search
def search_flight(number):
    for flight in flights:
        if flight["flight_no"] == number:
            return flight

    return None


# Sort flights by price using Bubble Sort
def sort_flights():
    n = len(flights)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if flights[j]["price"] > flights[j + 1]["price"]:
                flights[j], flights[j + 1] = (
                    flights[j + 1], flights[j]
                )

    print("\nFlights sorted by price (lowest to highest):")
    display_flights()


# Reserve flight
def reserve_flight(number, name, seats):
    flight = search_flight(number)

    if flight is None:
        print("Flight not found.")
        return

    print("\nFlight Found!")
    print("From:", flight["from"])
    print("To:", flight["to"])
    print("Price per seat: Rs.", flight["price"])
    print("Available seats:", flight["seats"])

    if seats <= 0:
        print("Please enter a valid number of seats.")

    elif seats > flight["seats"]:
        print("Sorry! Only", flight["seats"],
              "seats are available.")

    else:
        total = flight["price"] * seats

        # Update available seats
        flight["seats"] -= seats

        print("\n----- Reservation Successful -----")
        print("Passenger Name :", name)
        print("Flight No      :", flight["flight_no"])
        print("From           :", flight["from"])
        print("To             :", flight["to"])
        print("Seats Booked   :", seats)
        print("Total Amount   : Rs.", total)
        print("Remaining Seats:", flight["seats"])
        print("----------------------------------")


# Menu-driven function
def menu():
    while True:
        print("\n========== FLIGHT RESERVATION SYSTEM ==========")
        print("1. Display Flights")
        print("2. Search Flight")
        print("3. Sort Flights by Price")
        print("4. Reserve Flight")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_flights()

        elif choice == "2":
            number = int(input("Enter Flight Number to search: "))

            flight = search_flight(number)

            if flight is not None:
                print("\nFlight Found!")
                print("Flight No :", flight["flight_no"])
                print("From      :", flight["from"])
                print("To        :", flight["to"])
                print("Price     : Rs.", flight["price"])
                print("Seats     :", flight["seats"])
            else:
                print("Flight not found.")

        elif choice == "3":
            sort_flights()

        elif choice == "4":
            number = int(input("Enter Flight Number: "))
            name = input("Enter passenger name: ")
            seats = int(input("Enter number of seats to book: "))

            reserve_flight(number, name, seats)

        elif choice == "5":
            print("Thank you for using Flight Reservation System!")
            break

        else:
            print("Invalid choice! Please try again.")


# Main Program
menu()
