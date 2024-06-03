from Crypto.Hash import SHA256
import json

class BlockchainUtils():
    '''static methods allow class to be called without being instantiated'''
    @staticmethod
    def hash(data):
        datastring = json.dumps(data)
        dataBytes = datastring.encode('utf-8')
        dataHash = SHA256.new(dataBytes)
        return dataHash

