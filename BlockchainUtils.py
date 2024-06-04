from Crypto.Hash import SHA256
import json

class BlockchainUtils():
    '''static methods allow class to be called without being instantiated
        - no need for self keyword
    '''
    @staticmethod
    def hash(data):
        dataString = json.dumps(data)
        dataBytes = dataString.encode('utf-8')
        dataHash = SHA256.new(dataBytes)
        return dataHash

