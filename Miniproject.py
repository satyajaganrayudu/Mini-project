from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def transaction(self):
        pass


class Account(BankAccount):

    bank_name = "KIET Central Bank"

    def __init__(self, name, acc_no, balance, pin):
        self.name = name
        self._acc_no = acc_no
        self.__balance = balance
        self.__pin = pin

    def get_balance(self):
        return self.__balance

    def _update_balance(self, amount):
        self.__balance += amount

    def _verify_pin(self, entered_pin):
        return self.__pin == entered_pin

    @classmethod
    def display_bank_name(cls):
        print(f"\nBank Name: {cls.bank_name}")

    @staticmethod
    def validate_amount(amount):
        return amount > 0


class ATM(Account):

    def authenticate(self):
        attempts = 3
        while attempts > 0:
            pin = input("Enter your 4-digit PIN: ")
            if self._verify_pin(pin):
                print(" PIN verified successfully.")
                return True
            else:
                attempts -= 1
                print(f" Incorrect PIN. Attempts left: {attempts}")

        print(" ATM card blocked due to multiple incorrect PIN attempts.")
        return False

    def transaction(self):
        if not self.authenticate():
            return

        while True:
            print("\n====== ATM MENU ======")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View Account Details")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.check_balance()

            elif choice == "2":
                amount = float(input("Enter deposit amount: "))
                self.deposit(amount)

            elif choice == "3":
                amount = float(input("Enter withdrawal amount: "))
                self.withdraw(amount)

            elif choice == "4":
                self.view_details()

            elif choice == "5":
                print("\n Thank you for using the ATM")
                break

            else:
                print(" Invalid choice. Try again.")

    def check_balance(self):
        print(f"\n Current Balance: ₹{self.get_balance()}")

    def deposit(self, amount):
        if self.validate_amount(amount):
            self._update_balance(amount)
            print(f" ₹{amount} deposited successfully.")
        else:
            print(" Invalid deposit amount.")

    def withdraw(self, amount):
        if not self.validate_amount(amount):
            print(" Invalid withdrawal amount.")
        elif amount > self.get_balance():
            print(" Insufficient balance.")
        else:
            self._update_balance(-amount)
            print(f" ₹{amount} withdrawn successfully.")

    def view_details(self):
        print("\n Account Details")
        print(f"Name: {self.name}")
        print(f"Account Number: {self._acc_no}")
        print(f"Balance: ₹{self.get_balance()}")


Account.display_bank_name()

user = ATM("Ram", "KIET1234", 500000, "1718")
user.transaction()
