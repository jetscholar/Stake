from ProofOfStake import ProofOfStake

if __name__ == '__main__': # This line checks whether the script is being run as the main program.
    pos = ProofOfStake()
    pos.update('bob', 10)
    pos.update('alice', 100)
    print(pos.get('bob'))
    print(pos.get('alice'))
    print(pos.get('jack'))