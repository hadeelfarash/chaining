class BankAccount:
	def __init__(self, int_rate=0.01, balance=0): 
		self.int_rate=0.01
		self.balance=balance
		
	def deposit(self, amount):
		self.balance+=amount
		return self
		
	def withdraw(self, amount):
		self.balance -= amount
		if self.balance==0:
			print("Insufficient funds: Charging a $5 fee and deduct $5")
		return self
	def display_account_info(self):
		print("Balance:", self.balance)
		return self
		
	def yield_interest(self):
		self.balance+= self.balance*self.int_rate
		
#chaining method	
mohammad=BankAccount(0.01,1000)
mohammad.deposit(100).deposit(200).deposit(300).withdraw(100).yield_interest()
print(mohammad.display_account_info())


Ahmad=BankAccount(0.01,3000)
Ahmad.deposit(100).deposit(200).withdraw(100).withdraw(200).withdraw(500).withdraw(800)

print(Ahmad.display_account_info())