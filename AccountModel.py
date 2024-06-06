

class AccountModel():
    
    def __init__(self):
        self.accounts = [] # public keys of users
        self.balances = {} # map between key and balance
        
    def addAccount(self, publicKeyString):
        if not publicKeyString in self.accounts:
            self.accounts.append(publicKeyString)
            self.balances[publicKeyString] = 0
            
    def getBalance(self, publicKeyString):
        if publicKeyString not in self.accounts:
            self.addAccount(publicKeyString)
        return self.balances[publicKeyString]
    
    def updateBalance(self, publicKeyString, amount):
        if publicKeyString not in self.accounts:
            self.addAccount(publicKeyString)
        self.balances[publicKeyString] += amount
        