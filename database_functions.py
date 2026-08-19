import sqlite3
import datetime

# Kept globally as it is a safe string variable
uk_date = datetime.datetime.now().strftime("%d-%m-%Y")

def get_db_connection():
    """Helper function to create a new database connection for each request."""
    conn = sqlite3.connect("expenses.db")
    #returns data dictionary like instead of people
    conn.row_factory = sqlite3.Row 
    return conn

def add_expense(expense_name, expense_amount, expense_payment_type, expense_date=uk_date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO expense (expense_name, expense_amount, expense_payment_type, expense_date)
            VALUES (?, ?, ?, ?) """,
        (expense_name, expense_amount, expense_payment_type, expense_date),
    )
    conn.commit()
    conn.close()

def remove_expense(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expense WHERE expense_id =:expense_id", {'expense_id' : id})
    conn.commit()
    conn.close()

def update_expense_name(id, new_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE expense SET expense_name = :new_name WHERE expense_id =:expense_id",{"new_name" : new_name, 'expense_id' : id})
    conn.commit()
    conn.close()

def update_expense_price(id, new_price):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE expense SET expense_amount =:new_price WHERE expense_id =:expense_id",{"new_price" : new_price, 'expense_id' : id})
    conn.commit()
    conn.close()

def update_expense_type(id, new_type):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE expense SET expense_payment_type =:new_type WHERE expense_id =:expense_id",{"new_type" : new_type, 'expense_id' : id})
    conn.commit()
    conn.close()

def show_expenses():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expense")
    # FIXED: Added parentheses to execute fetchall()
    data = cursor.fetchall() 
    conn.close()
    return data
