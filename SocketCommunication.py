from p2pnetwork.node import Node
from PeerDiscoveryHandler import PeerDiscoveryHandler
from SocketConnector import SocketConnector
from BlockchainUtils import BlockchainUtils
import json

class SocketCommunication(Node):
    
    def __init__(self, ip, port):
        super(SocketCommunication, self).__init__('0.0.0.0', port, None)  # Accept connections on all interfaces
        self.peers = self.loadPeers()  # Load previously saved peers
        self.peerDiscoveryHandler = PeerDiscoveryHandler(self)
        self.socketConnector = SocketConnector('0.0.0.0', port)  # Ensure P2P traffic is accepted

    def savePeers(self):
        with open("peers.json", "w") as f:
            json.dump(self.peers, f)

    def loadPeers(self):
        try:
            with open("peers.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        
    def connectToFirstNode(self):
        if self.socketConnector.port != 10001:
            if not self.peers:
                known_nodes = ['172.16.4.5', '192.168.1.117', '10.0.0.2']  # Add known first nodes

                for node_ip in known_nodes:
                    try:
                        self.connect_with_node(node_ip, 10001)
                        print(f"Connected to first node: {node_ip}")
                        break  # Stop after the first successful connection
                    except Exception as e:
                        print(f"Failed to connect to {node_ip}: {e}")
            else:
                print(f"Already connected to peers: {self.peers}")

    def startSocketCommunication(self, node):
        self.node = node
        self.start()
        self.peerDiscoveryHandler.start()
        self.connectToFirstNode()
        
    def inbound_node_connected(self, connected_node):
        self.peerDiscoveryHandler.handshake(connected_node)
        
    def outbound_node_connected(self, connected_node):
        self.peerDiscoveryHandler.handshake(connected_node)
        
    def node_message(self, connected_node, message):
        message = BlockchainUtils.decode(json.dumps(message))
        if message.messageType == 'DISCOVERY':
            self.peerDiscoveryHandler.handleMessage(message)
        elif message.messageType == 'TRANSACTION':
            transaction = message.data
            self.node.handleTransaction(transaction)
        elif message.messageType == 'BLOCK':
            block = message.data
            self.node.handleBlock(block)
        elif message.messageType == 'BLOCKCHAINREQUEST':
            self.node.handleBlockchainRequest(connected_node)
        elif message.messageType == 'BLOCKCHAIN':
            blockchain = message.data
            self.node.handleBlockchain(blockchain)
        
    def send(self, receiver, message):
        self.send_to_node(receiver, message)
        
    def broadcast(self, message):
        self.send_to_nodes(message)