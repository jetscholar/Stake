import threading
import time

class PeerDiscoveryHandler():
    
    def __init__(self, node):
        self.socketCommunication = node
    
    def discovery(self):
        while True:
            print('discovery')
            time.sleep(10)