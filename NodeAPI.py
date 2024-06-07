from flask_classful import FlaskView, route
from flask import Flask


class NodeAPI(FlaskView):
    
    def __init__(self):
        self.app = Flask(__name__)
        
    def start(self, apiPort):
        NodeAPI.register(self.app, route_base='/')    
        self.app.run(host = 'localhost', port=apiPort)
        
    @route('/info', methods=['GET'])
    def info(self):
        return 'This is a communcation interface', 200