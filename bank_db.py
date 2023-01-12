from bank_model import Bank, Customer, Account, BankException, DBSession, init_db

db = DBSession().db_session()


def initialize_db():
    init_db()
    bank = Bank('Python Bank')
    db.add(bank)
    db.commit()
    return bank


def add_data():
    b = db.query(Bank).first()
    c1 = b.create_customer('John', 'Brownie', 'john@brown.com')
    db.add(c1)
    a1 = b.create_account(c1)
    db.add(a1)
    c2 = b.create_customer('Anne', 'Smithson', 'anne@email.com')
    db.add(c2)
    a2 = b.create_account(c2)
    db.add(a2)
    db.commit()


def query_db():
    #custs = db.query(Customer).filter(Customer.lastname == 'Brown').all()
    custs = db.query(Customer).filter(Customer.firstname == 'Anne').all()
    for c1 in custs:
        print(c1)
        print(c1.accounts)
        for a1 in c1.accounts:
            a1.deposit(500)
            db.merge(a1)
    db.commit()


if __name__ == '__main__':
    #initialize_db()
    #add_data()
    query_db()


#ef add_



# c = bank.create_customer('John', 'Brown')
# print(c)
# a1 = bank.create_account(c)
# a1.deposit(100)
# print(a1)
# try:
#     a = None
#     #a.charge(2)
#     a1.charge(50)
#     #a1.charge(-220)
#     a1.charge(200)
#
#     a1.deposit(-60)
#
# except BankException as my_ne:
#     print(f'Negative amount or not enough money!!! : {my_ne}')
#     print(f'Amount from exception: {my_ne.amount}')
# #except (NotEnoughMoneyException, NegativeAmountException) as ne:
# #    print(f'Negative amount or not enough money!!! : {ne}')
# #except Exception as e:
# #    print(f'Exception was thrown: {e}')
#
# # if a1.deposit(-60):
# #     print('Deposit to a1 succeeded')
# # else:
# #     print('Deposit to a1 not succeeded')
# a2 = bank.create_account(c)
# print(a2)
# c2 = bank.create_customer('Anne', 'Smith')
# a3 = bank.create_account(c2)
#
# print(bank)
#
