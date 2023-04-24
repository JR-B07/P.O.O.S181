from tkinter import *
import tkinter as tk
from tkinter import messagebox


class Account:
    def __init__(self, account_num, holder_name, age, balance):
        self.account_num = account_num
        self.holder_name = holder_name
        self.age = age
        self.balance = balance


class CajaPopular:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def get_account(self, account_num):
        for account in self.accounts:
            if account.account_num == account_num:
                return account
        return None


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Caja Popular")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.account_label = tk.Label(self, text="Número de cuenta:")
        self.account_label.pack(side="left")

        self.account_entry = tk.Entry(self)
        self.account_entry.pack(side="left")

        self.amount_label = tk.Label(self, text="Cantidad:")
        self.amount_label.pack(side="left")

        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(side="left")

        self.balance_button = tk.Button(self, text="Consultar saldo", command=self.show_balance)
        self.balance_button.pack(side="left")

        self.deposit_button = tk.Button(self, text="Depositar", command=self.deposit)
        self.deposit_button.pack(side="left")

        self.withdraw_button = tk.Button(self, text="Retirar", command=self.withdraw)
        self.withdraw_button.pack(side="left")

        self.transfer_button = tk.Button(self, text="Transferir", command=self.transfer)
        self.transfer_button.pack(side="left")

        self.quit_button = tk.Button(self, text="Salir", fg="red", command=self.master.destroy)
        self.quit_button.pack(side="right")

        self.message_label = tk.Label(self, text="")
        self.message_label.pack(side="bottom")

    def show_balance(self):
        account_num = self.account_entry.get()
        account = CajaPopular.get_account(account_num)
        if account:
            self.message_label.config(text=f"El saldo de la cuenta {account_num} es de ${account.balance}")
        else:
            self.message_label.config(text=f"La cuenta {account_num} no existe")

    def deposit(self):
        account_num = self.account_entry.get()
        account = CajaPopular.get_account(account_num)
        if account:
            amount = float(self.amount_entry.get())
            account.balance += amount
            self.message_label.config(text=f"Se depositaron ${amount} en la cuenta {account_num}")
        else:
            self.message_label.config(text=f"La cuenta {account_num} no existe")
        
    def withdraw(self):
        account_num = self.account_entry.get()
        account = CajaPopular.get_account(account_num)
        if account:
            amount = float(self.amount_entry.get())
            if amount <= account.balance:
                account.balance -= amount
                self.message_label.config(text=f"Se retiraron ${amount} de la cuenta {account_num}")
            else:
                self.message_label.config(text=f"No hay suficiente saldo en la cuenta {account_num}")
        else:
            self.message_label.config(text=f"La cuenta {account_num} no existe")
            

    def transfer(self):
        account_num = self.account_entry.get()
        account = CajaPopular.get_account(account_num)
        if account:
            dest_account_num = self.get_dest_account_num()
            dest_account = CajaPopular.get_account(dest_account_num)
            if dest_account:
                amount = float(self.amount_entry.get())
                if amount <= account.balance:
                    account.balance -= amount
                    dest_account.balance += amount
                    self.message_label.config(text="Se transfirieron ${} de la cuenta {} a la cuenta {}".format(amount, account_num, dest_account_num))
                else:
                    self.message_label.config(text="Saldo insuficiente en la cuenta {}".format(account_num))
            else:
                self.message_label.config(text="La cuenta de destino {} no existe".format(dest_account_num))
        else:
            self.message_label.config(text="La cuenta {} no existe".format(account_num))

CajaPopular = CajaPopular()
CajaPopular.add_account(Account("123", "Juan Perez", 25, 1000.0))
CajaPopular.add_account(Account("456", "Maria Rodriguez", 30, 500.0))
CajaPopular.add_account(Account("789", "Pedro Gomez", 40, 2000.0))
            
root = tk.Tk()
app = Application(master=root)
app.mainloop()
