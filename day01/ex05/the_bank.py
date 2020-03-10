class Account(object):

	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		self.value = self.value if hasattr(self, 'value') else -1
		Account.ID_COUNT += 1

	def transfer(self, amount):
		self.value += amount
	
	def	debit(self, amount):
		self.value -= amount

class Bank(object):
	"""The bank"""
	def __init__(self):
		self.account = []
	def add(self, account):
		self.account.append(account)
	def transfer(self, origin, dest, amount):
		"""
		    @origin:  int(id) or str(name) of the first account
		    @dest:    int(id) or str(name) of the destination account
		    @amount:  float(amount) amount to transfer
		    @return         True if success, False if an error occured
		"""
		if (self.check_corruption(origin) or self.check_corruption(dest))\
			and not self.fix_account(origin) and not self.fix_account(dest):
			return False
		if origin.value - amount < 0:
			return False
		origin.debit(amount)
		dest.transfer(amount)
		return True

	def	check_corruption(self, origin):
		check_starting_zip = False
		if len(origin.__dict__.keys()) % 2 != 0:
			return 1
		for attribute in origin.__dict__.keys():
			if attribute[0] == 'b':
				return 1
			if attribute[0:3] == "zip" or attribute[0:4] == "addr":
				check_starting_zip = True
		if not hasattr(origin, 'name') or not hasattr(origin, 'value') or not hasattr(origin, 'id')\
			or not check_starting_zip or origin.id != self.account.index(origin) + 1 or origin.value < 0:
			return 1
		return 0
	def fix_account(self, account):
		"""
		    fix the corrupted account
		    @account: int(id) or str(name) of the account
		    @return         True if success, False if an error occured
		"""
		account.id = self.account.index(account) + 1
		return False if self.check_corruption(account) else True

bank = Bank()
kwargs = {"value": 16, "zip":1}
kwargs2 = {"value": 0, "zip":1}

bank.add(Account("a", **kwargs))
bank.add(Account("b", **kwargs2))
print(bank.transfer(bank.account[0], bank.account[1], 7))
print(bank.account[0].value)
print(bank.account[1].value)


