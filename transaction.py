from datetime import date
import csv 

class Transaction:

    def __init__(self, transaction_type, amount, category, description):
        self._transaction_type=transaction_type
        self._amount=amount
        self.category=category
        self.description=description
        self.date=date.today()

    
    def __str__(self):
        return f"{self.transaction_type} | {self.amount} | {self.category} | {self.description} | {self.date}"


    def __repr__(self):
        return f"Type: '{self.transaction_type}' Amount: '{self.amount}' Category: {self.category} Description: '{self.description}' Date: {self.date}"
    @property    
    def transaction_type(self):
        return self._transaction_type
    

    @transaction_type.setter
    def transaction_type(self,value):
        if value in ("income", "expense"):
            self._transaction_type = value
        else:
            raise ValueError("Invalid entry!")
    

    @property
    def amount(self):
        return self._amount
    

    @amount.setter
    def amount(self, quantity):
        if quantity < 0:
            raise ValueError("You cannot enter a negative amount.")
        else:
            self._amount=quantity
    
    
class FinanceTracker:

    def __init__(self):
        self.list_=[]


    def income(self, amount, category, description):
        transaction = Transaction("income", amount, category, description)
        self.list_.append(transaction)


    def expense(self, amount, category, description):
        transaction2 = Transaction("expense", amount, category, description)
        self.list_.append(transaction2)


    def printlist(self):
        for element in self.list_:
            print(element)
    

    def get_balance(self):
        balance = 0
        for element in self.list_:
            if element.transaction_type == "income":
                balance += element.amount
            elif element.transaction_type == "expense":
                balance -= element.amount
        return balance
    

    def write_csv(self):
        with open("data.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["transaction_type", "amount", "category", "description", "date"])

            for element in self.list_:
                writer.writerow([element.transaction_type, element.amount,element.category,element.description,element.date])

    
    def read_csv(self):
        try:
            with open("data.csv", "r") as file:
                reader=csv.DictReader(file)

                for row in reader:
                    transaction = Transaction(
                        row["transaction_type"],
                        float(row["amount"]),
                        row["category"],
                        row["description"]
                    )
                    self.list_.append(transaction)
        except FileNotFoundError:
            pass
