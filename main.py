from transaction import FinanceTracker
def get_amount():
    while True:
        try:
            amount = float(input("Amount: "))
            if amount < 0:
                print("Amount cannot be negative!")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number!")

def main():
    finance = FinanceTracker()
    finance.read_csv()

    while True:

        print("\n1. Add income.")
        print("2. Add expense.")
        print("3. List transaction.")
        print("4. Get balance")
        print("5. Quit")

        choice = input("Choose: ")

        if choice == "1":
            get_amount()
            category = input("Category:")
            description = input("Description: ")
            finance.income(amount, category,description)
        
        elif choice == "2":
            get_amount()
            category = input("Category: ")
            description = input("Description: ")
            finance.expense(amount, category, description)


        elif choice == "3":

            if not finance.list_:
                print("No transactions yet!")
            else:
                finance.printlist()
        
        elif choice == "4":
            if not finance.list_:
                print("No transactions yet!")
            else:
                balance = finance.get_balance()
                print(f"Balance: {balance}")
        
        elif choice == "5":
            finance.write_csv()
            break
        
        else :
            print("Invalid choice!")

if __name__ == "__main__":
    main()