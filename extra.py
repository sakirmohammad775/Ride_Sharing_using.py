


class BusInfo:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked = 0


    def seats_left(self):
        available_seats=self.total_seats - self.booked
        return available_seats
    def reserve_seat(self):
        if self.seats_left() > 0:
            self.booked += 1
            return True
        return False
class AdminUser:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def verify_login(self, username, password):
        return self.username == username and self.password == password


class PassengerInfo:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus


class BusTicketSystem:
    def __init__(self):
        self.bus_list = []
        self.passenger_list = []
        self.admin = AdminUser("admin", "0000")
        self.logged_in = False


    def insert_bus(self, number, route, seats):
        bus = BusInfo(number, route, seats)
        self.bus_list.append(bus)
        print(f"Bus {number} successfully added\n")


    def search_bus(self, number):
        for bus in self.bus_list:
            if bus.number == number:
                return bus
        return None


    def reserve_ticket(self, number, name, phone):
        bus = self.search_bus(number)
        if not bus:
            print("Bus not found\n")
            return


        if bus.reserve_seat():
            passenger = PassengerInfo(name, phone, bus)
            self.passenger_list.append(passenger)
            print(f"Ticket confirmed for {name} on Bus {number}.Fare:500\n")
        else:
            print("No available seats on this bus\n")


    def display_buses(self):
        if not self.bus_list:
            print("No buses available.\n")
        else:
            print("\n Current Buses:")
            for bus in self.bus_list:
                print(f"Bus No: {bus.number}, Route: {bus.route}, Available: {bus.seats_left()} seats")
            print()


    def admin_panel(self):
        while True:
            print("\n--- Admin Dashboard --->")
            print("1. Add Bus")
            print("2. Show All Buses")
            print("3. Logout")


            choice = input("Select an option: ")


            if choice == '1':
                number = input("Bus Number: ")
                route = input("Route: ")
                try:
                    seats = int(input("Total Seats: "))
                    self.insert_bus(number, route, seats)
                except ValueError:
                    print("Please enter a valid seat number.")
            elif choice == '2':
                self.display_buses()
            elif choice == '3':
                self.logged_in = False
                print("Logged out from admin panel.\n")
                break
            else:
                print("Invalid input, try again.\n")


    def main_menu(self):
        while True:
            print("\n🚏 Welcome to Bangladesh Bus Ticket Booking System 🚏")
            print("1. Admin Login")
            print("2. Book Ticket")
            print("3. View Buses")
            print("4. Exit")


            choice = input("Enter your choice: ")


            if choice == '1':
                uname = input("Username: ")
                pword = input("Password: ")
                if self.admin.verify_login(uname, pword):
                    self.logged_in = True
                    print("Admin login successful!\n")
                    self.admin_panel()
                else:
                    print("Invalid credentials.\n")
            elif choice == '2':
                name = input("Your Name: ")
                phone = input("Phone Number: ")
                bus_no = input("Bus Number: ")
                self.reserve_ticket(bus_no, name, phone)
            elif choice == '3':
                self.display_buses()
            elif choice == '4':
                print("Exiting... Thank you for using the system.")
                break
            else:
                print("Invalid option. Please try again.\n")


system = BusTicketSystem()
system.main_menu()



