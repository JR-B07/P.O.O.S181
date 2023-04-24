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
        self.caja_popular = CajaPopular()

    def create_widgets(self):
        self.account_label = tk.Label(self)
        self.account_label["text"] = "Número de cuenta:"
        self.account_label.pack(side="left")

        self.account_entry = tk.Entry(self)
        self.account_entry.pack(side="left")

        self.amount_label = tk.Label(self)
        self.amount_label["text"] = "Cantidad:"
        self.amount_label.pack(side="left")

        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(side="left")

        self.balance_button = tk.Button(self)
        self.balance_button["text"] = "Consultar saldo"
        self.balance_button["command"] = self.show_balance
        self.balance_button.pack(side="left")

        self.deposit_button = tk.Button(self)
        self.deposit_button["text"] = "Depositar"
        self.deposit_button["command"] = self.deposit
        self.deposit_button.pack(side="left")

        self.withdraw_button = tk.Button(self)
        self.withdraw_button["text"] = "Retirar"
        self.withdraw_button["command"] = self.withdraw
        self.withdraw_button.pack(side="left")

        self.transfer_button = tk.Button(self)
        self.transfer_button["text"] = "Transferir"
        self.transfer_button["command"] = self.transfer
        self.transfer_button.pack(side="left")

        self.quit_button = tk.Button(self, text="Salir", fg="red",
                                     command=self.master.destroy)
        self.quit_button.pack(side="right")

        self.message_label = tk.Label(self, text="")
        self.message_label.pack(side="bottom")

        self.amount_label = tk.Label(self)
        self.amount_label["text"] = "Cantidad:"
        self.amount_label.pack(side="left")
        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(side="left")

    def show_balance(self):
        account_num = self.account_entry.get()
        account = self.caja_popular.get_account(account_num)
        if account:
            self.message_label.config(
                text="El saldo de la cuenta {} es de ${}".format(
                    account_num, account.balance))
        else:
            self.message_label.config(
                text="La cuenta {} no existe".format(account_num))
