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
        #TODO Add implementation
        pass

    def charge(self, amount):
        #TODO add implementation
        pass

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

    def __repr__(self):
        return f'Bank[{self.customer_list}, {self.account_list}]'


bank = Bank()
c = bank.create_customer('John', 'Brown')
print(c)
a1 = bank.create_account(c)
print(a1)
a2 = bank.create_account(c)
print(a2)
c2 = bank.create_customer('Anne', 'Smith')
a3 = bank.create_account(c2)

print(bank)

