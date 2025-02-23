import json
import random
# --- Bank Application ---
class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount."
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Insufficient funds or invalid amount."

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    
    def create_account(self, name, initial_deposit):
        account_number = random.randint(1000, 9999)
        while account_number in self.accounts:
            account_number = random.randint(1000, 9999)
        
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        return f"Account created. Account Number: {account_number}"
    
    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return f"Account Number: {account.account_number}, Name: {account.name}, Balance: {account.balance}"
        return "Account not found."
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            result = self.accounts[account_number].deposit(amount)
            self.save_to_file()
            return result
        return "Account not found."
    
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            result = self.accounts[account_number].withdraw(amount)
            self.save_to_file()
            return result
        return "Account not found."
    
    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            json.dump({acc: vars(self.accounts[acc]) for acc in self.accounts}, file)
    
    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as file:
                data = json.load(file)
                self.accounts = {int(acc): Account(**data[acc]) for acc in data}
        except FileNotFoundError:
            self.accounts = {}
