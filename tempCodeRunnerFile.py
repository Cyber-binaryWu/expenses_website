from database_functions import show_expenses
all_expenses = show_expenses()
for row in all_expenses:
    print(row['expense_name'])
    