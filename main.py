from expense import Expense
from storage import save_expenses, load_expenses
from expenseManager import ExpenseManager


manager = ExpenseManager([])
while True:

    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category=input("Enter the category : ")
        date=input("Enter date (YYYY-MM-DD):")

        expense = Expense(amount,category,date)
        manager.add_expense(expense)
        print("Expense added successfully!")

    elif choice == "2":
        print("View Expenses selected")

    elif choice == "3":
        print("Total Expense selected")

    elif choice == "4":
        print("Category Summary selected")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")


  