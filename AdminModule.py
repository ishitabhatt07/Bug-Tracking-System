import mysql.connector

# Establishing connection with the MySQL database
db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="****",
                             database="bug_tracking")

# Customer Services
def view_all_customers():
    cursor = db.cursor()
    query = "SELECT * FROM customer"
    cursor.execute(query)
    customers = cursor.fetchall()

    if customers:
        print("All Customers:")
        for customer in customers:
            print(f"Customer Login ID: {customer[0]}, Customer Name: {customer[2]}, Customer Age: {customer[3]}, Customer Phone: {customer[4]}, Customer Email: {customer[5]}")
    else:
        print("No customers found.")


def search_customer_by_name():
    customer_name = input("Enter the customer name to search: ")

    cursor = db.cursor()
    query = "SELECT * FROM customer WHERE custName = %s"
    values = (customer_name,)
    cursor.execute(query, values)
    customers = cursor.fetchall()

    if customers:
        print(f"Customers with name '{customer_name}':")
        for customer in customers:
            print(f"Customer Login ID: {customer[0]}, Customer Name: {customer[2]}, Customer Age: {customer[3]}, Customer Phone: {customer[4]}, Customer Email: {customer[5]}")
    else:
        print(f"No customers found with name '{customer_name}'.")


def search_customer_by_loginId():

    cust_loginId = input("Enter customer login ID: ")
    cursor = db.cursor()
    query = "SELECT * FROM customer WHERE custLoginId = %s "
    values = (cust_loginId,)
    cursor.execute(query, values)
    customer = cursor.fetchone()

    if customer:
        print(f"Customers with loginID '{cust_loginId}': ")

        print(f"Customer Login ID: {customer[0]}, Customer Name: {customer[2]}, Customer Age: {customer[3]}, Customer Phone: {customer[4]}, Customer Email: {customer[5]}")
    else:
        print(f"No customer found with loginID '{cust_loginId}'. ")


def employee_add_new():
    empLoginId = input("Enter a new Employee login ID: ")
    empPassword = input("Enter a unique Employee password: ")
    empType = input("Enter the Employee type: ")
    empName = input("Enter the Employee name: ")
    empPhone = input("Enter Employee phone number: ")
    empEmail= input("Enter Employee email : ")
    empStatus= input("Enter status : ")

    cursor = db.cursor()
    query = "INSERT INTO employee(empLoginId, empPassword, empType, empName, empPhone, empEmail, empStatus) VALUES(%s, %s, %s, %s, %s, %s,%s)"
    values = (empLoginId, empPassword, empType, empName, empPhone, empEmail, empStatus)
    cursor.execute(query, values)
    db.commit()

    print("New employee is successfully added!")

def view_all_employees():
    cursor = db.cursor()
    query = "SELECT * FROM employee"
    cursor.execute(query)
    employees = cursor.fetchall()

    if employees:
        print("All Customers:")
        for employee in employees:
            print(f"Employee Login ID: {employee[0]}, Employee password: {employee[1]}, Employee Type: {employee[2]}, Employee Name: {employee[3]}, Employee Phone: {employee[4]}, Employee mail: {employee[5]}, Employee Status: {employee[6]}")
    else:
        print("No employees found.")


def search_employee_by_name():
    employee_name = input("Enter the employee name to search: ")

    cursor = db.cursor()
    query = "SELECT * FROM employee WHERE empName = %s"
    values = (employee_name,)
    cursor.execute(query, values)
    employees = cursor.fetchall()

    if employees:
        print(f"Employees with name '{employee_name}':")
        for employee in employees:
            print(f"Employee Login ID: {employee[0]}, Employee Type: {employee[2]}, Employee Name: {employee[3]}, Employee Phone: {employee[4]}, Employee Email: {employee[5]}, Employee Status: {employee[6]}")
    else:
        print(f"No customers found with name '{employee_name}'.")



