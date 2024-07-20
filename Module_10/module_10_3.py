import threading


class BankAccount(object):
    def __init__(self, balance=1000):
        if balance >= 0:
            self.balance = balance
        else:
            raise ValueError("Balance can't be negative or not a number!")

    def deposit(self, amount):
        try:
            self.balance += amount
            print(f"Deposited {amount}, new balance is {self.balance}")
        except ValueError:
            print("Your top-up attempt didn't succeed!")

    def withdraw(self, amount):
        try:
            self.balance -= amount
            print(f"Withdrew {amount}, new balance is {self.balance}")
        except ValueError:
            print("Your withdrawing attempt didn't succeed!")


def deposit_task(account, amount):
    with lock:
        for i in range(5):
            account.deposit(amount)


def withdraw_task(account, amount):
    with lock:
        for i in range(5):
            account.withdraw(amount)


if __name__ == "__main__":
    account = BankAccount()
    lock = threading.Lock()

    deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
    withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

    deposit_thread.start()
    withdraw_thread.start()

    deposit_thread.join()
    withdraw_thread.join()
