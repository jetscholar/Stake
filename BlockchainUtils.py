from Crypto.Hash import SHA256
import json
import jsonpickle

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
    
    @staticmethod
    def encode(objectToEncode):
        return jsonpickle.encode(objectToEncode, unpicklable=True)
    
    @staticmethod
    def decode(encodedObject):
        return jsonpickle.decode(encodedObject)

