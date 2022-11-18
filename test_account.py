from account import *


class Test:
    def setup_method(self):
        self.p1 = Account('Paige')

    def teardown_method(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == 'Paige'
        assert self.p1.get_balance() == 0

    def test_deposit(self):
        '''
        Test function is used to test the deposit method
        in the Account class
        Testing Negative, Positive, and Zero values
        :param amount: Deposited amount
        :return: Function should return True or False
        '''
        assert self.p1.deposit(30) is True
        assert self.p1.deposit(0) is False
        assert self.p1.deposit(-50) is False

    def test_withdraw(self):
        '''
        Test function used to test the withdraw method
        in the Account class
        Testing Negative, Positive, and Zero values
        :param amount: Withdrawn Amount
        :return: Function should return True or False
        '''
        # Account is set to zero here
        assert self.p1.withdraw(0) is False
        assert self.p1.withdraw(30) is False

        # Adding funds to the account to test withdraw
        self.p1.deposit(50)
        assert self.p1.withdraw(30) is True
        assert self.p1.withdraw(60) is False
        assert self.p1.withdraw(-59) is False

    def test_get_balance(self):
        '''
        Test function used to test the get_balance
        method in the Account class
        :return: Function should return True or False
        '''
        # Testing account p1 (Paige)
        assert self.p1.get_balance() == 0
        assert self.p1.get_balance() != 50

    def test_get_name(self):
        '''
        Test function used to test the get_name
        method in the Account class
        :return: Function should return True or False
        '''
        assert self.p1.get_name() == 'Paige'
        assert self.p1.get_name() != 'Paaaaaige'


