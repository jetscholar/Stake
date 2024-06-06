from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from Node import Node
import sys
import pprint



printer = pprint.PrettyPrinter()

if __name__ == '__main__':
    
    ip = sys.argv[1]
    port = int(sys.argv[2])
    
    node = Node(ip, port)
    node.startP2P()
    
    if port == 10002:
        node.p2p.connect_with_node('localhost', 10001)

    
    
    
    
    
    
#     blockchain = Blockchain()
#     pool = TransactionPool()
    
#     alice = Wallet()
#     bob = Wallet()
#     exchange = Wallet()
#     forger = Wallet()
    
#     exchangeTransaction = exchange.createTransaction(alice.publicKeyString(), 10, 'EXCHANGE')
    
#     if not pool.transactionExists(exchangeTransaction):
#         pool.addTransaction(exchangeTransaction)
    
        
#     coveredTransaction = blockchain.getCoveredTranasctionSet(pool.transactions)
#     lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
#     blockCount = blockchain.blocks[-1].blockCount + 1
#     # blockOne = Block(coveredTransaction, lastHash, forger.publicKeyString(), blockCount)
#     blockOne = forger.createBlock(coveredTransaction, lastHash, blockCount)
#     blockchain.addBlock(blockOne)
#     pool.removeFromPool(blockOne.transactions)
    
#     # alice sends 5 token to bob
#     transaction = alice.createTransaction(bob.publicKeyString(), 5, 'TRANSFER')
    
#     if not pool.transactionExists(transaction):
#         pool.addTransaction(transaction)
        
#     coveredTransaction = blockchain.getCoveredTranasctionSet(pool.transactions)
#     lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
#     blockCount = blockchain.blocks[-1].blockCount + 1
#     # blockTwo = Block(coveredTransaction, lastHash, forger.publicKeyString(), blockCount)
#     blockTwo = forger.createBlock(coveredTransaction, lastHash, blockCount)
#     blockchain.addBlock(blockTwo)    
#     pool.removeFromPool(blockTwo.transactions)
    
    
#     printer.pprint(blockchain.toJson())
    
    
    #print(coveredTransaction)
        
    
    # wallet = Wallet()
    # accountModel = AccountModel()
    
    # #accountModel.addAccount(wallet.publicKeyString)
    # accountModel.updateBalance(wallet.publicKeyString(), 10)
    # accountModel.updateBalance(wallet.publicKeyString(), -5)
    
    # print(accountModel.balances)
    
    
    # sender = 'sender'
    # receiver = 'receiver'
    # amount = 1
    # type = 'TRANSFER'
    
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
    
    #action = wallet.createTransaction(receiver, amount, type)
    
    # print(transaction.toJson())
    
    # signatureValid = Wallet.signatureValid(transaction.payload(), transaction.signature, fraudWallet.publicKeyString())
    
    # print(signatureValid)
    
    #if pool.transactionExists(transaction) == False:
    #    pool.addTransaction(transaction)
        
    # print(pool.transactions)
    
    #block = Block(pool.transactions, 'lastHash', 'forger', 1)
    
    # printer.pprint(block.toJson())
    
    # blockchain = Blockchain()
    
    # lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    # blockCount = blockchain.blocks[-1].blockCount +1
    
    # block = wallet.createBlock(pool.transactions, lastHash, blockCount)
    
    #if not blockchain.lastBlockHashValid(block):
    #    print('lastBlockHash is not valid')
        
    # if not blockchain.blockCountValid(block):
    #    print('Blockcount is not valid')
        
    #if blockchain.lastBlockHashValid(block) and blockchain.blockCountValid(block):
        #blockchain.addBlock(block)
    
    # printer.pprint(block.toJson())
    
    # print(block.toJson())
    # signatureValid = Wallet.signatureValid(block.payload(), block.signature, wallet.publicKeyString())
    
    # print(signatureValid)
    
    
    # blockchain.addBlock(block)
    # printer.pprint(blockchain.toJson())
    
    