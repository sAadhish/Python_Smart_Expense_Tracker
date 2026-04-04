import json
from expense import Expense

def save_expenses(expenses):

    try:

        expense_list=[]

        for expense in expenses :
            expense_list.append(expense.to_dict())

        with open('expense_list.json','w') as file :
            json.dump(expense_list,file,indent=4)
    

    except Exception as e:
                print("Error saving data:", e)


  
def load_expenses():
    try:
        with open('expense_list.json', 'r') as file:
            expense_list = json.load(file)

        expenses = []

        for item in expense_list:
            # converting json dict to object
            expense = Expense(
                item["amount"],
                item["category"],
                item["date"]
            )
            expenses.append(expense)

        return expenses

    except FileNotFoundError:
        return []
    except Exception as e:
        print("Error loading:", e)
        return []
