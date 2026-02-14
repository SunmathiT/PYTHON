class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawn:", amount)
            else:
                print("Insufficient balance")
        else:
            print("Invalid withdraw amount")

    def display_balance(self):
        print("Current Balance:", self.balance)


# ---- Main Program ----
acc = BankAccount()

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amt = float(input("Enter amount to deposit: "))
        acc.deposit(amt)

    elif choice == 2:
        amt = float(input("Enter amount to withdraw: "))
        acc.withdraw(amt)

    elif choice == 3:
        acc.display_balance()

    elif choice == 4:
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice")
