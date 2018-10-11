from builtins import print


class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    tag = "#Customer Tag#"

    def __init__(self, name):
        """Return a Customer object whose name is *name*."""
        self.name = name

    def set_balance(self, balance=0.0):
        """Set the customer's starting balance."""
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance

    @staticmethod
    def staticmethodsample():
        print("in Static Method...")

    @classmethod
    def classmethodsample(cls):
        print("in Class method {}".format(cls.tag))

c = Customer("touraj")
c.set_balance()
c.deposit(1000)
balance = c.withdraw(100)
print("Balance is {}".format(balance))
c.staticmethodsample()
Customer.staticmethodsample()
Customer.classmethodsample()