def search_employee_by_loginId():

    emp_loginId = input("Enter employee login ID: ")
    cursor = db.cursor()
    query = "SELECT * FROM employee WHERE empLoginId = %s "
    values = (emp_loginId,)
    cursor.execute(query, values)
    employee = cursor.fetchone()

    if employee:
        print(f"Employee with loginID '{emp_loginId}': ")

        print(f"Employee Login ID: {employee[0]}, Employee Type: {employee[2]}, Employee Name: {employee[3]}, Employee Phone: {employee[4]}, Employee Email: {employee[5]}, Employee Status: {employee[6]}")
    else:
        print(f"No customer found with loginID '{emp_loginId}'. ")


def search_employee_by_type():
    employee_type = input("Enter the employee type to search (ADMIN/EXPERT): ")

    cursor = db.cursor()
    query = "SELECT * FROM employee WHERE empType = %s"
    values = (employee_type,)
    cursor.execute(query, values)
    employees = cursor.fetchall()

    if employees:
        print(f"Employees with type '{employee_type}':")
        for employee in employees:
            print(
                f"Employee Login ID: {employee[0]}, Employee Type: {employee[2]}, Employee Name: {employee[3]}, Employee Phone: {employee[4]}, Employee Email: {employee[5]}, Employee Status: {employee[6]}")
    else:
        print(f"No customers found with name '{employee_type}'.")


def activate_deactivate_employee():
    emp_loginID = input("Enter the employee login ID: ")
    cursor = db.cursor()
    query = "SELECT * FROM employee WHERE empLoginID= %s"
    values = (emp_loginID,)
    cursor.execute(query, values)
    employee = cursor.fetchone()

    if employee:
        if employee[6] == "INACTIVE":
            new_status = "ACTIVE"
        else:
            new_status = "INACTIVE"
        update_query = "UPDATE employee SET empStatus = %s WHERE empLoginID= %s"
        update_values = (new_status, emp_loginID)
        cursor.execute(update_query, update_values)
        db.commit()
        print("Status updated successfully!")

    else:
        print("LoginID not found.")


def change_employee_password():
    emp_loginID = input("Enter the employee login ID to change the password: ")
    new_pw = input("Enter the new password: ")
    cursor = db.cursor()
    query = "SELECT * FROM employee WHERE empLoginID= %s"
    values = (emp_loginID,)
    cursor.execute(query, values)
    employee = cursor.fetchone()

    if employee:
        update_query = "UPDATE employee SET empPassword = %s WHERE empLoginID= %s"
        update_values = (new_pw, emp_loginID)
        cursor.execute(update_query, update_values)
        db.commit()
        print("Password updated successfully!")

    else:
        print("LoginID not found.")



# Bug Services
def view_all_bugs():
    cursor = db.cursor()
    query = "SELECT * FROM bug"
    cursor.execute(query)
    bugs = cursor.fetchall()

    if bugs:
        print("All Bugs:")
        for bug in bugs:
            print(f" custLoginId: '{bug[2]}'\n bugStatus '{bug[3]}' productName: '{bug[4]}' bugDesc: '{bug[5]}'")
            print("\n")
    else:
        print("No bugs found.")


def search_bug_by_bugId():

    bug_Id = input("Enter Bug ID: ")

    cursor = db.cursor()
    query = "SELECT * FROM bug WHERE bugId = %s "
    values = (bug_Id,)
    cursor.execute(query, values)
    bug = cursor.fetchone()

    if bug:
        print(f"Bug with bugID '{bug_Id}': ")
        print(f"\n custLoginId: '{bug[2]}'\n bugStatus '{bug[3]}' productName: '{bug[4]}' bugDesc: '{bug[5]}")
    else:
        print(f"No bug found with bugID '{bug_Id}'. ")


def search_bug_by_status():
    bug_status = input("Enter the bug status to search (New Bug/Assigned/Solved): ")

    cursor = db.cursor()
    query = "SELECT * FROM Bug WHERE bugStatus = %s"
    values = (bug_status,)
    cursor.execute(query, values)
    bugs = cursor.fetchall()

    if bugs:
        print(f"Bugs with type '{bug_status}':")
        for bug in bugs:
            print(f"\n custLoginId: '{bug[2]}'\n bugStatus '{bug[3]}' productName: '{bug[4]}' bugDesc: '{bug[5]}")
    else:
        print(f"No bugs found with status '{bug_status}'.")



