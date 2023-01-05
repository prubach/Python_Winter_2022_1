class Customer:
    last_id = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f'Customer[{self.id}, {self.firstname}, {self.lastname}]'


class Account:
    last_id = 1000

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
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

