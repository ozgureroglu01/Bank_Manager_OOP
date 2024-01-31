class BankAccount:
    next_account_number = 1
    def __init__(self,account_holder_name,balance=0):
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number +=1
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self,m):
        self.balance += m 

    def withdraw(self,m):
        if self.balance > 0 and m <= self.balance:
            self.balance -= m 
        else:
            raise ValueError("You cant withdraw more money than there is in your account")
    
    def check_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}\nHolder Name: {self.account_holder_name}\nBalance: {self.balance}"

def main():
    account = get_account()
    print(account)

def get_account():
    name = input("Please enter your name: ")
    try:
        balance = float(input("Enter your balance: "))
    except ValueError:
        print("Enter a valid number")

    return BankAccount(name,balance)
    

if __name__ == "__main__":
    main()