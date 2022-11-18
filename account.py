class Account():
    def __init__(self, name: str) -> None:
        self.__account_name = name
        self.__account_balance = 0                      # Set the defaults up here

    def deposit(self, amount) -> bool:
        if amount <= 0:                                 # Returns false if less than or is zero
            return False
        else:
            self.__account_balance += amount            # Returns True is greater than zero and adds to the account
            return True

    def withdraw(self, amount) -> bool:
        if amount > self.__account_balance:            # If the amount trying to withdraw is less than the account
            return False                                # It will return false
        elif amount <= 0:
            return False
        else:
            self.__account_balance -= amount            # If the amount is trying to withdraw an appropriate amount
            return True                                 # it will return true

    def get_balance(self) -> float:
        return self.__account_balance                   # Returns the account balance

    def get_name(self) -> str:
        return self.__account_name                      # Returns the account name