def search_bug_by_custLoginId():

    cust_loginId = input("Enter customer login ID to search the bug: ")

    cursor = db.cursor()
    query = "SELECT * FROM bug WHERE custLoginId = %s "
    values = (cust_loginId,)
    cursor.execute(query, values)
    bugs = cursor.fetchall()

    if bugs:
        print(f"Bugs with Customer Login ID '{cust_loginId}': ")
        for bug in bugs:
            print(f"\n custLoginId: '{bug[2]}'\n bugStatus: '{bug[3]}'\n productName: '{bug[4]}'\n bugDesc: '{bug[5]}'")
            print("\n")
    else:
        print(f"No bugs found with custLoginID '{cust_loginId}'. ")



def assign_bug_to_expert():
    bug_id = input("Enter the bug ID to assign: ")
    expert_login_id = input("Enter the expert login ID to assign: ")

    cursor = db.cursor()
    query = "SELECT * FROM bug WHERE bugId = %s"
    values = (bug_id,)
    cursor.execute(query, values)
    bug = cursor.fetchone()

    if bug:
        update_query = "UPDATE bug SET expertAssignedDate = now(), expertLoginId = %s WHERE bugId = %s"
        update_values = (expert_login_id, bug_id)
        cursor.execute(update_query, update_values)
        db.commit()
        print(f"Bug with ID '{bug_id}' has been assigned to expert with login ID '{expert_login_id}'.")
    else:
        print(f"No bug found with ID '{bug_id}'.")

# Admin module menu
def admin_module_menu():
    print("-----ADMIN MODULE-----")
    print("1. Customer Services - Manage Services (View, Search)")
    print("2. Employee Services - Manage Employee (Admin & Expert types)(Add, View, Search, Edit, Activate/Deactivate)")
    print("3. Bug Services - Manage Bug(View, Search, AssignBugToExpert)")

    choice = input("\nEnter your choice:")

    if choice == "1":
        print("\n1. Customer: View All")
        print("2. Customer: Search - by Customer Name")
        print("3. Customer: Search - by Customer Login ID")

        choice1 = input("\nEnter your choice(1-3):")

        if choice1 == "1":
            view_all_customers()
        elif choice1 == "2":
            search_customer_by_name()
        elif choice1 == "3":
            search_customer_by_loginId()
        else:
            print("Invalid Choice!!!")

    elif choice == "2":
        print("\n4. Employee: Add New (Admin or Expert)")
        print("5. Employee: View All")
        print("6. Employee: Search - by Employee Name")
        print("7. Employee: Search - by Employee Login ID")
        print("8. Employee: Search - by Employee Type")
        print("9. Employee: Activate or Deactivate")
        print("10. Employee: Change Password")

        choice2 = input("\nEnter your choice(4-10):")

        if choice2 == "4":
            employee_add_new()
        elif choice2 == "5":
            view_all_employees()
        elif choice2 == "6":
            search_employee_by_name()
        elif choice2 == "7":
            search_employee_by_loginId()
        elif choice2 == "8":
            search_employee_by_type()
        elif choice2 == "9":
            activate_deactivate_employee()
        elif choice2 == "10":
            change_employee_password()
        else:
            print("Invalid Choice!")

    elif choice == "3":
        print("\n11. Bug: View All")
        print("12. Bug: Search by bugId")
        print("13. Bug: Search by status")
        print("14. Bug: Search by custLoginId")
        print("15. Bug: Assign to Expert")
        print("16. Logout")

        choice3 = input("\nEnter your choice (11-16):")

        if choice3 == "11":
            view_all_bugs()
        elif choice3 == "12":
            search_bug_by_bugId()
        elif choice3 == "13":
            search_bug_by_status()
        elif choice3 == "14":
            search_bug_by_custLoginId()
        elif choice3 == "15":
            assign_bug_to_expert()
        elif choice3 == "16":
            print("Logging out...")
            return
        else:
            print("Invalid choice.")




# Closing the database connection
db.close()









