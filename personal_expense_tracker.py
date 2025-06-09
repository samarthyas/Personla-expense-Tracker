import csv
import os

expenses = []
budget = 0.0

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (e.g., Food, Travel): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    description = input("Enter description: ")

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    expenses.append(expense)
    print("Expense added successfully.\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return

    for idx, expense in enumerate(expenses, 1):
        if all(key in expense for key in ['date', 'category', 'amount', 'description']):
            print(f"{idx}. Date: {expense['date']}, Category: {expense['category']}, "
                  f"Amount: {expense['amount']}, Description: {expense['description']}")
        else:
            print(f"{idx}. Incomplete data, skipping this entry.")
    print()

def set_budget():
    global budget
    try:
        budget = float(input("Enter your monthly budget: "))
        print(f"Monthly budget set to {budget}\n")
    except ValueError:
        print("Invalid input. Budget must be a number.\n")

def track_budget():
    total_spent = sum(expense['amount'] for expense in expenses)
    print(f"Total expenses so far: {total_spent}")
    if budget == 0:
        print("No budget set.\n")
    elif total_spent > budget:
        print("⚠️ You have exceeded your budget!\n")
    else:
        print(f"You have {budget - total_spent:.2f} left for the month.\n")

def save_expenses(filename="expenses.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        writer.writerows(expenses)
    print("Expenses saved successfully.\n")

def load_expenses(filename="expenses.csv"):
    if not os.path.exists(filename):
        return
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                row['amount'] = float(row['amount'])
                expenses.append(row)
            except ValueError:
                continue
    print("Expenses loaded from file.\n")

def menu():
    while True:
        print("========== Personal Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            if budget == 0:
                set_budget()
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.\n")

if __name__ == "__main__":
    load_expenses()
    menu()
