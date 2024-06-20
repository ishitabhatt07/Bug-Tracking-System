
import mysql.connector

# Establishing connection with the MySQL database
db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="****",
                             database="bug_tracking")

# Employee Login
def employee_login(db):
    cursor = db.cursor()
    empLoginId = input("Enter your employee login ID: ")
    empPassword = input("Enter your password: ")

    cursor = db.cursor()
    query = "SELECT * FROM employee WHERE empLoginId = %s AND empPassword = %s"
    values = (empLoginId, empPassword)
    cursor.execute(query, values)
    employee = cursor.fetchone()

    if employee:
        print("Login successful!")
        # Proceed with employee functionality
    else:
        print("Invalid employee login ID or password.")

# Customer Login
def customer_login(db):
    cursor = db.cursor()
    custLoginId = input("Enter your customer login ID: ")
    custPassword = input("Enter your password: ")

    cursor = db.cursor()
    query = "SELECT * FROM customer WHERE custLoginId = %s AND custPassword = %s"
    values = (custLoginId, custPassword)
    cursor.execute(query, values)
    customer = cursor.fetchone()

    if customer:
        print("Login successful!")
        # Proceed with customer functionality
    else:
        print("Invalid customer login ID or password.")
'''
# Employee Signup
def employee_signup():
    empLoginId = input("Enter a unique employee login ID: ")
    empPassword = input("Enter a password: ")
    empType = input("Enter the employee type (ADMIN/EXPERT): ")
    empName = input("Enter the employee name: ")
    empPhone = input("Enter the employee phone number: ")
    empEmail = input("Enter the employee email: ")

    cursor = db.cursor()
    query = "INSERT INTO employee (empLoginId, empPassword, empType, empName, empPhone, empEmail) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (empLoginId, empPassword, empType, empName, empPhone, empEmail)
    cursor.execute(query, values)
    db.commit()

    print("Employee signup successful!")
'''
# Customer Signup
def customer_signup():
    custLoginId = input("Enter a unique customer login ID: ")
    custPassword = input("Enter a password: ")
    custName = input("Enter the customer name: ")
    custAge = int(input("Enter the customer age: "))
    custPhone = input("Enter the customer phone number: ")
    custEmail = input("Enter the customer email: ")

    cursor = db.cursor()
    query = "INSERT INTO customer (custLoginId, custPassword, custName, custAge, custPhone, custEmail) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (custLoginId, custPassword, custName, custAge, custPhone, custEmail)
    cursor.execute(query, values)
    db.commit()

    print("Customer signup successful!")

# Main menu
def main_menu():
    print("Welcome to the Bug Tracking System!")
    print("1. Employee Login")
    print("2. Customer Login")

    print("3. Customer Signup")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        employee_login(db)
    elif choice == "2":
        customer_login(db)

    elif choice == "3":
        customer_signup()
    else:
        print("Invalid choice.")

# Calling the main menu

main_menu()
# Closing the database connection
db.close()
