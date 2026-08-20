from flask import Flask, render_template, redirect, url_for, request
from database_functions import show_expenses, remove_expense, insert_expense

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/expenses")
def expenses():
    all_expenses = show_expenses()
    return render_template('expenses.html', expenses=all_expenses)

# Handles delete requests from the hmtl form which provides the ID
@app.route("/delete-expense/<int:id>", methods=["POST"])
def delete_expense(id):
    remove_expense(id) # runs your existing SQLite delete code
    return redirect(url_for('expenses')) # Reloads the page to show it is gone

@app.route("/add-expense", methods=["POST"])
def add_expense():
    expense_name = request.form.get("expense_name")
    expense_amount = request.form.get("expense_amount")
    expense_type = request.form.get("expense_type")
    expense_date = request.form.get("expense_date")
    insert_expense(str(expense_name), float(expense_amount), str(expense_type), str(expense_date))
    return redirect(url_for("expenses"))

@app.route("/update_expense/<int:id>", methods=["PUT"])
def update_expense(id):
    print(id)
    return redirect(url_for("expenses"))

if __name__ == "__main__":
    app.run(debug=True)
