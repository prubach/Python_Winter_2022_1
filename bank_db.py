from bank_model import Bank, Customer, Account, BankException, DBSession, init_db

db = DBSession().db_session()


def initialize_db():
    init_db()
    bank = Bank('Python Bank')
    db.add(bank)
    db.commit()
    return bank




if __name__ == '__main__':
    initialize_db()

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
