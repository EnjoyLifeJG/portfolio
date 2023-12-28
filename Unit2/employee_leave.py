# By Jean-G. De Souza
# Essex University Online
# PG Cert in Computer Science - Module OOP: Unit 2
# Activity instructions: Write a Python program to achieve basic employee-related functionality
# which includes retaining employee details and allowing an employee to book a day of annual leave.
# Extend the Python program you have now created to use protected and unprotected variables. Remember to record your findings in your e-portfolio.

# ---------------------------------

class Employee:
    def __init__(self, employee_id, name, annual_leave):
        self.employee_id = employee_id  # Public variable
        self.name = name  # Public variable
        self._annual_leave = annual_leave  # Protected variable

    def display_details(self):
        """ Display employee's details """
        print(f"Employee ID: {self.employee_id}")
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


def main():
    # Creating an employee for demonstration
    emp = Employee("1234", "Jean De Souza", 25)

    # Displaying employee details
    emp.display_details()

    # Simulate booking annual leave
    print("\nBooking 5 days of annual leave...")
    emp.book_annual_leave(5)

    # Displaying details after booking leave
    print("\nEmployee details after booking annual leave:")
    emp.display_details()


# Running the main function
main()
