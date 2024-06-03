'''
By Jean-G. De Souza
Essex University Online
PG Cert in Computer Science - Module OOP: Unit 2

    Activity instructions:
  " Write a Python program to achieve basic employee-related functionality which includes
    retaining employee details and allowing an employee to book a day of annual leave.
    Extend the Python program you have now created to use protected and unprotected variables.
    Remember to record your findings in your e-portfolio. "
'''

# ---------------------------------

class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id  # Public variable
        self.name = name  # Public variable
        self._annual_leave = 25  # Protected variable (25 days for all employees by default)

    def display_details(self):
        """ Display employee's details """
        print(f"\nEmployee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Annual Leave Remaining: {self._annual_leave}")

    def book_annual_leave(self, days):
        """ Book annual leave for the employee """
        if days <= self._annual_leave:
            self._annual_leave -= days
            print(f"{days} days of annual leave booked.")
            print(f"Annual Leave Remaining: {self._annual_leave}")
        else:
            print("Insufficient annual leave balance.")


def main_menu():
    employees = {}

    while True:
        print("\nWelcome to the Employee Management System")
        print("\nPlease select an option:")
        print("1. Add New Employee")
        print("2. View Employee Details")
        print("3. Book Annual Leave")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            employee_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            employees[employee_id] = Employee(employee_id, name)
            print("Employee added successfully.")
            input("Press Enter to return to the main menu...")


        elif choice == '2':
            employee_id = input("Enter Employee ID: ")
            if employee_id in employees:
                employees[employee_id].display_details()
                input("Press Enter to return to the main menu...")
            else:
                print("Employee not found.")
                input("Press Enter to return to the main menu...")


        elif choice == '3':
            employee_id = input("Enter Employee ID: ")
            if employee_id in employees:
                days = int(input("Enter number of days to book: "))
                employees[employee_id].book_annual_leave(days)
                input("Press Enter to return to the main menu...")
            else:
                print("Employee not found.")
                input("Press Enter to return to the main menu...")

        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to return to the main menu...")


# Running the main menu
main_menu()
