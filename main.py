from expense import Expense
from storage import save_expenses, load_expenses

def main():
    # Step 1: Create some sample expenses
    expense1 = Expense(500, "Food", "2026-04-01")
    expense2 = Expense(1200, "Travel", "2026-04-02")

    expenses = [expense1, expense2]

    # Step 2: Save expenses to file
    save_expenses(expenses)
    print("Expenses saved successfully!\n")

    # Step 3: Load expenses from file
    loaded_expenses = load_expenses()

    # Step 4: Display loaded expenses
    print("Loaded Expenses:")
    for e in loaded_expenses:
        print(e)


if __name__ == "__main__":
    main()