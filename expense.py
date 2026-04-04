from datetime import datetime

class Expense:

    def __init__(self,amount, category , date : None):
       
       if amount <= 0:
            raise ValueError("Amount must be greater than 0")
       
       self.amount= amount 
       self.category = category 

       if date:
            self.date = date
       else:
            self.date = datetime.now().strftime("%Y-%m-%d")
    

    # convert to dict for json storing 

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }


    def __str__(self):
        return f"Date: {self.date} | Category: {self.category} | Amount: ₹{self.amount}"
        