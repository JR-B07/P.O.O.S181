import tkinter as tk

class Account:
    def __init__(self, account_number, account_holder, age, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.age = age
        self.balance = balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].balance
        else:
            return "Account not found"

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].balance += amount
        else:
            return "Account not found"

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount > self.accounts[account_number].balance:
                return "Insufficient funds"
            else:
                self.accounts[account_number].balance -= amount
        else:
            return "Account not found"

    def transfer(self, account_number, target_account, amount):
        if account_number in self.accounts and target_account in self.accounts:
            if amount > self.accounts[account_number].balance:
                return "Insufficient funds"
            else:
                self.accounts[account_number].balance -= amount
                self.accounts[target_account].balance += amount
        else:
            return "Account not found"

class BankGUI:
    def __init__(self, bank):
        self.bank = bank

        self.root = tk.Tk()
        self.root.title("Caja Popular")

        # Crear campos de entrada
        self.account_number_entry = tk.Entry(self.root)
        self.amount_entry = tk.Entry(self.root)

        # Crear etiquetas de texto
        self.account_number_label = tk.Label(self.root, text="No. Cuenta")
        self.account_holder_label = tk.Label(self.root, text="Titular")
        self.age_label = tk.Label(self.root, text="Edad")
        self.balance_label = tk.Label(self.root, text="Saldo")
        self.amount_label = tk.Label(self.root, text="Cantidad")

        # Crear botones
        self.balance_button = tk.Button(self.root, text="Consultar Saldo", command=self.get_balance)
        self.deposit_button = tk.Button(self.root, text="Ingresar Efectivo", command=self.deposit)
        self.withdraw_button = tk.Button(self.root, text="Retirar Efectivo", command=self.withdraw)
        self.transfer_button = tk.Button(self.root, text="Depositar a Otra Cuenta", command=self.transfer)

        # Colocar elementos en la ventana
        self.account_number_label.grid(row=0, column=0)
        self.account_number_entry.grid(row=0, column=1)
        self.balance_button.grid(row=1, column=0, columnspan=2)
        self.account_holder_label.grid(row=2, column=0)
        self.age_label.grid(row=3, column=0)
        self.balance_label.grid(row=4, column=0)
        self.amount_label.grid(row=5, column=0)
        self.amount_entry.grid(row=5, column=1)
        self.deposit_button.grid(row=6, column=0, columnspan=2)
        self.withdraw_button.grid(row=7, column=0, columnspan=2)
        self.transfer_button.grid(row=8, column=0, columnspan=2)
                        
       # Crear campos de salida
        self.account_holder_output = tk.Label(self.root, text="")
        self.age_output = tk.Label(self.root, text="")
        self.balance_output = tk.Label(self.root, text="")

        # Colocar campos de salida
        self.account_holder_output.grid(row=2, column=1)
        self.age_output.grid(row=3, column=1)
        self.balance_output.grid(row=4, column=1)

    def get_balance(self):
        account_number = self.account_number_entry.get()
        balance = self.bank.get_balance(account_number)
        if balance == "Account not found":
            self.account_holder_output.config(text="")
            self.age_output.config(text="")
            self.balance_output.config(text=balance)
        else:
            account = self.bank.accounts[account_number]
            self.account_holder_output.config(text=account.account_holder)
            self.age_output.config(text=str(account.age))
            self.balance_output.config(text=str(account.balance))

    def deposit(self):
        account_number = self.account_number_entry.get()
        amount = int(self.amount_entry.get())
        self.bank.deposit(account_number, amount)
        self.get_balance()

    def withdraw(self):
        account_number = self.account_number_entry.get()
        amount = int(self.amount_entry.get())
        result = self.bank.withdraw(account_number, amount)
        if result == "Account not found" or result == "Insufficient funds":
            self.account_holder_output.config(text="")
            self.age_output.config(text="")
        self.balance_output.config(text=result)
        self.get_balance()

    def transfer(self):
        account_number = self.account_number_entry.get()
        target_account = input("Enter the target account number: ")
        amount = int(self.amount_entry.get())
        result = self.bank.transfer(account_number, target_account, amount)
        if result == "Account not found" or result == "Insufficient funds":
            self.account_holder_output.config(text="")
            self.age_output.config(text="")
        self.balance_output.config(text=result)
        self.get_balance()

    def run(self):
        self.root.mainloop()

# Crear banco y cuentas de prueba
bank = Bank()
account1 = Account("123", "Juan Pérez", 25, 1000)
account2 = Account("456", "María González", 30, 500)
bank.add_account(account1)
bank.add_account(account2)

# Crear interfaz gráfica y ejecutarla
gui = BankGUI(bank)
gui.run()
