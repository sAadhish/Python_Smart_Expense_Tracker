from expense import Expense
from storage import save_expenses ,load_expenses


class ExpenseManager :

    def __init__(self,expense):
        self.expenses = load_expenses()
        


    def add_expense(self, expense):
        # expense = Expense(amount, category, date)
        self.expenses.append(expense)
        save_expenses(self.expenses)

        

    def get_total_expense(self):

        total_expense = 0 

        for expense in self.expenses:
            total_expense = expense.amount + total_expense
            
        return total_expense
    
# group expense by category
    def get_category_summary(self):

        summary ={}

        for expense in self.expenses:
            category = expense.category
            
            if category in summary :
                summary[category] +=expense.amount

            else:
                summary[category]= expense.amount

        return summary



# list all the inputa            
    def list_expenses(self):

        if not self.expenses:
                 print("No expenses found")
                 return
        
        for expense in self.expenses:
            print(f"{expense.category} - {expense.amount} - {expense.date}")
