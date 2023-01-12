from sqlalchemy import Column, Integer, String, create_engine, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(50), nullable=True)
    lastname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=True)
    accounts = relationship('Account', back_populates='customer')

    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def __repr__(self):
        return f'Customer[{self.id}, {self.firstname}, {self.lastname}, {self.email}]'


class Account:
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float)
    fk_customer_id = Column(Integer, ForeignKey(Customer.id), index=True, nullable=False)
    customer = relationship(Customer, back_populates='accounts')

    def __init__(self, customer):
        self.customer = customer
        self._balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise NegativeAmountException(f'Amount passed is negative: {amount}', amount)
        self._balance += amount

    def charge(self, amount):
        if amount <= 0:
            raise NegativeAmountException(f'Amount passed is negative: {amount}', amount)
        if amount > self._balance:
            raise NotEnoughMoneyException(f'Is not enough money to charge : {amount}', amount)
        self._balance -= amount

    def __repr__(self):
        return f'Acount[{self.id}, {self.customer.lastname}, {self._balance}]'


class Bank:
    def __init__(self):
        self.account_list = []
        self.customer_list = []

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.account_list.append(a)
        return a

    def transfer(self, from_account_id, to_account_id, amount):
        #TODO implement by finding the appropriate accounts in self.account_list and then performing
        # charge and deposit
        pass


    def find_account(self, id):
        # search through the self.accoun_list and return the account
        pass

    def __repr__(self):
        return f'Bank[{self.customer_list}, {self.account_list}]'

class BankException(Exception):
    def __init__(self, msg, amount):
        super().__init__(msg)
        self.amount = amount


class NotEnoughMoneyException(BankException):
    def __init__(self, msg, amount):
        super().__init__(msg, amount)

class NegativeAmountException(BankException):
    def __init__(self, msg, amount):
        super().__init__(msg, amount)


bank = Bank()
c = bank.create_customer('John', 'Brown')
print(c)
a1 = bank.create_account(c)
a1.deposit(100)
print(a1)
try:
    a = None
    #a.charge(2)
    a1.charge(50)
    #a1.charge(-220)
    a1.charge(200)

    a1.deposit(-60)

except BankException as my_ne:
    print(f'Negative amount or not enough money!!! : {my_ne}')
    print(f'Amount from exception: {my_ne.amount}')
#except (NotEnoughMoneyException, NegativeAmountException) as ne:
#    print(f'Negative amount or not enough money!!! : {ne}')
#except Exception as e:
#    print(f'Exception was thrown: {e}')

# if a1.deposit(-60):
#     print('Deposit to a1 succeeded')
# else:
#     print('Deposit to a1 not succeeded')
a2 = bank.create_account(c)
print(a2)
c2 = bank.create_customer('Anne', 'Smith')
a3 = bank.create_account(c2)

print(bank)

