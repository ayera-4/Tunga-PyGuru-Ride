class Bank_account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(f"Current balance is: {self.balance}")


def run_transactions(acc_object, action):
    if action == 1:
        amount = int(input("Enter amount: "))
        acc_object.deposit(amount)
        acc_object.display_balance()
    elif action == 2:
        amount = int(input("Enter amount: "))
        acc_object.withdrawal(amount)
        acc_object.display_balance()
    elif action == 3:
        acc_object.display_balance()


#Test Output
acc_num = input("Enter account number: ")
my_account = Bank_account(acc_num)

action_id = int(input("Enter 1 to Deposit or 2 to Withdrawal or 3 to Display balance: "))
run_transactions(my_account, action_id)