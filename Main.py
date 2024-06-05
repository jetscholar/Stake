from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
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
    
    blockchain = Blockchain()
    
    lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount +1
    
    block = wallet.createBlock(pool.transactions, lastHash, blockCount)
    
    if not blockchain.lastBlockHashValid(block):
        print('lastBlockHash is not valid')
        
    if not blockchain.blockCountValid(block):
        print('Blockcount is not valid')
        
    if blockchain.lastBlockHashValid(block) and blockchain.blockCountValid(block):
        blockchain.addBlock(block)
    
    # printer.pprint(block.toJson())
    
    # print(block.toJson())
    # signatureValid = Wallet.signatureValid(block.payload(), block.signature, wallet.publicKeyString())
    
    # print(signatureValid)
    
    
    # blockchain.addBlock(block)
    printer.pprint(blockchain.toJson())
    
    