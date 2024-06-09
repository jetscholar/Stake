from Lot import Lot
from BlockchainUtils import BlockchainUtils

class ProofOfStake():
    '''
    Keeps track of stakers' public keys
    and the stake amount.
    
    '''
    def __init__(self):
        self.stakers = {}
        self.setGenesisNodeStake()
        
    def setGenesisNodeStake(self):
        '''
            Sets the first staker as the genesis with amount of 1
        '''
        genesisPublicKey = open('keys/genesisPublicKey.pem', 'r').read()
        self.stakers[genesisPublicKey] = 1
        
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
        
    def validatorLots(self, seed):
        lots = []
        for validator in self.stakers.keys():
            for stake in range(self.get(validator)):
                lots.append(Lot(validator, stake+1, seed))
        return lots
    
    def winnerLot(self, lots, seed):
        '''
            Iterates over the lots, determins which is
            nearest to the reference lot
            determines winner lot
        '''
        winnerLot = None
        leastOffset = None
        referenceHshIntValue = int(BlockchainUtils.hash(seed).hexdigest(), 16)
        for lot in lots:
            lotIntValue = int(lot.lotHash(), 16)
            offset = abs(lotIntValue-referenceHshIntValue)
            if leastOffset is None or offset < leastOffset:
                leastOffset = offset
                winnerLot = lot
        return winnerLot
    
    def forger(self, lastBlockHash):
        lots = self.validatorLots(lastBlockHash)
        winnerLot = self.winnerLot(lots, lastBlockHash)
        return winnerLot.publicKey