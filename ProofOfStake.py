

class ProofOfStake():
    '''
    Keeps track of stakers public keys
    and the stake amount.
    
    '''
    def __init__(self):
        self.stakers = {}
        
    def update(self, publicKeyString, stake):
        '''
        checks if the publickey is in the dictionary,
        if not it adds the stake, else updates it
        '''
        if publicKeyString in self.stakers.keys():
            self.stakers[publicKeyString] += stake
        else:
            self.stakers[publicKeyString] = stake
            
    def get(self, publicKeyString):
        '''
        Checks if the public key is in the dictionary, 
        returns it if so else returns nothing.
        '''
        if publicKeyString in self.stakers.keys():
            return self.stakers[publicKeyString]
        else:
            return None