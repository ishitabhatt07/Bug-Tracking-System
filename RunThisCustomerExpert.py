import mysql.connector
import LoginSignup
import AdminModule

# Establishing connection with the MySQL database
db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="*****",
                             database="bug_tracking")


# Customer Module
def create_account():
    custLoginId = input("Enter a customer login ID: ")
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

    print("Customer account created successfully!")


def update_account():
    custLoginId = input("Enter your customer login ID: ")
    custName = input("Enter the updated customer name: ")
    custAge = int(input("Enter the updated customer age: "))
    custPhone = input("Enter the updated customer phone number: ")
    custEmail = input("Enter the updated customer email: ")

    cursor = db.cursor()
    query = "SELECT * FROM customer WHERE custLoginId = %s"
    values = (custLoginId,)
    cursor.execute(query, values)
    customer = cursor.fetchone()

    if customer:
        update_query = "UPDATE customer SET custName = %s, custAge = %s, custPhone = %s, custEmail = %s WHERE custLoginId = %s"
        update_values = (custName, custAge, custPhone, custEmail, custLoginId)
        cursor.execute(update_query, update_values)
        db.commit()

        print("Customer account updated successfully!")
    else:
        print("Customer account not found.")


def post_new_bug():
    custLoginId = input("Enter your customer login ID: ")
    productName = input("Enter the product name: ")
    bugDesc = input("Enter the bug description: ")

    cursor = db.cursor()
    query = "INSERT INTO bug (custLoginId, productName, bugDesc) VALUES (%s, %s, %s)"
    values = (custLoginId, productName, bugDesc)
    cursor.execute(query, values)
    db.commit()

    print("New bug posted successfully!")


def view_all_bugs():
    cursor = db.cursor()
    query = "SELECT * FROM bug"
    cursor.execute(query)
    bugs = cursor.fetchall()

    if bugs:
        print("All Bugs:")
        for bug in bugs:
            print(f"Bug ID: {bug[0]}, Posting Date: {bug[1]}, Customer Login ID: {bug[2]}, Bug Status: {bug[3]}, Product Name: {bug[4]}, Bug Description: {bug[5]}, Expert Assigned Date: {bug[6]}, Expert Login ID: {bug[7]}, Bug Solved Date: {bug[8]}, Solution: {bug[9]}")
    else:
        print("No bugs found.")


def search_bugs_by_status():
    bug_status = input("Enter the bug status to search: ")

    cursor = db.cursor()
    query = "SELECT * FROM bug WHERE bugStatus = %s"
    values = (bug_status,)
    cursor.execute(query, values)
    bugs = cursor.fetchall()

    if bugs:
        print(f"Bugs with status '{bug_status}':")
        for bug in bugs:
            print(f"Bug ID: {bug[0]}, Posting Date: {bug[1]}, Customer Login ID: {bug[2]}, Bug Status: {bug[3]}, Product Name: {bug[4]}, Bug Description: {bug[5]}, Expert Assigned Date: {bug[6]}, Expert Login ID: {bug[7]}, Bug Solved Date: {bug[8]}, Solution: {bug[9]}")
    else:
        print(f"No bugs found with status '{bug_status}'.")


def view_bug_solution():
    bug_id = int(input("Enter the bug ID to view the solution: "))

    cursor = db.cursor()
    query = "SELECT * FROM bug WHERE bugId = %s"
    values = (bug_id,)
    cursor.execute(query, values)
    bug = cursor.fetchone()

    if bug:
        if bug[9]:
            print(f"Bug ID: {bug[0]}, Solution: {bug[9]}")
        else:
            print("Bug solution not available.")
    else:
        print(f"No bug found with ID '{bug_id}'.")


def change_customer_password():
    custLoginId = input("Enter your customer login ID: ")
    new_password = input("Enter the new password: ")

    cursor = db.cursor()
    query = "SELECT * FROM customer WHERE custLoginId = %s"
    values = (custLoginId,)
    cursor.execute(query, values)
    customer = cursor.fetchone()

    if customer:
        update_query = "UPDATE customer SET custPassword = %s WHERE custLoginId = %s"
        update_values = (new_password, custLoginId)
        cursor.execute(update_query, update_values)
        db.commit()

        print("Password changed successfully!")
    else:
        print("Customer account not found.")


