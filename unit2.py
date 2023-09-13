class BankAccount:
    def__init__(self, account _number, account_holder_name,initial_balance):
        self._account_number=account_number
self._account_holder_name=account_holder_name
        self._account_balance=initial_balance
    def deposit(self, amount):
      if amount >0:
self._account_balance+=amount
        print("Deposited & {amount}.New balance:& {self._account_balance}.")
    else:
        print("Invalid deposit amount.please enter a positive amount.")
  def withdraw (self, amount):
    if amount >0 and amount <=
self._account_balance:
self._account_balance_=amount 
            print("withdraw & {amount}.New balance. & {self._account_balance}")elif amount<=0:
            print("invalid withdrawal amount.please enter a positive amount.")
      else:
print("Insufficient fund for withdrawal.")
    def display_balance(self):
       print(f"account 
holder:
{self._account_number}")
        print(f"account 
balance: &
  self{._account_balance}")
#creating an instance of the
Bankaccound class
account=
bankaccount("1234567890",
"john doe", 1000.0)

#Testing deposit and
withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()
