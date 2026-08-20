from flask import Flask, render_template, redirect, url_for, request
from database_functions import show_expenses, remove_expense

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/expenses")
def expenses():
    all_expenses = show_expenses()
    for row in all_expenses:
        print(row)
    return render_template('expenses.html', expenses=all_expenses)

# NEW ROUTE: Handles the delete action from the HTML form
@app.route("/delete-expense/<int:id>", methods=["POST"])
def delete_expense(id):
    remove_expense(id) # This runs your existing SQLite delete code
    return redirect(url_for('expenses')) # Reloads the page to show it is gone

@app.route("/add-expense", methods=["POST"])
def add_expense():
    expense_name = request.form.get("Expense_name")
    return redirect(url_for("expenses"))


if __name__ == "__main__":
    app.run(debug=True)
