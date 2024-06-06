

class TransactionPool():
    
    def __init__(self):
        self.transactions = []
        
    def addTransaction(self, transaction):
        self.transactions.append(transaction)
        
    def transactionExists(self, transaction):
        # check if transaction exists
        for poolTransaction in self.transactions:
            if poolTransaction.equals(transaction):
                return True
        return False
    
    def removeFromPool(self, transactions):
        newPoolTransactions = []
        for poolTransaction in self.transactions:
            insert = True
            for transaction in transactions:
                if poolTransaction.equals(transaction):
                    insert = False
            if insert == True:
                newPoolTransactions.append(poolTransaction)
        self.transactions = newPoolTransactions