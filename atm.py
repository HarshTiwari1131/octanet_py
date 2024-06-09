class ATM:
    def _init_(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def authenticate(self, input_pin):
        return input_pin == self.pin

    def check_balance(self):
        return f"Your current balance is: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount:.2f}")
        return f"Successfully deposited ${amount:.2f}. {self.check_balance()}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: ${amount:.2f}")
        return f"Successfully withdraw ${amount:.2f}. {self.check_balance()}"

    def get_transaction_history(self):
        if not self.transaction_history:
            return "No transactions yet."
        return "\n".join(self.transaction_history)

def main():
    atm = ATM(pin="1234")
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        input_pin = input("Enter your PIN: ")
        if atm.authenticate(input_pin):
            break
        else:
            attempts += 1
            print(f"Incorrect PIN. {max_attempts - attempts} attempts left.")

    if attempts == max_attempts:
        print("Too many incorrect attempts. Exiting.")
        return

    session_transactions = 0
    max_session_transactions = 5

    while True:
        if session_transactions >= max_session_transactions:
            print("Maximum transactions for this session reached. Please log in again.")
            break

        print("\nWelcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")
        choice = input("Please select an option: ")

        if choice == '1':
            print(atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit(amount))
            session_transactions += 1
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw(amount))
            session_transactions += 1
        elif choice == '4':
            print(atm.get_transaction_history())
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if _name_ == "_main_":
    main()
