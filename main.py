from expense import Expense
from storage import save_expenses, load_expenses
from expenseManager import ExpenseManager

expense_data = load_expenses()
manager = ExpenseManager(expense_data)

while True:

    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount! Please enter a number.")
            continue
        category=input("Enter the category : ")
        date=input("Enter date (YYYY-MM-DD):")

        expense = Expense(amount,category,date)
        manager.add_expense(expense)
        save_expenses(manager.expenses)

        print("\nExpense added successfully!\n")

    elif choice == "2":
        manager.list_expenses()

    elif choice == "3":
        total = manager.get_total_expense()
        print("total expense : ",total)

    elif choice == "4":
        summary = manager.get_category_summary()
        print("\nCategory Summary:")
        for cat, amt in summary.items():
            print(f"{cat} : {amt}")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")


  