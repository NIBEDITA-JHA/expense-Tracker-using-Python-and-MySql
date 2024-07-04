import mysql.connector
from datetime import date

# Connect to MySQL (XAMPP)
mydb = mysql.connector.connect(
    host="localhost",  # Or your XAMPP MySQL server host
    user="root",       # Default user for XAMPP MySQL
    password="",       # Default password is blank for XAMPP MySQL
    database="expense_tracker"
)

# Rest of your script...
# Function to add an expense
def add_expense(description, amount):
    cursor = mydb.cursor()
    today = date.today()
    formatted_date = today.strftime('%Y-%m-%d')
    sql = "INSERT INTO expenses (description, amount, date) VALUES (%s, %s, %s)"
    values = (description, amount, formatted_date)
    cursor.execute(sql, values)
    mydb.commit()
    print("Expense added successfully.")

# Function to view all expenses
def view_expenses():
    cursor = mydb.cursor()
    sql = "SELECT * FROM expenses"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

# Main program loop
if __name__ == "__main__":
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter amount: "))
            add_expense(description, amount)
        elif choice == '2':
            print("\nAll Expenses:")
            view_expenses()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")