# Expert Module
def view_assigned_bugs():
    expert_login_id = input("Enter your expert login ID: ")

    cursor = db.cursor()
    query = "SELECT * FROM bug WHERE expertLoginId = %s"
    values = (expert_login_id,)
    cursor.execute(query, values)
    bugs = cursor.fetchall()

    if bugs:
        print(f"Bugs assigned to expert with login ID '{expert_login_id}':")
        for bug in bugs:
            print(f"Bug ID: {bug[0]}, Posting Date: {bug[1]}, Customer Login ID: {bug[2]}, Bug Status: {bug[3]}, Product Name: {bug[4]}, Bug Description: {bug[5]}, Expert Assigned Date: {bug[6]}, Bug Solved Date: {bug[8]}, Solution: {bug[9]}")
    else:
        print(f"No bugs assigned to expert with login ID '{expert_login_id}'.")


def filter_assigned_bugs_by_status():
    expert_login_id = input("Enter your expert login ID: ")
    bug_status = input("Enter the bug status to filter: ")

    cursor = db.cursor()
    query = "SELECT * FROM bug WHERE expertLoginId = %s AND bugStatus = %s"
    values = (expert_login_id, bug_status)
    cursor.execute(query, values)
    bugs = cursor.fetchall()

    if bugs:
        print(f"Bugs assigned to expert with login ID '{expert_login_id}' and status '{bug_status}':")
        for bug in bugs:
            print(f"Bug ID: {bug[0]}, Posting Date: {bug[1]}, Customer Login ID: {bug[2]}, Bug Status: {bug[3]}, Product Name: {bug[4]}, Bug Description: {bug[5]}, Expert Assigned Date: {bug[6]}, Bug Solved Date: {bug[8]}, Solution: {bug[9]}")
    else:
        print(f"No bugs found with assigned expert login ID '{expert_login_id}' and status '{bug_status}'.")


def solve_bug():
    bug_id = int(input("Enter the bug ID to solve: "))
    solution = input("Enter the solution: ")

    cursor = db.cursor()
    query = "SELECT * FROM bug WHERE bugId = %s"
    values = (bug_id,)
    cursor.execute(query, values)
    bug = cursor.fetchone()

    if bug:
        update_query = "UPDATE bug SET bugStatus = 'Bug Solved', bugSolvedDate = now(), solution = %s WHERE bugId = %s"
        update_values = (solution, bug_id)
        cursor.execute(update_query, update_values)
        db.commit()

        print(f"Bug with ID '{bug_id}' has been solved.")
    else:
        print(f"No bug found with ID '{bug_id}'.")


def change_expert_password():
    expert_login_id = input("Enter your expert login ID: ")
    new_password = input("Enter the new password: ")

    cursor = db.cursor()
    query = "SELECT * FROM employee WHERE empLoginId = %s AND empType = 'EXPERT'"
    values = (expert_login_id,)
    cursor.execute(query, values)
    expert = cursor.fetchone()

    if expert:
        update_query = "UPDATE employee SET empPassword = %s WHERE empLoginId = %s"
        update_values = (new_password, expert_login_id)
        cursor.execute(update_query, update_values)
        db.commit()

        print("Password changed successfully!")
    else:
        print("Expert account not found.")


# Customer module menu
def customer_module_menu():
    print("Customer Module")
    print("1. Create Account")
    print("2. Update Account")
    print("3. Post New Bug")
    print("4. View All Bugs")
    print("5. Search Bugs based on status")
    print("6. View Bug Solution")
    print("7. Change Password")
    print("8. Logout")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        create_account()
    elif choice == "2":
        update_account()
    elif choice == "3":
        post_new_bug()
    elif choice == "4":
        view_all_bugs()
    elif choice == "5":
        search_bugs_by_status()
    elif choice == "6":
        view_bug_solution()
    elif choice == "7":
        change_customer_password()
    elif choice == "8":
        print("Logging out...")
        return
    else:
        print("Invalid choice.")

    customer_module_menu()


# Expert module menu
def expert_module_menu():
    print("Expert Module")
    print("1. View Assigned Bugs")
    print("2. Filter Assigned Bugs based on status")
    print("3. Solve the Bug")
    print("4. Change Password")
    print("5. Logout")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        view_assigned_bugs()
    elif choice == "2":
        filter_assigned_bugs_by_status()
    elif choice == "3":
        solve_bug()
    elif choice == "4":
        change_expert_password()
    elif choice == "5":
        print("Logging out...")
        return
    else:
        print("Invalid choice.")

    expert_module_menu()


# Main menu
def main_menu():
    print("Welcome to the Bug Tracking System!")
    print("1. Customer Login")
    print("2. Expert Login")
    print("3. Admin Login")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        LoginSignup.customer_login(db)
        customer_module_menu()
    elif choice == "2":
        LoginSignup.employee_login()
        expert_module_menu()
    elif choice == "3": 
        LoginSignup.employee_login()
        AdminModule.admin_module_menu()
    elif choice == "4":
        print("Exiting...")
        return
    else:
        print("Invalid choice.")




# Calling the main menu
main_menu()

# Closing the database connection
db.close()
