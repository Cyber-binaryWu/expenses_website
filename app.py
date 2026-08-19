from flask import Flask, render_template
from database_functions import show_expenses

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

if __name__ == "__main__":
    app.run(debug=True)
