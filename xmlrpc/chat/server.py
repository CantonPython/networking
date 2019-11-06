# Demo chat server with xmlrpc

import os
import time
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from pprint import pprint


# Restrict path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class ChatServer:
    def __init__(self):
        self.sessions = {}

    def ping(self):
        return 'pong'

    def login(self, name, password):
        for token in self.sessions:
            session = self.sessions[token]
            if name == session['name']:
                return session['token']
        token = os.urandom(16).hex()
        self.sessions[token] = {
            'token': token,
            'name': name,
            'start': time.time(),
            'msg': ['welcome'],
        }
        return token

    def logout(self, token):
        self.sessions.pop(token, None)
        return 0

    def post(self, token, message):
        name = self.sessions[token]['name']
        msg = '({0}) {1}'.format(name, message)
        for key in self.sessions:
            if token != key:
                session = self.sessions[key]
                session['msg'].append(msg)
        return 0

    def get(self, token):
        msg = []
        if token in self.sessions:
            session = self.sessions[token]
            msg = session['msg']
            session['msg'] = []
        return msg

def main():
    addr = ('100.115.92.205', 8000)
    server = SimpleXMLRPCServer(addr, requestHandler=RequestHandler)
    server.register_introspection_functions()
    server.register_instance(ChatServer())
    server.serve_forever()

if __name__ == '__main__':
    main()
