from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import pprint

printer = pprint.PrettyPrinter()

if __name__ == '__main__':
    
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'
    
    # transaction = Transaction(sender, receiver, amount, type)
    # # print(transaction.toJson()) # test 1
    
    # wallet = Wallet()
    # signature = wallet.sign(transaction.toJson())
    # #print(signature)
    
    # transaction.sign(signature)
    # #print(transaction.toJson())
    
    # # check the signature
    # signatureValid = Wallet.signatureValid(transaction.payload(), signature, wallet.publicKeyString())
    
    # print(signatureValid)
    
    wallet = Wallet()
    fraudWallet = Wallet()
    
    pool = TransactionPool()
    
    transaction = wallet.createTransaction(receiver, amount, type)
    
    # print(transaction.toJson())
    
    # signatureValid = Wallet.signatureValid(transaction.payload(), transaction.signature, fraudWallet.publicKeyString())
    
    # print(signatureValid)
    
    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)
        
    # print(pool.transactions)
    
    #block = Block(pool.transactions, 'lastHash', 'forger', 1)
    
    # printer.pprint(block.toJson())
    
    block = wallet.createBlock(pool.transactions, 'lastHash', 1)
    
    # printer.pprint(block.toJson())
    
    # print(block.toJson())
    signatureValid = Wallet.signatureValid(block.payload(), block.signature, wallet.publicKeyString())
    
    print(signatureValid)
    