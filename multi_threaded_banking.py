import threading

# The bank account class
class BankAccount:
    # Initialize the account with a given balance
    def __init__(self, balance):
        self.balance = balance
        # Create a lock to synchronize access to the account
        self.lock = threading.Lock()

    # Method to deposit money into the account
    def deposit(self, amount):
        # Acquire the lock to synchronize access to the account
        self.lock.acquire()
        try:
            # Update the account balance
            self.balance += amount
        finally:
            # Release the lock
            self.lock.release()

    # Method to withdraw money from the account
    def withdraw(self, amount):
        # Acquire the lock to synchronize access to the account
        self.lock.acquire()
        try:
            # Update the account balance
            self.balance -= amount
        finally:
            # Release the lock
            self.lock.release()

# The thread class for depositing money
class DepositThread(threading.Thread):
    def __init__(self, account, amount):
        # Call the parent class's constructor
        super().__init__()
        # Store the account and amount to deposit
        self.account = account
        self.amount = amount

    def run(self):
        # Deposit the money into the account
        self.account.deposit(self.amount)

# The thread class for withdrawing money
class WithdrawThread(threading.Thread):
    def __init__(self, account, amount):
        # Call the parent class's constructor
        super().__init__()
        # Store the account and amount to withdraw
        self.account = account
        self.amount = amount

    def run(self):
        # Withdraw the money from the account
        self.account.withdraw(self.amount)

# Create a bank account with an initial balance of 1000
account = BankAccount(1000)

# Create a thread to deposit 500 into the account
deposit_thread = DepositThread(account, 500)

# Create a thread to withdraw 500 from the account
withdraw_thread = WithdrawThread(account, 500)

# Start the threads
deposit_thread.start()
withdraw_thread.start()

# Wait for the threads to finish
deposit_thread.join()
withdraw_thread.join()

# Print the final balance of the account
print(f"Final balance: {account.balance}")