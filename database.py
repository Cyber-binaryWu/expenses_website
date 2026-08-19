import sqlite3

connection = sqlite3.connect("expenses.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS expense(
                expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
                expense_name TEXT,
                expense_amount NUMERIC,
                expense_payment_type TEXT,
                expense_date TEXT)""")
connection.close()