class Banking:
    def __init__(self, user_name, initail_balance):
        self.name = user_name
        self.balance = initail_balance
        
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            
        return amount
    
    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return amount
        else:
            return print(f"Incificient Balance.")
    
        
                        
clint = Banking("Mridul", 10000)

print("Welcome to Bank Management System!!!")    
        
print(f"Account Name: {clint.name}")
print(f"Account Balance: {clint.balance}")
print(f"Deposite Balance: {clint.deposit(5000)}")
print(f"Main Balance: {clint.get_balance()}")
print(f"Withdrew Balance: {clint.withdraw(2000)}")
print(f"Main Balance: {clint.get_balance()}")
